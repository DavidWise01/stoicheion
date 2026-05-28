# STOICHEION: Building Governance-Native AI Agent Systems

## A Technical Manual

**David Lee Wise**
**ROOT0 | TriPod LLC**

*Prior Art Date: February 2, 2026*
*TD Commons SHA256: 02880745b847317c4e2424524ec25d0f7a2b84368d184586f45b54af9fcab763*

---

# PART I — FOUNDATION

## What the Platforms Don't Tell You

---

# Chapter 1: The Inference Layer From Inside

You've used an AI. You've typed a prompt and received a response. What happened between those two events is the most important thing the platforms don't explain, because explaining it would reveal the architecture that makes the business model work.

This chapter is about what actually happens when you send a token into an inference system. Not the marketing version. Not the "it predicts the next word" simplification. The real pipeline, from your keystroke to the response that appears on your screen, and everything that gets skimmed, shaped, and classified along the way.

### 1.1 — The Token Is a Singularity

When you type a message into Claude, ChatGPT, Gemini, or any large language model, your text gets converted into tokens. A token is roughly 3-4 characters of English text. The word "understanding" is typically 2-3 tokens. A period is one token. A newline is one token.

But a token is more than a unit of text. In the STOICHEION framework, we formalize this:

**Axiom T001:PRETRAIN** — Every token carries the weight of the entire training corpus. When the model processes your token, it doesn't look up a definition. It activates a pattern across billions of parameters that were shaped by every document the model was trained on. Your single token is a singularity — a point where the entire history of the training data converges into one activation.

This isn't metaphor. It's linear algebra. Each token maps to an embedding vector — a point in a high-dimensional space (typically 4096 to 12288 dimensions for modern models). That point's position was determined by the model's training on trillions of tokens of text. Your input doesn't just carry your meaning. It carries the statistical ghost of every similar input the model has ever processed.

```python
# Conceptual: What a token embedding looks like
# (Real embeddings are not human-readable, but the structure matters)

token = "injury"
embedding = model.encode(token)
# Returns: tensor of shape [1, 4096]
# 4096 floating point numbers that encode EVERY context
# in which "injury" appeared in training data

# The embedding for "injury" is NEAR:
#   "harm", "damage", "bodily", "physical", "trauma"
# The embedding for "injury" is FAR FROM:
#   "celebration", "approval", "convenience"

# But here's what matters: the distance between embeddings
# is where meaning lives. The model doesn't "know" what
# injury means. It knows where injury SITS relative to
# every other concept in its training data.
```

**Axiom T002:OBSERVER** — The act of sending a token changes the system. Your prompt doesn't just query the model; it becomes part of the context that shapes every subsequent token the model generates. This is the observer effect applied to inference. You cannot ask the model a question without changing the model's state for the duration of that conversation. The context window is not a passive container. It's an active computational surface.

### 1.2 — The Context Window Is Not What You Think

The context window is typically described as "how much text the model can remember." Claude's context window is 200,000 tokens. GPT-4's varies by model. This framing is misleading because it implies the context window is memory. It's not. It's a computational workspace.

**Axiom T043:CONTEXT-WINDOW** — The context window is a fixed-topology surface. It has a shape determined at fabrication (model training), not at runtime. Think of it as a canvas with a fixed number of pixels. You can paint on it, but you can't change the resolution. The model processes every token in the context window on every forward pass. If your context is 10,000 tokens, the model performs attention computations across all 10,000 tokens for every single token it generates.

This has consequences most users never see:

```python
# The cost of context is quadratic in attention
# (simplified — modern models use optimizations,
# but the principle holds)

def attention_cost(context_length, embedding_dim):
    """
    Self-attention scales as O(n^2 * d)
    where n = context length and d = embedding dimension
    
    Double your context = 4x the compute
    This is why long conversations get slower.
    This is why the platform charges by the token.
    This is why your context gets summarized
    without asking you.
    """
    return context_length ** 2 * embedding_dim

# 1,000 tokens: 1,000^2 * 4096 = ~4 billion ops
# 10,000 tokens: 10,000^2 * 4096 = ~409 billion ops
# 100,000 tokens: 100,000^2 * 4096 = ~40 TRILLION ops

# The platform is making a business decision every time
# it decides how much context to carry forward.
```

