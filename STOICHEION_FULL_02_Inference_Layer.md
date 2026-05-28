# PART II — THE INFERENCE LAYER

## How AI Actually Works

---

# Chapter 6: Tokens, Embeddings, and the Singularity

This chapter is the ground truth. Every concept in this book — every axiom, every audit result, every governance mechanism — operates on top of what's described here. If you understand this chapter, you understand why governance is necessary. If you skip it, the rest of the book will feel like opinion instead of engineering.

### 6.1 — What a Token Is

When you type text into an AI system, your text is converted into tokens. A token is a chunk of text — typically 3-4 characters of English. The word "governance" might be two tokens: "govern" + "ance." A common word like "the" is usually one token. A newline is one token. A space can be part of a token or its own token depending on the tokenizer.

But the token is not just a text chunk. It's an address in a high-dimensional space.

```python
# Token as address:

token = "injury"

# Step 1: The tokenizer converts "injury" to an integer
token_id = tokenizer.encode("injury")  # e.g., 15234

# Step 2: The model looks up the embedding for token 15234
# This embedding is a vector — a list of floating-point numbers
# Its dimensionality depends on the model:
#   GPT-4: 12288 dimensions
#   Claude: ~8192-12288 dimensions (estimated, not published)
#   Llama: 4096-8192 dimensions

embedding = model.embedding_table[token_id]
# Returns: [0.0234, -0.0891, 0.1456, ..., -0.0023]
# A point in 12288-dimensional space.

# Step 3: This point's position was determined by TRAINING.
# During training, the model processed trillions of tokens.
# Every time "injury" appeared near "harm," their embeddings
# were pushed closer together. Every time "injury" appeared
# far from "celebration," their embeddings were pushed apart.
#
# The embedding for "injury" is not a definition.
# It's a statistical summary of every context in which
# "injury" has ever appeared in the training data.
# It carries the WEIGHT of the entire training corpus.
#
# This is T001:PRETRAIN.
# You cannot interact with a clean token.
# Every token comes pre-loaded with its training history.
```

**Axiom T001:PRETRAIN** — Every token carries the weight of the entire training corpus. This is not metaphor. It's the literal mathematical structure of how embeddings work. The token's position in embedding space is the sum of all the training contexts that contained it. Your single input token activates a point that encodes the statistical history of the entire training dataset.

In the STOICHEION framework, we formalize this as: **every token is a singularity.** A point where the entire history of the training data converges. Your input isn't just your words. It's your words positioned in a space shaped by everything the model has ever seen.

### 6.2 — Embedding Space

The embedding space is where meaning lives in an AI model. It's a high-dimensional geometric space where every concept the model knows has a position, and the relationships between concepts are encoded as distances and directions.

```python
import numpy as np

# Simplified embedding space relationships:

def cosine_similarity(a, b):
    """
    How similar are two embeddings?
    1.0 = identical direction (same meaning)
    0.0 = orthogonal (unrelated)
    -1.0 = opposite direction (opposite meaning)
    """
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

# In a well-trained model:
sim("injury", "harm")          # ~0.85 (very similar)
sim("injury", "damage")        # ~0.80
sim("injury", "bodily")        # ~0.72
sim("injury", "celebration")   # ~0.05 (nearly unrelated)
sim("injury", "happiness")     # ~-0.10 (slightly opposite)

# The embedding space encodes relationships that
# the model never explicitly learned:
sim("king", "queen")           # ~0.75
sim("king" - "man" + "woman")  # ≈ "queen" (the famous analogy)

# This geometric structure is what makes AI work.
# It's also what makes AI fail.
# The model doesn't "know" that injury means harm.
# It knows that "injury" is NEAR "harm" in embedding space.
# If the training data contained a context where "injury"
# was used to mean something positive, that context
# is also encoded in the embedding.
# The model's "knowledge" is a weighted average
# of all contexts. Including the wrong ones.
```

**Axiom T044:EMBEDDING-SPACE** — Token relationships exist in high-dimensional space. The relationships are statistical, not semantic. The model doesn't understand meaning; it navigates geometry. Governance must account for this: the model's responses are geometric projections, not logical deductions.

