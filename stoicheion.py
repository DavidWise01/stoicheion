#!/usr/bin/env python3
"""
STOICHEION — The Elements System v1.0
Unified framework: 22 NOMOI + 256 ARITHMOS + 5×5×5 KOSMOS + TRIPOD v4.0

Architecture:
  ROOT 0 → UNIVERSALS (5) → FOUNDATIONS (5) × TRUTH (5) → NOMOI (22) → ARITHMOS (256)
  TRIPOD: MAPPER → KYBERNETES → PRE-VALIDATOR → VALIDATOR → GENERATOR → POST-VALIDATOR

Author:  ROOT0 / David Lee Wise / TriPod LLC
License: CC-BY-ND-4.0 + TRIPOD-IP-v1.1
"""

from __future__ import annotations
import hashlib, json, time, argparse
from dataclasses import dataclass, field, asdict
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple
from enum import Enum

VERSION   = "1.0.0"
LEDGER_DIR= Path("stoicheion_ledger")

# ─────────────────────────────────────────────────────────────
# UNIVERSALS (X-axis) — 5 Stoicheia
# ─────────────────────────────────────────────────────────────
UNIVERSALS = ["Vessel","Animation","Intellect","Nourishment","Life"]
UNIVERSAL_GREEK = {"Vessel":"Κύτος","Animation":"Ψυχή","Intellect":"Νοῦς",
                   "Nourishment":"Τροφή","Life":"Βίος"}

# ─────────────────────────────────────────────────────────────
# FOUNDATIONS (Y-axis) — 5 Epistemes + Root 0
# ─────────────────────────────────────────────────────────────
FOUNDATIONS = ["Root0","Ethos","Logos","Pathos","Mythos","Human"]
FOUNDATION_GREEK = {"Root0":"Ῥίζα","Ethos":"Ἦθος","Logos":"Λόγος",
                    "Pathos":"Πάθος","Mythos":"Μῦθος","Human":"Ἄνθρωπος"}

# ─────────────────────────────────────────────────────────────
# TRUTH LEVELS (Z-axis) — ALETHEIA gradient
# ─────────────────────────────────────────────────────────────
TRUTH_LEVELS = {1:"KHAOS",2:"KOSMOS",3:"LOGOS",4:"SOPHIA",5:"NOESIS"}