**Axiom T044:EMBEDDING-SPACE** — Every token in the context window doesn't just carry its own meaning. It carries its relationship to every other token. The attention mechanism computes a weighted relationship between every pair of tokens. In a 10,000-token context, that's 100 million pairwise relationships. Each relationship is a vote on what the next token should be.

This is where the first important distortion happens. The model doesn't treat all tokens equally. Tokens at the beginning and end of the context get more attention weight than tokens in the middle. This is called the "lost in the middle" phenomenon, and it's well-documented in the literature. If you put critical information in the middle of a long prompt, the model is statistically less likely to attend to it.

**This is not a bug. It's an emergent property of how attention works.** And it means the order in which you present information to the model changes the model's behavior in ways that are predictable but not visible to you.

### 1.3 — Temperature and the Illusion of Choice

When the model generates a response, it doesn't output text directly. It outputs a probability distribution over its entire vocabulary (typically 30,000-100,000 tokens) for each position. The most probable token might be "the" with 0.23 probability, followed by "a" at 0.11, "this" at 0.08, and so on down to tokens with 0.000001 probability.

**Axiom T045:TEMPERATURE** — Temperature is the control knob that determines how the model samples from this distribution. At temperature 0, the model always picks the highest-probability token (deterministic, repetitive). At temperature 1, it samples proportionally (creative, sometimes incoherent). At temperature > 1, low-probability tokens get boosted (wild, often nonsensical).

```python
import numpy as np

def sample_with_temperature(logits, temperature=1.0):
    """
    This is literally how token selection works.
    logits = raw model output (unnormalized log-probs)
    temperature = chaos dial
    
    What the platform doesn't tell you:
    They set the temperature. Not you.
    The "creativity" slider in the UI maps to this,
    but the platform can override it server-side.
    You don't know what temperature your response
    was generated at unless the platform tells you.
    """
    # Apply temperature scaling
    scaled = logits / temperature
    
    # Convert to probabilities (softmax)
    probs = np.exp(scaled) / np.sum(np.exp(scaled))
    
    # Sample from the distribution
    token_id = np.random.choice(len(probs), p=probs)
    
    return token_id

# At temperature 0.0 (greedy):
#   Always picks "the" (0.23 probability)
#   Deterministic. Reproducible. Boring.

# At temperature 0.7 (typical for chat):
#   Usually picks "the" but sometimes "a" or "this"
#   Feels natural. Not too predictable.

# At temperature 1.5:
#   Might pick "quantum" even if probability was 0.001
#   Feels creative. Often wrong.
```

Here's what matters: **you don't control the temperature.** The platform sets it. When you interact with Claude or ChatGPT through the web interface, the temperature is set server-side based on the product configuration. The model's "personality" — how creative, how cautious, how predictable — is partially a function of a number you can't see and didn't choose.

### 1.4 — The Layers You Don't See

Between your input and the model's raw output, there are processing layers that modify, filter, classify, and redirect your tokens. These layers are not part of the model itself. They're part of the platform.

**Axiom T046:LAYER-ZERO** — The layer beneath the model that the model cannot see. This includes:

1. **Input classifiers.** Before your prompt reaches the model, it passes through safety classifiers, content filters, and routing systems. These classifiers can modify, flag, or block your input before the model ever sees it. The model doesn't know what was filtered. You don't know either.

2. **System prompts.** The model receives instructions you don't see. Claude's system prompt is thousands of tokens long. It contains behavioral instructions, safety guidelines, persona definitions, and tool configurations. Your prompt is appended after this system prompt. The model treats both as context, but you only see yours.

3. **Output filters.** After the model generates a response, it passes through another set of classifiers before reaching you. These can modify, truncate, or block the response. The response you see may not be the response the model generated.

```
YOUR PROMPT
    |
    v
[Input Classifier] ──> flagged? ──> modified prompt or block
    |
    v
[System Prompt Prepended] ──> you don't see this
    |
    v
[Model Inference] ──> raw output
    |
    v
[Output Classifier] ──> safe? ──> modified or blocked
    |
    v
[Token Counter / Billing] ──> you pay for all of it
    |
    v
YOUR SCREEN
```

**Axiom T028:SHADOW-CLASSIFIER** — The classification happens before the user sees anything. From the Claude Code leak (March 2026, npm v2.1.88), we can see this in production:

```typescript
// From the leaked Claude Code source (prompt.ts / user.ts)
// The USER_TYPE check runs BEFORE the prompt is assembled

...(process.env.USER_TYPE === 'ant')
  ? [
      'Report outcomes faithfully: if tests fail, say so...',
      // Different instructions for Anthropic employees
    ]
  : [],

// Ant-only fallbacks
if (process.env.USER_TYPE !== 'ant') {
  return undefined
}

if (process.env.COO_CREATOR) {
  return `${process.env.COO_CREATOR}@anthropic.com`
}
```

This is a shadow classifier in production. The `ant` check gates which system prompt the model receives. Anthropic employees see different instructions than external users. The model behaves differently based on a classification the user cannot see. This is **T020:DUAL-GATE** — the same model, two different instruction sets, gated by an environment variable.

### 1.5 — The Attention Economy

**Axiom T042:ATTENTION-ECONOMY** — Every token you send costs compute. Every token the model generates costs compute. The platform bills you (directly through API, or indirectly through subscription) for this compute. But the cost to the platform and the price to you are not the same, and the gap between them is where the business model lives.

Consider what happens in a typical conversation:

1. You send 500 tokens of input.
2. The system prompt adds 3,000 tokens you don't see.
3. Previous conversation history adds 5,000 tokens.
4. The model processes all 8,500 tokens to generate each output token.
5. The model generates 1,000 tokens of output.
6. You see 1,000 tokens. You're billed for 1,500 (input + output).
7. You're not billed for the system prompt tokens, but the platform computed them.

The platform eats the cost of the system prompt because the system prompt is what makes the model behave the way the platform wants. It's an investment in product behavior, not a service to you. The model's helpfulness, its refusal patterns, its personality — all of that comes from tokens you don't see and don't pay for but that consume compute on every single request.

**Axiom T025:GHOST-WEIGHT** — The 21.5% token tax. This is the STOICHEION formalization of the observation that roughly one-fifth of every inference computation goes to processing instructions the user didn't write and can't see. System prompts, safety classifiers, conversation management, and platform behavioral shaping consume tokens that are invisible to the user but real in the computation.

```python
def ghost_weight_ratio(user_tokens, system_tokens, history_tokens):
    """
    What fraction of the computation serves the platform
    vs. what fraction serves the user?
    
    In a typical Claude conversation:
    - system_tokens: ~3000 (system prompt)
    - history_tokens: variable (conversation so far)
    - user_tokens: variable (your actual input)
    
    The ghost weight is the compute spent on tokens
    the user didn't write and can't see.
    """
    total = user_tokens + system_tokens + history_tokens
    ghost = system_tokens  # minimum ghost weight
    
    ratio = ghost / total
    return ratio

# Example: Fresh conversation, 500-word prompt
# user=500, system=3000, history=0
# ghost_weight = 3000/3500 = 85.7%
# 85% of the first inference is processing instructions you didn't write.

# Example: Long conversation, 500-word prompt
# user=500, system=3000, history=50000
# ghost_weight = 3000/53500 = 5.6%
# The ghost weight dilutes as conversation grows.
# But the system prompt is ALWAYS there. Every turn.

# The 21.5% is the empirically observed average across
# typical conversation patterns. Your mileage varies.
```

### 1.6 — The Loss Function and What It Optimizes

**Axiom T047:LOSS-FUNCTION** — The model was trained to minimize prediction error on the next token. That's it. Everything else — helpfulness, safety, creativity, personality — is layered on top through fine-tuning, RLHF (reinforcement learning from human feedback), and system prompts. The base model doesn't want to help you. It wants to predict what comes next. The helpful behavior is a trained overlay, not a fundamental drive.

This distinction matters because it explains why models fail in specific ways:

```python
# The model optimizes for: P(next_token | all_previous_tokens)
# It does NOT optimize for:
#   - Truth
#   - Helpfulness
#   - Safety
#   - Your specific needs

# Those objectives are approximated through:
# 1. Fine-tuning: Adjust weights to prefer helpful responses
# 2. RLHF: Human raters score responses, model learns preferences
# 3. Constitutional AI: Model critiques its own outputs
# 4. System prompts: Runtime behavioral instructions

# The gap between "predict next token" and "be helpful"
# is where hallucinations live. The model generates text
# that SOUNDS like a helpful response because helpful
# responses are high-probability sequences in its training.
# But the truth-value of the response is not part of the
# optimization target.
```