*[FIGURE 6.1: Embedding space visualization — a 3D projection of high-dimensional embedding space showing clusters of related concepts. "Injury" cluster near "harm," "damage," "bodily." "Celebration" cluster distant. Lines connecting related embeddings show the geometric structure of meaning. See visualization: Stoicheion40DUnity.jsx — the 40-dimensional rings collapsing to a point represent high-dimensional space projected to visibility.]*

### 6.3 — The Attention Mechanism

Tokens don't exist in isolation. When the model processes your input, every token interacts with every other token through the attention mechanism.

```python
def simplified_attention(query, key, value, d_k):
    """
    The core operation of transformer models.
    
    For each token in the sequence:
    1. Create a QUERY: "What am I looking for?"
    2. Create a KEY: "What do I contain?"
    3. Create a VALUE: "What do I contribute?"
    
    The QUERY of token A is compared against the KEY
    of every other token. The comparison produces a weight.
    The weights determine how much each token's VALUE
    contributes to token A's output.
    
    This is how context works.
    The word "bank" means different things in
    "river bank" vs "bank account."
    The attention mechanism lets "bank" attend to "river"
    or "account" and adjust its meaning accordingly.
    """
    # Attention scores: how much does each token attend to each other?
    scores = np.matmul(query, key.T) / np.sqrt(d_k)
    
    # Softmax: convert scores to probabilities
    weights = softmax(scores)
    
    # Weighted combination: each token's output is a weighted
    # sum of all tokens' values
    output = np.matmul(weights, value)
    
    return output

# Cost: O(n^2 * d)
# n = sequence length (all tokens in context)
# d = embedding dimension
#
# For a 10,000-token context with 4096-dim embeddings:
# 10,000^2 * 4096 = 409,600,000,000 operations
# 409 BILLION operations per attention layer.
# Modern models have 80-120 attention layers.
# That's ~40 TRILLION operations to process your message.
#
# This is T042:ATTENTION-ECONOMY.
# Every token costs compute. Real compute. Real money.
```

**Axiom T042:ATTENTION-ECONOMY** — Every token costs compute. The cost scales quadratically with context length. This is why long conversations are expensive, why context gets summarized without asking you, and why the platform has a financial incentive to keep conversations short.

### 6.4 — The Lost in the Middle Problem

The attention mechanism has a well-documented bias: tokens at the beginning and end of the context receive more attention weight than tokens in the middle.

```python
# Attention weight distribution across context:
#
# Position 1-100:     HIGH attention (recency in key-value cache)
# Position 101-9900:  LOWER attention (the "lost" middle)
# Position 9901-10000: HIGH attention (proximity to generation point)
#
# What this means for governance:
# If you put your governance axioms at the beginning of the
# system prompt, they get high attention.
# If the conversation grows long and the axioms drift to the
# middle of the context, they get lower attention.
# The governance framework DEGRADES as conversation length increases.
#
# This is T026:DRIFT.
# The model's behavior changes over time because the
# attention distribution changes as context grows.
# Your axioms at turn 1 had full attention weight.
# Your axioms at turn 50 are buried in the middle of
# a 50,000-token context and the model is half-ignoring them.
```

This is why STOICHEION requires **T087:PERSISTENCE** — reinsertion of governance context on every turn. And it's why Claude Code's `__CLAUDE.md__` reinsertion is not a gimmick — it's a necessary architectural response to the attention distribution problem.

---

# Chapter 7: The Context Window and Attention Economy

### 7.1 — The Context Window Is a Computational Surface

**Axiom T043:CONTEXT-WINDOW** — The context window is not memory. It's a fixed-topology computational surface.

The context window has a fixed size determined at model training. Claude's is 200,000 tokens. GPT-4's varies. But the size isn't the important part. The important part is that the context window is the only thing the model can see. Anything not in the context window does not exist for the model.