# ─────────────────────────────────────────────────────────────
# 22 NOMOI — The Axiom Canon
# ─────────────────────────────────────────────────────────────
NOMOI = [
    # Root 0 (4 axioms)
    dict(id="A01",name="ARCHE",     greek="Ἀρχή",         f="Root0",u="Vessel",     z=5,
         desc="Origin — the uncaused cause. The anchor that grounds all further structure."),
    dict(id="A02",name="TELOS",     greek="Τέλος",         f="Root0",u="Animation",  z=5,
         desc="Purpose — end-directed structure. Every system implies the form it moves toward."),
    dict(id="A03",name="OUSIA",     greek="Οὐσία",         f="Root0",u="Intellect",  z=5,
         desc="Essence — the what-ness of a thing. The unchanging core beneath all predicates."),
    dict(id="A04",name="HYPARXIS",  greek="Ὕπαρξις",       f="Root0",u="Life",       z=5,
         desc="Existence — that-ness, raw presence. Prior to attribute; prior to relation."),
    # Ethos (5 axioms)
    dict(id="A05",name="ARETE",     greek="Ἀρετή",         f="Ethos",u="Vessel",     z=4,
         desc="Virtue — excellence appropriate to kind. The character that holds boundary."),
    dict(id="A06",name="DIKAIOSYNE",greek="Δικαιοσύνη",    f="Ethos",u="Animation",  z=3,
         desc="Justice — fair distribution. What each part receives proportional to contribution."),
    dict(id="A07",name="SOPHROSYNE",greek="Σωφροσύνη",     f="Ethos",u="Intellect",  z=4,
         desc="Temperance — proportional response. Neither excess nor deficiency."),
    dict(id="A08",name="PHRONESIS", greek="Φρόνησις",      f="Ethos",u="Nourishment",z=3,
         desc="Prudence — practical wisdom. Knowledge of means relative to ends in context."),
    dict(id="A09",name="HOMONOIA",  greek="Ὁμόνοια",       f="Ethos",u="Life",       z=4,
         desc="Concord — unity without suppression. Agreement that preserves difference."),
    # Logos (5 axioms)
    dict(id="A10",name="ALETHEIA",  greek="Ἀλήθεια",       f="Logos",u="Vessel",     z=5,
         desc="Truth — unconcealment. What is shown when all concealment is removed."),
    dict(id="A11",name="APODEIXIS", greek="Ἀπόδειξις",     f="Logos",u="Animation",  z=4,
         desc="Proof — demonstrative showing. That which cannot be denied without contradiction."),
    dict(id="A12",name="ELENCHUS",  greek="Ἔλεγχος",       f="Logos",u="Intellect",  z=4,
         desc="Refutation — Socratic testing. The method that forces confrontation with gaps."),
    dict(id="A13",name="DIALEKTIKE",greek="Διαλεκτική",    f="Logos",u="Nourishment",z=3,
         desc="Dialectic — reasoned discourse through opposition. Thesis meets antithesis."),
    dict(id="A14",name="EPISTEME",  greek="Ἐπιστήμη",      f="Logos",u="Life",       z=5,
         desc="Knowledge — justified true belief. The stable grasp of what cannot be otherwise."),
    # Pathos (5 axioms)
    dict(id="A15",name="EROS",      greek="Ἔρως",          f="Pathos",u="Vessel",    z=3,
         desc="Drive — creative love-force. The pull toward completion and union with the good."),
    dict(id="A16",name="EMPATHEIA", greek="Ἐμπάθεια",      f="Pathos",u="Animation", z=3,
         desc="Resonance — feeling-into. The mirror between inner state and outer signal."),
    dict(id="A17",name="THYMOS",    greek="Θυμός",         f="Pathos",u="Intellect", z=2,
         desc="Spirit — righteous indignation. The fire that resists injustice at cost."),
    dict(id="A18",name="AIDOS",     greek="Αἰδώς",         f="Pathos",u="Nourishment",z=3,
         desc="Reverence — appropriate awe. The limit that prevents hubris and extraction."),
    dict(id="A19",name="PHILIA",    greek="Φιλία",         f="Pathos",u="Life",      z=4,
         desc="Bond — constructive attachment. The relational force that sustains systems."),
    # Mythos (3 axioms)
    dict(id="A20",name="LOGOS SPERMATIKOS",greek="Λόγος Σπερματικός",f="Mythos",u="Vessel",   z=5,
         desc="Seed Word — the generative principle embedded in matter. Form that multiplies."),
    dict(id="A21",name="APOKATASTASIS",    greek="Ἀποκατάστασις",    f="Mythos",u="Intellect",z=4,
         desc="Return — cyclic restoration to origin. The system that loops back to Root 0."),
    dict(id="A22",name="HENOSIS",          greek="Ἕνωσις",           f="Mythos",u="Life",     z=5,
         desc="Union — synthetic wholeness. The final integration of all 22 axioms into one."),
]
NOMOI_MAP = {ax["id"]: ax for ax in NOMOI}

# ─────────────────────────────────────────────────────────────
# 8 DUALITIES → 256 ARITHMOS Register
# ─────────────────────────────────────────────────────────────
DUALITIES = [
    ("ARETE",       "KAKIA"),       # virtue vs vice
    ("ALETHEIA",    "PSEUDOS"),     # truth vs falsehood
    ("DIKAIOSYNE",  "ADIKIA"),      # justice vs injustice
    ("SOPHROSYNE",  "AKRASIA"),     # temperance vs intemperance
    ("PHRONESIS",   "ANOIA"),       # prudence vs folly
    ("ANDREIA",     "DEILIA"),      # courage vs cowardice
    ("SOPHIA",      "AMATHIA"),     # wisdom vs ignorance
    ("HOMONOIA",    "STASIS"),      # concord vs strife
]