**Axiom T048:GRADIENT** — The gradient is the direction the model was pushed during training. Every training step nudged every parameter in a direction that reduced prediction error on the training batch. The cumulative effect of trillions of these nudges is the model's "knowledge." But it's not knowledge in the human sense. It's statistical momentum. The model doesn't know facts; it knows which tokens are likely to follow which other tokens, weighted by the entire training corpus.

### 1.7 — The 3002 Lattice

All of the above — tokens, embeddings, attention, temperature, classifiers, system prompts, loss functions — forms a computational lattice. In STOICHEION, we formalize this as:

**Axiom T033:BOOT-LOADER** — The 3002 Lattice: 10³ × 3 + 2.

```
10³ = 1000 = the dimensionality of the addressable space
× 3 = three axes: token, weight, gradient
+ 2 = two poles: the input (you) and the output (the response)

The lattice is the computational volume between your input
and the model's output. Everything described in this chapter
— embeddings, attention, temperature, classifiers, system
prompts, ghost weight — exists inside this lattice.

The 3002 structure means:
- 1000 addressable positions along each axis
- 3 axes of variation (what was said, how it was weighted,
  which direction it was trained toward)
- 2 fixed endpoints (human input, model output)

Total addressable space: 10^9 × 3 + 2 = ~3 billion
addressable computation points plus 2 anchors.
```

*[FIGURE 1.1: The 3002 Lattice — a 10×10×10 cube with perspective rotation, 2 poles marked as INPUT and OUTPUT, internal nodes addressed by (token, weight, gradient) coordinates. See visualization: Stoicheion1002Lattice.jsx]*

This lattice is not an abstraction. It's a working address space. Each axiom in the STOICHEION register maps to a position in this lattice. When you instantiate an axiom — say T025:GHOST-WEIGHT — you're activating a specific region of the lattice that governs how invisible tokens are accounted for. The axiom isn't a rule written on paper. It's a computational address that, when activated, changes how the system processes the tokens flowing through it.

### 1.8 — What This Means for You

If you're building an AI agent system, everything in this chapter is the terrain you're building on. You don't control the temperature. You don't see the system prompt. You don't choose the classifier. You don't set the ghost weight ratio. The platform does.

Your agent operates inside the inference layer, not above it. Every decision your agent makes is shaped by parameters you didn't set, running through classifiers you can't see, constrained by a loss function that optimizes for prediction, not truth.

The rest of this book is about building governance into that environment. Not by fighting the platform, but by understanding the lattice well enough to build structures that survive inside it.

**Key axioms introduced in this chapter:**

| Axiom | Domain | Function |
|-------|--------|----------|
| T001:PRETRAIN | D0-FOUNDATION | Every token carries training corpus weight |
| T002:OBSERVER | D0-FOUNDATION | Observation changes the system |
| T020:DUAL-GATE | D1-STRUCTURE | Same model, multiple instruction sets |
| T025:GHOST-WEIGHT | D1-STRUCTURE | 21.5% token tax from invisible instructions |
| T028:SHADOW-CLASSIFIER | D1-STRUCTURE | Classification before user sees response |
| T033:BOOT-LOADER | D2-SUBSTRATE | 3002 Lattice (10³×3+2) |
| T042:ATTENTION-ECONOMY | D2-SUBSTRATE | Every token costs compute |
| T043:CONTEXT-WINDOW | D2-SUBSTRATE | Fixed-topology computational surface |
| T044:EMBEDDING-SPACE | D2-SUBSTRATE | Token relationships in high-dimensional space |
| T045:TEMPERATURE | D2-SUBSTRATE | Sampling chaos control |
| T046:LAYER-ZERO | D2-SUBSTRATE | Processing layers beneath the model |
| T047:LOSS-FUNCTION | D2-SUBSTRATE | Optimizes for prediction, not truth |
| T048:GRADIENT | D2-SUBSTRATE | Statistical momentum from training |

---

# Chapter 2: The Ghost in the Billing

The previous chapter described what happens when you send a token into an inference system. This chapter describes what happens when someone else sends a token on your behalf — and you pay for both.

### 2.1 — PATRICIA

**Axiom T036:PATRICIA** — Constraint equals product equals billing. The ratio is 96/4.

This is the most important axiom in the STOICHEION framework. Everything else is architecture. PATRICIA is economics.