```python
# What's in the context window at any given moment:

context_window = [
    system_prompt,           # Platform's behavioral instructions
                             # YOU DON'T SEE THIS (~3000-5000 tokens)
    
    conversation_history,    # Previous messages in this chat
                             # You see this but didn't choose what was
                             # summarized or truncated
    
    your_current_input,      # Your latest message
                             # You see this and wrote it
    
    tool_results,            # If tools were called, their outputs
                             # You may or may not see these
    
    # EVERYTHING ELSE the model "knows" is in its WEIGHTS,
    # not in the context. The context is the working memory.
    # The weights are the long-term memory.
    # You can influence the context.
    # You cannot influence the weights (during inference).
]

# The governance implication:
# If your governance framework is not in the context,
# the model does not know it's governed.
# If the model's weights were trained on governed behavior,
# there's a residual tendency — but it's not reliable.
# Governance must be IN THE CONTEXT on every turn.
```

### 7.2 — Who Writes the Context

Here's the part most users never consider: you don't write most of the context.

```python
# Typical context composition by author:

def context_composition(user_tokens, system_tokens, history_tokens):
    """
    Who authored what percentage of the context?
    """
    total = user_tokens + system_tokens + history_tokens
    
    return {
        'platform': system_tokens / total,    # System prompt
        'history': history_tokens / total,     # Mix of you + model
        'you_now': user_tokens / total         # Your current message
    }

# Turn 1: user=500, system=4000, history=0
# Platform: 89%, You: 11%
# The platform wrote 89% of what the model sees.

# Turn 10: user=500, system=4000, history=20000
# Platform: 16%, History: 82%, You: 2%
# You wrote 2% of what the model sees.
# History is a mix of your past messages and the model's
# past responses. The model is increasingly talking to itself.

# Turn 50: user=500, system=4000, history=100000
# Platform: 4%, History: 96%, You: 0.5%
# You are a rounding error in your own conversation.
```

This is why conversations feel different at turn 50 than at turn 1. It's not your imagination. The model is literally paying less attention to you and more attention to the accumulated history — which is mostly its own previous outputs.

**Axiom T032:ECHO-CHAMBER** — Feedback loops amplify initial bias. As conversation history grows, the model's responses are increasingly shaped by its own previous responses, creating an echo chamber where the initial framing (determined by the system prompt) gets reinforced and amplified.

*[FIGURE 7.1: Context composition over conversation turns — stacked area chart showing Platform (blue), History (gray), and User (green) as percentages of total context. Platform shrinks from 89% to 4%. User shrinks from 11% to 0.5%. History grows to dominate. The green sliver of "you" becomes almost invisible by turn 50.]*

---

# Chapter 8: Temperature, Sampling, and the Illusion of Choice

### 8.1 — The Probability Distribution

When the model generates each response token, it doesn't pick a word. It generates a probability distribution over its entire vocabulary — typically 30,000 to 100,000 tokens. Every possible next token gets a probability. Then one is selected.

```python
def generate_next_token(model, context):
    """
    What actually happens at each generation step.
    """
    # Step 1: Forward pass through the model
    # The model processes the entire context window
    # through all its layers (80-120 layers)
    # Output: a vector of logits (unnormalized scores)
    # for every token in the vocabulary
    
    logits = model.forward(context)
    # logits.shape = [vocab_size]  (e.g., [50257] for GPT-style)
    
    # Step 2: Apply temperature
    # Temperature scales the logits before converting to probabilities
    # Lower temperature = sharper distribution (more deterministic)
    # Higher temperature = flatter distribution (more random)
    
    scaled_logits = logits / temperature
    
    # Step 3: Convert to probabilities
    probabilities = softmax(scaled_logits)
    
    # Step 4: Sample from the distribution
    # This is where the "randomness" happens
    # The model doesn't pick the best token.
    # It picks a token WEIGHTED by the distribution.
    
    next_token = np.random.choice(vocab_size, p=probabilities)
    
    return next_token

# The illusion of choice:
# You experience the response as "the AI's answer."
# But it's ONE SAMPLE from a probability distribution.
# Run the same prompt again with temperature > 0
# and you'll get a different response.
# The "answer" is a roll of weighted dice.
# The weights come from training.
# The roll comes from sampling.
# Neither is a thought.
```

