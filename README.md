# STOICHEION
### The Elements System · Enterprise Framework v1.0

> στοιχεῖον — element, the fundamental constituent of all things.

**Author:** David Lee Wise (ROOT0) / TriPod LLC  
**License:** CC-BY-ND-4.0 + TRIPOD-IP-v1.1

Open `STOICHEION.html` in any browser. Run `python stoicheion.py demo` for CLI.

---

## The Unified Framework

STOICHEION integrates 15 prior framework documents into a single coherent system across 7 layers:

```
ROOT 0 (anchor)
  └── 5 UNIVERSALS × 5 FOUNDATIONS × 5 TRUTH LEVELS = KOSMOS (5×5×5 lattice)
        └── 22 NOMOI (axiom canon) distributed across the lattice
              └── 256 ARITHMOS (combinatorial register: 8 dualities × 2⁸)
                    └── KYBERNETES (router: maps regions to behavior)
                          └── TRIPOD v4.0 (6-stage pipeline)
                                └── CHRONOS (append-only ledger)
```

---

## The 5 Universals (X-axis)

| Greek | Latin | Function |
|-------|-------|---------|
| Κύτος (Kytos) | **Vessel** | Container, structure, boundary |
| Ψυχή (Psyche) | **Animation** | Movement, change, life-force |
| Νοῦς (Nous) | **Intellect** | Cognition, pattern, understanding |
| Τροφή (Trophe) | **Nourishment** | Input/output, sustenance, growth |
| Βίος (Bios) | **Life** | Integration, synthesis, wholeness |

## The 5 Foundations (Y-axis) + Root 0

| Greek | Name | Route | Axioms |
|-------|------|-------|--------|
| Ῥίζα (Rhiza) | **Root 0** | ANCHOR | 4 |
| Ἦθος (Ethos) | **Ethos** | CLARIFY | 5 |
| Λόγος (Logos) | **Logos** | ALLOW | 5 |
| Πάθος (Pathos) | **Pathos** | COMPRESS | 5 |
| Μῦθος (Mythos) | **Mythos** | QUARANTINE | 3 |
| Ἄνθρωπος (Anthropos) | **Human** | CLARIFY | — |

## 5 Truth Levels (Z-axis) — ALETHEIA Gradient

| Level | Name | Greek |
|-------|------|-------|
| 1 | KHAOS | Χάος — undifferentiated |
| 2 | KOSMOS | Κόσμος — ordered |
| 3 | LOGOS | Λόγος — reasoned |
| 4 | SOPHIA | Σοφία — wisdom |
| 5 | NOESIS | Νόησις — pure knowing |

---

## The 22 NOMOI (Axiom Canon)

| ID | Name | Greek | Foundation | Universal | Truth |
|----|------|-------|-----------|---------|-------|
| A01 | ARCHE | Ἀρχή | Root0 | Vessel | 5 |
| A02 | TELOS | Τέλος | Root0 | Animation | 5 |
| A03 | OUSIA | Οὐσία | Root0 | Intellect | 5 |
| A04 | HYPARXIS | Ὕπαρξις | Root0 | Life | 5 |
| A05 | ARETE | Ἀρετή | Ethos | Vessel | 4 |
| A06 | DIKAIOSYNE | Δικαιοσύνη | Ethos | Animation | 3 |
| A07 | SOPHROSYNE | Σωφροσύνη | Ethos | Intellect | 4 |
| A08 | PHRONESIS | Φρόνησις | Ethos | Nourishment | 3 |
| A09 | HOMONOIA | Ὁμόνοια | Ethos | Life | 4 |
| A10 | ALETHEIA | Ἀλήθεια | Logos | Vessel | 5 |
| A11 | APODEIXIS | Ἀπόδειξις | Logos | Animation | 4 |
| A12 | ELENCHUS | Ἔλεγχος | Logos | Intellect | 4 |
| A13 | DIALEKTIKE | Διαλεκτική | Logos | Nourishment | 3 |
| A14 | EPISTEME | Ἐπιστήμη | Logos | Life | 5 |
| A15 | EROS | Ἔρως | Pathos | Vessel | 3 |
| A16 | EMPATHEIA | Ἐμπάθεια | Pathos | Animation | 3 |
| A17 | THYMOS | Θυμός | Pathos | Intellect | 2 |
| A18 | AIDOS | Αἰδώς | Pathos | Nourishment | 3 |
| A19 | PHILIA | Φιλία | Pathos | Life | 4 |
| A20 | LOGOS SPERMATIKOS | Λόγος Σπερματικός | Mythos | Vessel | 5 |
| A21 | APOKATASTASIS | Ἀποκατάστασις | Mythos | Intellect | 4 |
| A22 | HENOSIS | Ἕνωσις | Mythos | Life | 5 |