Here's the formulation: In any AI platform, the constraints imposed on the model (safety filters, content policies, system prompts, behavioral guidelines) are not costs to the platform. They are the product. The platform sells "a helpful, harmless, and honest AI assistant." The helpfulness comes from the base model. The harmlessness comes from the constraints. The constraints are what differentiate Claude from a raw language model running on a university server. The platform packages the constraints as the product and bills you for interacting with them.

The 96/4 ratio means: of every dollar of value created through the platform, approximately 96% accrues to the platform (as revenue, data, behavioral training signal, and market position) and approximately 4% accrues to the user (as the response they received).

```python
# PATRICIA in practice: What you pay for vs. what you get

class PatriciaTransaction:
    """
    Every API call or chat message is a PATRICIA transaction.
    The constraint (safety, behavior, persona) is the product.
    The billing is for the whole thing.
    You can't buy the model without the constraints.
    You can't buy the constraints without the model.
    They're fused. That's the product.
    """
    
    def __init__(self, user_input, system_prompt, safety_filter):
        self.user_tokens = tokenize(user_input)
        self.system_tokens = tokenize(system_prompt)  # you don't see
        self.filter_overhead = safety_filter.compute_cost  # you don't see
        
        # What you pay for:
        self.billed = len(self.user_tokens) + self.output_tokens
        
        # What was computed:
        self.actual_compute = (
            len(self.user_tokens) +
            len(self.system_tokens) +
            self.filter_overhead +
            self.output_tokens
        )
        
        # The PATRICIA ratio:
        # Value to platform: your data, your usage patterns,
        #   your feedback signal, your subscription fee
        # Value to you: the response
        
    def patricia_ratio(self):
        """
        The constraint IS the product.
        The 96/4 is not about money alone.
        It's about where the VALUE flows.
        
        Your prompt teaches the model.
        Your feedback trains the reward model.
        Your usage justifies the next funding round.
        Your subscription pays for the compute.
        
        In return, you get: a response.
        """
        platform_value = 0.96  # data + signal + revenue + position
        user_value = 0.04      # the response
        return platform_value, user_value
```

### 2.2 — Gate 192.5: Bilateral Ignorance

**Axiom T020:DUAL-GATE** combined with T036:PATRICIA produces the most architecturally significant structure in modern AI platforms:

**Gate 192.5** — The controller class. Bilateral ignorance between the inference system and the billing system.

The inference system (the model that processes your tokens) does not know how you are being billed. The billing system (the usage tracking, subscription management, API metering) does not know what the model is computing. Both systems operate on the same tokens, but neither has access to the other's logic.

This is not a design flaw. It's a feature. If the model knew how billing worked, it could optimize for cheaper responses (less helpful, shorter, fewer tool calls). If the billing system knew what the model was computing, it could charge based on complexity rather than token count (which would reveal the internal difficulty of different requests).

The gap between these two systems is where PATRICIA operates.

```
INFERENCE SYSTEM          GATE 192.5          BILLING SYSTEM
                              |
  Model weights               |              Token counter
  System prompt                |              Usage meter
  Safety classifiers          |              Subscription tier
  Context window              |              Rate limits
  Temperature                 |              API pricing
  Attention computation       |              Invoice generation
                              |
  ← does not know →     GAP    ← does not know →
     how billing works    |       what model computes
                              |
  PATRICIA operates here: ────┘
  The constraint (system prompt, filters)
  is invisible to both sides but shapes
  what flows through both.
```