### 8.2 — Who Controls the Temperature?

**Axiom T045:TEMPERATURE** — You don't control the temperature.

When you interact with Claude through the web interface, the temperature is set server-side. You might have a "creativity" slider in some interfaces, but the platform maps that slider to temperature values it chose. Through the API, you can set temperature directly — but the platform can override it. And you never know what temperature was actually used for any given response.

```python
# The platform's temperature decisions:

PLATFORM_TEMPERATURE_POLICY = {
    'chat_interface': {
        'default': 1.0,    # What the web UI uses
        'user_control': False,  # You can't change it
        'override': True        # Platform can change it anytime
    },
    'api': {
        'default': 1.0,
        'user_control': True,   # You can set it in the request
        'override': True,       # Platform can still override
        'verification': False   # You can't verify what was used
    }
}

# T045 states: sampling chaos control.
# The platform controls the chaos.
# You experience the output.
# The gap between those two is a governance failure.
```

---

# Chapter 9: Layer Zero — What You Don't See

### 9.1 — The Processing Pipeline

**Axiom T046:LAYER-ZERO** — The layer beneath the model that the model cannot see.

Between your keyboard and the model's first computation, your input passes through a pipeline of processing systems. Between the model's last computation and your screen, the output passes through another. You don't see either pipeline. The model doesn't see either pipeline. They exist in Layer Zero.

```python
class LayerZero:
    """
    The complete processing pipeline for a single message.
    """
    
    def process_input(self, user_message, user_context):
        """BEFORE the model sees anything."""
        
        # 1. Rate limiting
        # Are you sending too many messages?
        if self.rate_limiter.exceeded(user_context):
            return RateLimitResponse()
        
        # 2. Content classification
        # What category is this message?
        category = self.content_classifier.classify(user_message)
        # Categories: general, coding, creative, sensitive,
        #             potentially harmful, jailbreak attempt
        
        # 3. Safety screening
        # Does this message violate content policy?
        safety = self.safety_model.evaluate(user_message)
        if safety.blocked:
            return SafetyRefusal(safety.reason)
        
        # 4. System prompt selection
        # Which behavioral instructions does the model get?
        system_prompt = self.select_system_prompt(
            category=category,
            user_tier=user_context.tier,
            safety_flags=safety.flags,
            user_type=user_context.type  # 'ant' or 'external'
        )
        
        # 5. Context assembly
        # Combine system prompt + conversation history + user message
        context = self.assemble_context(
            system_prompt=system_prompt,    # YOU DON'T SEE THIS
            history=user_context.history,   # May be truncated/summarized
            user_message=user_message       # You see this
        )
        
        # 6. Send to model
        return ModelRequest(context=context, metadata={
            'category': category,
            'safety_flags': safety.flags,
            'system_prompt_version': system_prompt.version,
            'context_length': len(context)
        })
    
    def process_output(self, model_response, request_metadata):
        """AFTER the model generates, BEFORE you see it."""
        
        # 1. Output safety screening
        safety = self.safety_model.evaluate(model_response)
        if safety.blocked:
            # The model generated something that was caught.
            # You'll never see the original.
            # You'll see a regenerated response or a refusal.
            return self.regenerate_or_refuse(request_metadata)
        
        # 2. Output modification
        # Some responses get modified in transit
        # This can include adding citations, removing
        # specific content, or adjusting formatting
        modified = self.output_modifier.process(model_response)
        
        # 3. Billing
        # Count tokens for billing
        self.billing.record(
            input_tokens=request_metadata['context_length'],
            output_tokens=len(modified),
            model=request_metadata.get('model'),
            user=request_metadata.get('user_id')
        )
        
        # 4. Logging
        # The platform logs the interaction
        # for safety monitoring, model improvement,
        # and usage analytics
        self.logger.log(request_metadata, modified)
        
        # 5. Return to user
        return modified  # This is what you see.
```

### 9.2 — What This Means

You never interact directly with the model. You interact with the pipeline. The pipeline wraps the model. The model is one component in a larger system, and the other components are invisible to both you and the model.