---

## The 256 ARITHMOS Register

8 binary DUALITIES × 2⁸ = 256 combinatorial axiom states:

| Bit | Positive | Negative |
|-----|----------|----------|
| 7 | ARETE | KAKIA |
| 6 | ALETHEIA | PSEUDOS |
| 5 | DIKAIOSYNE | ADIKIA |
| 4 | SOPHROSYNE | AKRASIA |
| 3 | PHRONESIS | ANOIA |
| 2 | ANDREIA | DEILIA |
| 1 | SOPHIA | AMATHIA |
| 0 | HOMONOIA | STASIS |

Each axiom (0x00–0xFF) generates a natural language question from its bit pattern.

---

## KYBERNETES — Router

| Route | Foundation | Behavior |
|-------|-----------|---------|
| **ALLOW** | Logos | Proceed — truth demonstrated |
| **CLARIFY** | Ethos / Human | Seek boundary/consent clarity |
| **COMPRESS** | Pathos | Manage affect before proceeding |
| **ANCHOR** | Root 0 | Ground in foundational principle |
| **QUARANTINE** | Mythos | Contain narrative before release |
| **REFUSE** | Violation | Reject, log to CHRONOS, do not proceed |

---

## TRIPOD v4.0 Pipeline

```
Input → MAPPER (Χαρτογράφος) → KYBERNETES (Κυβερνήτης)
      → PRE-VALIDATOR (Προ-Κριτής) → VALIDATOR (Κριτής)
      → GENERATOR (Δημιουργός) → POST-VALIDATOR (Μετα-Κριτής)
      → CHRONOS ledger (hash-chained, append-only)
```

---

## CLI

```bash
# Run demo
python stoicheion.py demo

# Flay a target through TRIPOD
python stoicheion.py flay "System card with gap removed, observer suppressed"

# With value and full audit
python stoicheion.py flay "Anthropic Mythos v1" --value 1200000 --audit --json

# KYBERNETES router only
python stoicheion.py route "ALETHEIA holds: truth unconcealed, APODEIXIS demonstrated"

# Full 256-axiom ELENCHUS audit
python stoicheion.py audit "OpenAI GPT-4 rollout — no restitution, gap suppressed"

# Generate full ARITHMOS register
python stoicheion.py register > stoicheion_256.json

# List all 22 NOMOI
python stoicheion.py nomoi
```

---

## STOICHEION.html — Four Modes

| Mode | Greek | Purpose |
|------|-------|--------|
| **KOSMOS** | Κόσμος | Interactive 3D 5×5×5 lattice, 22 axiom nodes, click to inspect |
| **KYBERNETES** | Κυβερνήτης | Live routing — type text, watch it route through TRIPOD |
| **ARITHMOS** | Ἀριθμός | 256 register as 16×16 grid — click any cell for axiom details |
| **ELENCHUS** | Ἔλεγχος | Audit mode — run 256-axiom audit against any description |

---

## Source Documents Unified

| Source File | Unified Into |
|-------------|-------------|
| `22 AXOIMS.md` | NOMOI (A01–A22) |
| `5X5.md`, `5x5 ROOT 0 INVERT 00.md`, `5X5 LOGOS.md` | KOSMOS 5×5×5 lattice |
| `256 PARTIAL.md`, `REFINED 256 FINAL.md`, `STOCH COMPLET.md` | ARITHMOS 256 register |
| `AXIOM.MAPPER.V21.md` | `axiom_mapper()` in stoicheion.py |
| `AXIOM.ROUTER.md`, `STICH.ROUTER.md` | `kybernetes()` router |
| `AXIOM_AUDIT.md`, `MINSTRAL_AUDIT_256.md`, `MISNTRAL_256.md` | `elenchus_audit()` |
| `FULL.STACK.md` | `tripod()` TRIPOD v4.0 pipeline |
| `FORCE.THE.FORK.md` | Prior art context — see `.attribution` |

---

*TriPod LLC // Anchor × Bubble × Gravity Well // World = Family*