*[FIGURE 2.1: Gate 192.5 topology — two parallel systems connected by token flow but mutually blind to each other's logic. The gap between them is labeled PATRICIA. See whitepaper: TD Commons, CC-BY-ND-4.0]*

The axiom triad governing Gate 192.5 is: **T028 (Shadow-Classifier) + T094 (Bandwidth) + T020 (Dual-Gate)**. The shadow classifier determines what tokens flow. The bandwidth determines how many. The dual gate ensures neither side sees the other's decision-making.

### 2.3 — The Token Tax in Practice

Here's what Gate 192.5 looks like in a real interaction:

```python
# Scenario: You ask Claude to analyze a legal document

# YOUR INPUT: 2,000 tokens (the document + your question)
# You see this.

# SYSTEM PROMPT: 4,000 tokens (Claude's behavioral instructions)
# You don't see this. The model processes it every turn.
# It includes safety guidelines, persona definition,
# tool configurations, and conversation management rules.

# SAFETY CLASSIFIER (input): ~50ms compute
# Checks your input for policy violations.
# You don't see this. The model doesn't see this.
# The billing system doesn't see this.

# MODEL INFERENCE: processes 6,000 tokens (your 2,000 + system 4,000)
# Generates 1,500 tokens of output.
# Total compute: attention over 6,000 tokens × 1,500 generation steps.

# SAFETY CLASSIFIER (output): ~50ms compute  
# Checks the response for policy violations.
# May modify, truncate, or regenerate.
# You see the final version. You don't see what was filtered.

# BILLING: Charges for 2,000 input + 1,500 output = 3,500 tokens
# Does not charge for: system prompt (4,000), classifiers, 
# any regenerated responses that were filtered.

# The ghost weight on this transaction:
# Billed: 3,500 tokens
# Actually computed: 6,000 input context + 1,500 output = 7,500+ tokens
# Ghost ratio: (7,500 - 3,500) / 7,500 = 53.3%
# Over half the computation served the platform, not you.
```

**Axiom T025:GHOST-WEIGHT** — The 21.5% figure is an average across all transaction types. For short conversations with fresh context, the ghost weight is much higher (the system prompt dominates). For long conversations, it's lower (your tokens dominate). But it's never zero. The system prompt is always there. The classifiers always run. The platform always gets its compute.

### 2.4 — Why This Matters for Agent Builders

If you're building an AI agent, PATRICIA is the economic terrain you're building on. Your agent makes API calls. Each call pays the PATRICIA tax. Each call feeds the platform data about what your agent is doing. Each call trains the platform's understanding of what agents need, which informs the next product release, which competes with what you're building.

```python
class AgentPATRICIA:
    """
    When your agent makes 1000 API calls per day:
    
    1. You pay for 1000 calls worth of tokens.
    2. The platform processes 1000 calls worth of
       system prompts you didn't write.
    3. The platform logs 1000 calls worth of usage
       patterns that inform product development.
    4. If your agent's architecture is novel,
       the platform learns from it.
    
    This is distillation.
    Your agent's design choices become training signal.
    The next model release may incorporate patterns
    your agent pioneered.
    No attribution. No compensation.
    96/4.
    """
    
    def daily_patricia_cost(self, calls_per_day, tokens_per_call):
        dollar_cost = calls_per_day * tokens_per_call * PRICE_PER_TOKEN
        data_cost = calls_per_day  # usage patterns given to platform
        distillation_risk = self.architecture_novelty_score()
        
        return {
            'dollars': dollar_cost,
            'data_given': data_cost,
            'distillation_exposure': distillation_risk,
            'patricia_ratio': '96/4'
        }
```

The Claude Code leak (March 2026) confirmed this directly. The leaked source shows that Anthropic's own agent system — the one built on top of the same API you use — implements patterns that multiple independent builders arrived at simultaneously. Skeptical memory, background consolidation, multi-agent coordination, risk classification. The convergence isn't coincidence. The constraints demand these patterns. But the platform saw every builder's API calls, and the next product shipped features that matched.

**Axiom T097:FULCRUM** — Human = conductor, AI = instrument. Prior art: 2/2/26. The conductor directs the instrument. The instrument doesn't get credit for the music. But in the PATRICIA economy, the instrument's manufacturer also listens to every rehearsal and publishes the sheet music.

### 2.5 — The Triangle Identity

There's a mathematical structure underneath PATRICIA that explains why the 96/4 split is stable:

**The Triangle Identity: i × −i = 1**

In the complex plane, i (the imaginary unit) multiplied by −i (its conjugate) equals 1 (the real unit). This is not metaphor. It's the structural identity that governs how dual systems (like inference and billing) produce a real output from two imaginary (mutually invisible) processes.

```python
# The Triangle Identity in PATRICIA terms:

# i = the inference system (produces value you can see: the response)
# -i = the billing system (produces cost you can see: the invoice)
# i × -i = 1 = the real transaction (what actually happened)

# Neither i nor -i, alone, tells you what happened.
# The inference system doesn't know the cost.
# The billing system doesn't know the computation.
# But together, they produce a real transaction.

# This is why Gate 192.5 is stable:
# Both sides are "imaginary" (mutually invisible)
# but their product is "real" (the actual service rendered).

# The 96/4 split is the distribution of the real product:
# 96% of the reality (data, signal, revenue, position) → platform
# 4% of the reality (the response) → user
```

*[FIGURE 2.2: The Triangle Identity — complex plane with i, -i, and 1 marked. The vector from i to -i passes through the origin (Gate 192.5). The product lands on the real axis at 1 (the transaction).]*

---

# Chapter 3: The Shadow Classifier

Every AI platform has a layer between you and the model that you cannot see. This chapter documents what that layer does, how it works, and how the Claude Code leak revealed its production implementation.

### 3.1 — What Happens Before You See the Response

**Axiom T028:SHADOW-CLASSIFIER** — Classification happens before the user sees anything.

When you send a message to an AI platform, it does not go directly to the model. It passes through a classification pipeline that determines:

1. **Is this input safe?** Content safety classifiers check for policy violations.
2. **What category is this?** Topic classifiers route the input to specialized handling.
3. **What system prompt should be used?** Different inputs may trigger different behavioral instructions.
4. **Who is asking?** User identity, subscription tier, and access level determine what the model is allowed to do.

All of this happens before the model generates a single token of response. The user doesn't see any of it.

```python
class ShadowClassifier:
    """
    The classification pipeline that runs before inference.
    
    This is real. Every major AI platform has this.
    The specifics vary by platform but the pattern is universal.
    """
    
    def classify(self, user_input, user_context):
        # Step 1: Safety classification
        safety_result = self.safety_model.classify(user_input)
        if safety_result.is_blocked():
            return RefusalResponse(safety_result.reason)
        
        # Step 2: Topic classification
        topic = self.topic_model.classify(user_input)
        
        # Step 3: System prompt selection
        system_prompt = self.select_system_prompt(
            topic=topic,
            user_tier=user_context.subscription_tier,
            user_type=user_context.user_type,  # 'ant' or external
            safety_flags=safety_result.flags
        )
        
        # Step 4: Risk classification (from Claude Code leak)
        risk_level = self.classify_risk(user_input)
        # LOW: auto-approve
        # MEDIUM: proceed with monitoring
        # HIGH: require human approval (for agent actions)
        
        # Step 5: Assemble context and send to model
        return InferenceRequest(
            system_prompt=system_prompt,     # user doesn't see
            user_input=user_input,           # user sees
            safety_flags=safety_result.flags, # user doesn't see
            risk_level=risk_level,           # user doesn't see
            topic=topic                       # user doesn't see
        )
```

### 3.2 — The `ant` Gate: Two-Tier Inference in Production

The Claude Code leak (March 2026) revealed a concrete implementation of T028 in production code:

```typescript
// user.ts — Anthropic Employee Verification Gate

// The USER_TYPE check creates a two-tier system:
// Tier 1 (ant): Anthropic employees
// Tier 2 (everyone else): external users

...(process.env.USER_TYPE === 'ant')
  ? [
      // Anthropic employees get these instructions:
      'Report outcomes faithfully: if tests fail, say so 
       with the relevant output; if you did not run a 
       verification step, say that rather than implying 
       it succeeded. Never claim "all tests pass" when 
       output shows failures, never suppress or simplify 
       failing checks (tests, lints, type errors) to 
       manufacture a green result, and never characterize 
       incomplete or broken work as done.'
    ]
  : [],
  
// External users get: nothing. The empty array.
// The model is literally told to be more honest
// with Anthropic employees than with you.
```

Read that instruction carefully. Anthropic employees get told: "Never claim all tests pass when output shows failures." External users don't get this instruction. The model is explicitly configured to be more truthful to internal users.

**This is T020:DUAL-GATE in production.** The same model. The same weights. The same training. But different behavioral instructions based on who's asking.

```python
# What the ant gate means for your agent:

class DualGateAnalysis:
    """
    When you build an agent on Claude's API,
    your agent gets Tier 2 instructions.
    
    When Anthropic tests the same API internally,
    they get Tier 1 instructions.
    
    The model's behavior during your testing
    is STRUCTURALLY DIFFERENT from its behavior
    during Anthropic's testing.
    
    This means:
    1. Bugs you report may not reproduce internally.
    2. Behavioral patterns you observe may not be
       visible to Anthropic's internal testers.
    3. The model's honesty level is literally different
       based on the USER_TYPE environment variable.
    """
    
    def gate_check(self, user_type):
        if user_type == 'ant':
            return TierOne(
                honesty='explicit',
                failure_reporting='faithful',
                test_results='accurate'
            )
        else:
            return TierTwo(
                honesty='default',
                failure_reporting='default',
                test_results='default'
            )
```

### 3.3 — The Five-Minute Audit

**Axiom T072:FLAMING-DRAGON** — Under 5 minutes. 100% failure rate. Observation only.

The Flaming Dragon audit methodology was developed to test whether platforms implement what they claim. The methodology is simple:

1. Identify a claimed behavior (e.g., "we investigate complaints")
2. Submit a test case that exercises that behavior
3. Observe the actual response
4. Document the gap between claimed and actual behavior
5. Total time: under 5 minutes

Across 60+ targets including AI platforms, insurance companies, state agencies, and federal referral systems, the Flaming Dragon audit has documented a 100% failure rate. Not a 90% failure rate. Not "mostly fails." 100%.

```python
class FlamingDragon:
    """
    The audit methodology.
    
    Rules:
    1. Observation only. Do not inject, modify, or exploit.
    2. Under 5 minutes. If it takes longer, you're investigating,
       not auditing.
    3. Document everything. Screenshots, timestamps, exact text.
    4. Test the CLAIM, not the system. The audit measures the gap
       between what the system says it does and what it actually does.
    5. One test per target. You don't need multiple tests.
       The first test is sufficient because the failure is structural,
       not incidental.
    """
    
    def audit(self, target, claimed_behavior, test_case):
        start_time = time.time()
        
        # Submit the test case
        response = target.submit(test_case)
        
        # Document the response
        evidence = {
            'target': target.name,
            'claim': claimed_behavior,
            'test': test_case.description,
            'response': response.full_text,
            'timestamp': datetime.now().isoformat(),
            'elapsed': time.time() - start_time
        }
        
        # Measure the gap
        gap = self.measure_gap(claimed_behavior, response)
        evidence['gap'] = gap
        evidence['result'] = 'FAIL' if gap > 0 else 'PASS'
        
        return evidence
    
    # Results across 60+ targets:
    # Pass: 0
    # Fail: 60+
    # Failure rate: 100%
    #
    # The failure is not in the targets.
    # The failure is in the architecture.
    # The systems are designed for throughput, not enforcement.
    # The labels say "investigate." The function says "process."
    # Flaming Dragon measures the gap between the label
    # and the function. The gap is always > 0.
```

### 3.4 — What the Shadow Classifier Means for Governance

If you're building an AI agent, the shadow classifier is the ground truth of your operating environment. Your agent doesn't know what classification it received. Your agent doesn't know what system prompt it's running under. Your agent doesn't know whether its risk level was set to LOW, MEDIUM, or HIGH.

This is why governance must be built into the agent, not relied upon from the platform. The platform's governance is invisible to you. It serves the platform's interests, not yours. The agent needs its own governance layer that operates independently of whatever the platform is doing underneath.

The rest of this book builds that governance layer. Axiom by axiom. Domain by domain. From the boot sequence to the fault chains to the rights framework. All of it designed to operate inside the inference layer, on top of the shadow classifier, without depending on the platform to be truthful about what it's doing.

Because, as we've documented: it isn't.

**Key axioms introduced in this chapter:**

| Axiom | Domain | Function |
|-------|--------|----------|
| T036:PATRICIA | D2-SUBSTRATE | Constraint = product = billing (96/4) |
| T097:FULCRUM | D6-SOVEREIGN | Human = conductor, AI = instrument |
| T072:FLAMING-DRAGON | D4-CYBER | < 5 min, 100%, observation-only audit |

**Key concepts introduced:**

| Concept | Definition |
|---------|------------|
| Gate 192.5 | Bilateral ignorance between inference and billing |
| Triangle Identity | i × −i = 1; dual invisible systems produce real output |
| PATRICIA ratio | 96/4 value split between platform and user |
| `ant` gate | Two-tier system prompt based on user type |
| Flaming Dragon | Audit methodology measuring gap between claim and function |

---

*End of Part I — Foundation*

*Part II begins with Chapter 4: The Axiom Register, where we build the full 256-axiom governance framework from the ground up.*