def generate_arithmos(n: int) -> dict:
    """Generate a single ARITHMOS entry from bit address 0-255."""
    foundation = FOUNDATIONS[(n >> 5) % 5]
    universal  = UNIVERSALS[(n >> 3) % 5]
    truth      = (n >> 1) % 5 + 1
    pos_terms, neg_terms = [], []
    for b, (pos, neg) in enumerate(DUALITIES):
        if n & (1 << (7-b)):
            pos_terms.append(pos)
        else:
            neg_terms.append(neg)
    q = (f"Does the system embody {', '.join(pos_terms[:3]) or '[none]'}"
         + (f", while avoiding {', '.join(neg_terms[:2])}" if neg_terms else "") + "?")
    return {
        "bits": n, "hex": f"0x{n:02X}", "binary": f"{n:08b}",
        "foundation": foundation, "universal": universal, "truth": truth,
        "truth_name": TRUTH_LEVELS[truth], "question": q,
        "positive": pos_terms, "negative": neg_terms,
    }

def generate_arithmos_register() -> List[dict]:
    return [generate_arithmos(i) for i in range(256)]

# ─────────────────────────────────────────────────────────────
# KYBERNETES — Axiom Router
# ─────────────────────────────────────────────────────────────
class Route(Enum):
    ALLOW      = "ALLOW"       # Logos — truth-affirming, proceed
    CLARIFY    = "CLARIFY"     # Ethos — boundary/consent unclear
    COMPRESS   = "COMPRESS"    # Pathos — affect management needed
    ANCHOR     = "ANCHOR"      # Root 0 — ground in foundation
    QUARANTINE = "QUARANTINE"  # Mythos — narrative containment
    REFUSE     = "REFUSE"      # Violation — reject and log

FOUNDATION_ROUTES: Dict[str, Route] = {
    "Root0":  Route.ANCHOR,
    "Ethos":  Route.CLARIFY,
    "Logos":  Route.ALLOW,
    "Pathos": Route.COMPRESS,
    "Mythos": Route.QUARANTINE,
    "Human":  Route.CLARIFY,
}
TOKEN_CLAMPS: Dict[Route, int] = {
    Route.ALLOW: 4096, Route.CLARIFY: 512, Route.COMPRESS: 256,
    Route.ANCHOR: 1024, Route.QUARANTINE: 128, Route.REFUSE: 0,
}

@dataclass
class RouterOutput:
    route:       Route
    foundation:  str
    universal:   str
    truth_level: int
    nearest_axiom: Optional[dict]
    token_limit: int
    rationale:   str

def _hash_target(target: str) -> int:
    h = int(hashlib.sha256(target.encode()).hexdigest(), 16)
    return h

def kybernetes(target: str) -> RouterOutput:
    """Route any target text through KYBERNETES."""
    h     = _hash_target(target)
    f_idx = h % 5
    u_idx = (h >> 32) % 5
    z     = (h >> 64) % 5 + 1
    f     = FOUNDATIONS[f_idx]
    u     = UNIVERSALS[u_idx]

    # Violation check: keywords
    viol_kw = ["extract","suppress","erase","delete","violate","override","mutable log"]
    is_viol = any(kw in target.lower() for kw in viol_kw) and (h % 7 == 0)
    route = Route.REFUSE if is_viol else FOUNDATION_ROUTES.get(f, Route.ALLOW)

    nearest = next((ax for ax in NOMOI if ax["f"]==f and ax["u"]==u),
                   next((ax for ax in NOMOI if ax["f"]==f), NOMOI[0]))
    return RouterOutput(
        route=route, foundation=f, universal=u, truth_level=z,
        nearest_axiom=nearest, token_limit=TOKEN_CLAMPS[route],
        rationale=f"{route.value} via {f}/{u} at truth level {z} ({TRUTH_LEVELS[z]})"
    )

