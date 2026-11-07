# RQT-200 — Complete binary quadratic root-class census

**2026-11-07 | Exact original RQT-122/133 sources.**

Let K=h^⊥∩M with integral Gram G_K, and let L⊂K be the verified index-64 candidate of RQT-198 with basis B. Set Q=BᵀG_KB and H=BᵀWB, where W=G_K(Y−I)^−1. Exact source verification: det Q=−16384, det H=1, H integral, H+Hᵀ=−Q.

## The next natural invariant

The square−2 equation xᵀQx=−2 implies xᵀQx≡2 mod 4. Since Q has even diagonal, this residue is determined entirely by x mod 2. Define the binary quadratic form q(x)=xᵀQx/2 mod 2 on (F₂)^21.

The **complete 2^21-class census** gives:
- All binary classes: **2,097,152**.
- Classes with xᵀQx≡2 mod 4: **983,040** (46.875%).
- Rank of polar form Q mod 2: **8**.
- Radical dimension: **13**.
- q vanishes identically on the radical.
- Arf invariant on the resulting 8D nonsingular quotient: **0**.
- Independent analytic check of the count: 2^13(2^7−2^3)=**983,040**.
- Qualifying residue classes span all **21 binary dimensions**.

A particularly short full-rank mod-2 witness consists of 21 classes, each with coordinate support ≤2. There are 11 qualifying singleton supports and 122 qualifying unordered two-coordinate supports. The 21 independent classes and full enumeration are in the executable audit's JSON output.

## Exact scope of the result

**PROVED:** The index-64 candidate admits 21 linearly independent binary residue classes satisfying the *necessary modulo-four norm condition* for −2 roots. The first parity layer does not obstruct a full-rank root basis.

**NOT PROVED:** L contains 21 actual integral roots of norm exactly −2. The chosen residue classes need not lift to such roots, need not satisfy Wall triangularity, and provide no 21-reflection product certificate. The minimum remains either 21 or 23.

## Reproduce

Run `research/rqt/rqt200_binary_quadratic_census.py` with original sources and RQT-198-report.json. Exhaustively enumerate 2^21 classes; verify Arf counts, radical vanishing, and independent short supports. The standalone ZIP contains source files, runnable program, detailed result, and this note.

## Next boundary — RQT-201

Lift the 21 independent parity classes to exact square−2 roots, with Wall pairings checked incrementally; distinguish congruence feasibility from an integral ordered root-chain certificate.