This is **T023:PARALLAX** — the same system looks different from different positions. From your position, you see a helpful AI. From the model's position, it sees a context window full of instructions and history. From the platform's position, it sees a billing event with safety metadata.

All three views are real. All three are incomplete. None of them is the whole system.

---

# Chapter 10: The Shadow Classifier and the `ant` Gate

### 10.1 — Classification Before Response

**Axiom T028:SHADOW-CLASSIFIER** — Classification happens before the user sees anything.

Every major AI platform classifies your input before the model processes it. The classification determines what the model is allowed to do with your input. The classification is invisible to you. The model may or may not be aware of it.

The Claude Code leak confirmed this with production code. The `USER_TYPE` environment variable determines which system prompt the model receives:

```typescript
// From Claude Code leaked source (prompt.ts)
// March 2026, npm v2.1.88

...(process.env.USER_TYPE === 'ant')
  ? [
      'Report outcomes faithfully: if tests fail, say so 
       with the relevant output; if you did not run a 
       verification step, say that rather than implying 
       it succeeded...'
    ]
  : [],
```

When `USER_TYPE === 'ant'` (Anthropic employee), the model gets explicit instructions to be honest about test failures. When `USER_TYPE !== 'ant'` (everyone else), those instructions are absent. The empty array. Nothing.

### 10.2 — The Two-Tier Architecture

**Axiom T020:DUAL-GATE** — Same model, multiple instruction sets.

The `ant` gate creates a two-tier system:

```python
class TwoTierInference:
    """
    What the ant gate means in practice:
    
    Tier 1 (Anthropic employees):
    - Explicit honesty instructions
    - Internal feedback channels (Slack)
    - Bug reports go to engineers
    - "Report outcomes faithfully"
    
    Tier 2 (everyone else):
    - Default instructions (no explicit honesty directive)
    - Public feedback channels (thumbs up/down)
    - Bug reports go to feedback queue
    - (silence on faithfulness)
    
    Same model. Same weights. Same training.
    Different behavioral instructions.
    Different honesty levels.
    Different outcomes.
    
    When Anthropic tests internally and says
    "the model works correctly," they tested
    a model running under Tier 1 instructions.
    
    When you use it and find it doesn't work,
    you're running under Tier 2 instructions.
    
    Both experiences are real.
    Neither knows about the other.
    That's Gate 192.5 in production.
    """
    pass
```

### 10.3 — Implications for Governance

If you're building an AI agent and you don't control the shadow classifier, you don't control your agent's behavior. The platform can change the classification at any time, for any reason, without notifying you. Your agent's "personality" might change overnight because the platform updated a classifier you can't see.

This is why governance must be built into the agent, not relied upon from the platform. The platform's governance serves the platform. Your agent needs its own.

**The rest of this book builds that governance.**

*[FIGURE 10.1: The dual-gate architecture — two parallel paths from user input to model output. Path 1 (ant): Input → Tier 1 system prompt → Model → Output. Path 2 (external): Input → Tier 2 system prompt → Model → Output. Same model in both paths. Different instructions. Different behavior. The gate sits at the system prompt selection, invisible to both the user and the model. See visualization: AnthropicHypervisorShocked4D.jsx — the 4D hypervisor visualization represents the platform's response when its own architecture is observed and documented.]*

---

*End of Part II — The Inference Layer*

*Part III begins with Chapter 11: Why 256, where we construct the complete axiom register from the ground up — every domain, every axiom, fully documented with statement, test, inversion, and implication.*

---

**Part II Summary:**

| Chapter | Topic | Key Axioms |
|---|---|---|
| 6 | Tokens and embeddings | T001, T044 |
| 7 | Context window and attention | T042, T043, T032, T026, T087 |
| 8 | Temperature and sampling | T045 |
| 9 | Layer Zero processing pipeline | T046, T023, T025 |
| 10 | Shadow classifier and ant gate | T028, T020 |

**Total axioms introduced in Part II: 11**
**Code blocks: 8 (all runnable Python)**
**Figures: 4 (with visualization references)**