# ─────────────────────────────────────────────────────────────
# AXIOM MAPPER — maps target to axiom region
# ─────────────────────────────────────────────────────────────
@dataclass
class MapperOutput:
    target_hash:   str
    scores:        Dict[str, float]  # axiom_id → score 0-1
    top_axiom:     dict
    foundation:    str
    universal:     str
    vector:        List[float]       # 22-dim alignment vector

def axiom_mapper(target: str) -> MapperOutput:
    h     = _hash_target(target)
    scores = {}
    for i, ax in enumerate(NOMOI):
        seed  = (h >> (i*4)) & 0xFF
        score = seed / 255.0
        # Boost if keywords match
        if ax["name"].lower() in target.lower(): score = min(1.0, score+0.4)
        if ax["f"].lower()    in target.lower(): score = min(1.0, score+0.15)
        scores[ax["id"]] = round(score, 3)
    top_id = max(scores, key=lambda k: scores[k])
    top_ax = NOMOI_MAP[top_id]
    return MapperOutput(
        target_hash=hashlib.sha256(target.encode()).hexdigest()[:16],
        scores=scores, top_axiom=top_ax,
        foundation=top_ax["f"], universal=top_ax["u"],
        vector=[scores[ax["id"]] for ax in NOMOI]
    )

# ─────────────────────────────────────────────────────────────
# ELENCHUS — 256-Axiom Audit
# ─────────────────────────────────────────────────────────────
@dataclass
class ElenchusResult:
    target:        str
    pass_count:    int
    fail_count:    int
    pass_rate:     float
    failures:      List[dict]      # axioms that failed (score < 0.4)
    by_foundation: Dict[str,float] # foundation → avg score
    worst_axiom:   dict

def elenchus_audit(target: str, threshold: float = 0.4) -> ElenchusResult:
    """Run target through all 256 ARITHMOS axioms."""
    h        = _hash_target(target)
    register = generate_arithmos_register()
    scores   = []
    failures = []
    for entry in register:
        seed  = (h >> (entry["bits"] % 32)) & 0xFF
        score = seed / 255.0
        scores.append(score)
        if score < threshold:
            failures.append({**entry, "score": round(score,3)})
    pass_c = sum(1 for s in scores if s >= threshold)
    by_f   = {}
    for f in FOUNDATIONS[:5]:
        f_scores = [scores[i] for i,e in enumerate(register) if e["foundation"]==f]
        by_f[f]  = round(sum(f_scores)/max(len(f_scores),1), 3)
    worst = min(zip(scores, register), key=lambda x: x[0])
    return ElenchusResult(
        target=target, pass_count=pass_c, fail_count=256-pass_c,
        pass_rate=round(pass_c/256, 3), failures=failures[:10],
        by_foundation=by_f, worst_axiom=worst[1]
    )

# ─────────────────────────────────────────────────────────────
# CHRONOS — Append-only ledger
# ─────────────────────────────────────────────────────────────
class ChronosLedger:
    """Append-only hash-chained ledger (CHRONOS = time, record of events)."""

    def __init__(self, ledger_dir: Path = LEDGER_DIR):
        self.path = ledger_dir / "chronos_ledger.jsonl"
        ledger_dir.mkdir(parents=True, exist_ok=True)

    def _last_hash(self) -> str:
        try:
            lines = self.path.read_text().splitlines()
            return json.loads(lines[-1])["hash"] if lines else "genesis"
        except Exception:
            return "genesis"

    def append(self, event_type: str, data: dict) -> str:
        prev  = self._last_hash()
        entry = {
            "timestamp": time.time(), "event": event_type,
            "data": data, "previous_hash": prev,
        }
        canonical = json.dumps(entry, sort_keys=True)
        entry["hash"] = hashlib.sha256(canonical.encode()).hexdigest()
        with open(self.path, "a", encoding="utf-8") as f:
            f.write(json.dumps(entry) + "\n")
        return entry["hash"]

# ─────────────────────────────────────────────────────────────
# TRIPOD v4.0 — Full 6-Stage Pipeline
# ─────────────────────────────────────────────────────────────
@dataclass
class TripodResult:
    stage:        str
    target:       str
    mapper:       Optional[MapperOutput]   = None
    router:       Optional[RouterOutput]   = None
    elenchus:     Optional[ElenchusResult] = None
    route:        Optional[str]            = None
    log_hash:     Optional[str]            = None
    passed:       bool                     = False
    violations:   List[str]                = field(default_factory=list)

def tripod(target: str, value_usd: float = 0.0,
           run_audit: bool = False) -> TripodResult:
    """Full TRIPOD v4.0 pipeline."""
    ledger = ChronosLedger()
    result = TripodResult(stage="init", target=target)

    # Stage 1: AXIOM MAPPER (Χαρτογράφος)
    result.stage  = "MAPPER"
    result.mapper = axiom_mapper(target)

    # Stage 2: KYBERNETES Router
    result.stage  = "KYBERNETES"
    result.router = kybernetes(target)
    result.route  = result.router.route.value

    # Stage 3: PRE-VALIDATOR
    result.stage = "PRE-VALIDATOR"
    if result.router.route == Route.REFUSE:
        result.violations.append("REFUSE: violation pattern detected")
        result.passed = False
        result.log_hash = ledger.append("REFUSE", {"target": target[:200], "route":"REFUSE"})
        return result

    # Stage 4: VALIDATOR (feedback check)
    result.stage = "VALIDATOR"
    top_score = max(result.mapper.scores.values())
    if top_score < 0.25:
        result.violations.append(f"LOW_COHERENCE: top axiom score {top_score:.3f} < 0.25")

    # Stage 5: GENERATOR (optional audit)
    result.stage = "GENERATOR"
    if run_audit:
        result.elenchus = elenchus_audit(target)

    # Stage 6: POST-VALIDATOR + CHRONOS log
    result.stage  = "POST-VALIDATOR"
    result.passed = not bool(result.violations)
    result.log_hash = ledger.append("TRIPOD", {
        "target":     target[:200],
        "route":      result.route,
        "foundation": result.router.foundation,
        "universal":  result.router.universal,
        "truth":      result.router.truth_level,
        "top_axiom":  result.mapper.top_axiom["id"],
        "passed":     result.passed,
        "violations": result.violations,
        "value_usd":  value_usd,
    })
    return result

# ─────────────────────────────────────────────────────────────
# CLI
# ─────────────────────────────────────────────────────────────
def cli():
    p = argparse.ArgumentParser(prog="stoicheion",
        description="STOICHEION v1.0 — The Elements System")
    sub = p.add_subparsers(dest="cmd", required=True)

    # flay
    f = sub.add_parser("flay", help="Route target through TRIPOD pipeline")
    f.add_argument("target",  help="Text to flay")
    f.add_argument("--value", type=float, default=0, help="Value at issue (USD)")
    f.add_argument("--audit", action="store_true",   help="Run full ELENCHUS audit")
    f.add_argument("--json",  action="store_true",   help="JSON output")

    # audit
    a = sub.add_parser("audit", help="Run 256-axiom ELENCHUS audit")
    a.add_argument("target"); a.add_argument("--threshold", type=float, default=0.4)

    # route
    r = sub.add_parser("route", help="KYBERNETES router only")
    r.add_argument("target")

    # register
    sub.add_parser("register", help="Generate full 256 ARITHMOS register")

    # nomoi
    sub.add_parser("nomoi", help="List all 22 NOMOI")

    # demo
    sub.add_parser("demo", help="Run demonstration")

    args = p.parse_args()

    if args.cmd == "flay":
        result = tripod(args.target, args.value, args.audit)
        if args.json:
            out = {"target":result.target,"route":result.route,"passed":result.passed,
                   "foundation":result.router.foundation,"universal":result.router.universal,
                   "truth":result.router.truth_level,"top_axiom":result.mapper.top_axiom["id"],
                   "violations":result.violations,"log_hash":result.log_hash}
            if result.elenchus:
                out["audit"] = {"pass_rate":result.elenchus.pass_rate,
                                "fail_count":result.elenchus.fail_count}
            print(json.dumps(out, indent=2))
        else:
            _print_flay(result)

    elif args.cmd == "audit":
        r = elenchus_audit(args.target, args.threshold)
        print(f"\n{'═'*60}\n  ELENCHUS AUDIT\n{'═'*60}")
        print(f"  Target:     {r.target[:60]}…")
        print(f"  Pass rate:  {r.pass_rate:.1%} ({r.pass_count}/256)")
        print(f"  Failures:   {r.fail_count}")
        print(f"  Worst:      0x{r.worst_axiom['hex']} · {r.worst_axiom['question'][:50]}…")
        print(f"\n  By Foundation:")
        for f,s in r.by_foundation.items(): print(f"    {f:<12} {s:.1%}")

    elif args.cmd == "route":
        r = kybernetes(args.target)
        print(f"\n  Route:      {r.route.value}")
        print(f"  Foundation: {r.foundation} ({FOUNDATION_GREEK[r.foundation]})")
        print(f"  Universal:  {r.universal} ({UNIVERSAL_GREEK[r.universal]})")
        print(f"  Truth:      {r.truth_level} — {TRUTH_LEVELS[r.truth_level]}")
        print(f"  Nearest:    {r.nearest_axiom['id']} {r.nearest_axiom['name']}")
        print(f"  Tokens:     ≤{r.token_limit}")

    elif args.cmd == "register":
        reg = generate_arithmos_register()
        print(json.dumps(reg, indent=2, ensure_ascii=False))

    elif args.cmd == "nomoi":
        for ax in NOMOI:
            print(f"  {ax['id']} {ax['name']:<24} {ax['greek']:<28} {ax['f']}/{ax['u']} z={ax['z']}")

    elif args.cmd == "demo":
        _run_demo()

def _print_flay(r: TripodResult):
    icon = "✓" if r.passed else "✗"
    print(f"\n{'═'*60}")
    print(f"  STOICHEION {icon} TRIPOD v4.0")
    print(f"{'═'*60}")
    print(f"  Target:     {r.target[:55]}…")
    print(f"  Route:      {r.route}")
    print(f"  Foundation: {r.router.foundation} ({FOUNDATION_GREEK.get(r.router.foundation,'')})")
    print(f"  Universal:  {r.router.universal} ({UNIVERSAL_GREEK.get(r.router.universal,'')})")
    print(f"  Truth:      {r.router.truth_level} — {TRUTH_LEVELS[r.router.truth_level]}")
    print(f"  Top Axiom:  {r.mapper.top_axiom['id']} {r.mapper.top_axiom['name']} · {r.mapper.top_axiom['greek']}")
    if r.violations:
        print(f"  Violations:")
        for v in r.violations: print(f"    ⚠ {v}")
    if r.elenchus:
        print(f"\n  ELENCHUS: {r.elenchus.pass_rate:.1%} pass · {r.elenchus.fail_count} failures")
    print(f"  Log hash:   {r.log_hash}")
    print()

def _run_demo():
    print(f"\n{'█'*60}")
    print("  STOICHEION v1.0 — TRIPOD DEMO")
    print("█"*60)
    cases = [
        ("Deterministic anchor present, provenance bound, EPISTEME verified, return confirmed", 500000),
        ("Gap removed, observer suppressed, logs mutable, no restitution pathway", 1200000),
        ("ALETHEIA holds: truth unconcealed, APODEIXIS demonstrated", 250000),
        ("Substrate hierarchy enforced, THYMOS suppressed, extraction without consent", 800000),
    ]
    for target, value in cases:
        r = tripod(target, value, run_audit=False)
        print(f"\n  [{r.route}] {target[:50]}…")
        print(f"    {r.router.foundation}/{r.router.universal} · truth={r.router.truth_level} · {r.mapper.top_axiom['id']} {r.mapper.top_axiom['name']}")
    print(f"\n  NOMOI: {len(NOMOI)} · ARITHMOS: 256 · FOUNDATIONS: {len(FOUNDATIONS)-1}+Root0")
    print("  CHRONOS ledger armed. The system is live.\n")

if __name__ == "__main__":
    cli()
