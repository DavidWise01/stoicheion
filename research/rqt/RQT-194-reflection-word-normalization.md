# RQT-194 — Reflection-word normalization and exact length bounds

**2026-11-06 | Original RQT-122/133 matrices and RQT-193 25-root certificate**

## Exact lower bound
For a root reflection R_r, rank(R_r−I)=1 and det(R_r)=−1. Therefore any word of m root reflections has rank(product−I)≤m and det(product)=(−1)^m. The original operator has rank(X−I)=21, det X=−1. Together with the proven RQT-193 25-root upper bound this yields **minimum length in {21,23,25}**. Neither 21 nor 23 has been constructed or excluded.

## Exact braid normalization
The 25 roots have a single repeated root pair up to sign: **r1=r20**. Exact original-Gram computations give <r1,rj>=0 for j=3,...,19, and <r1,r2>=1. Thus the 20th reflection commutes left across positions 3..19:
`R1 R2 R20 R3...R19 R21...R25=R1 R2 R1 R3...R19 R21...R25`.
The first three reflections form an A₂ braid:
`R1 R2 R1=R2 R1 R2`.
The original, commuted, and braided words all have length 25 and all match the original X **exactly**. None has adjacent equal reflections that cancel. All original roots were rechecked to lie in K=h-perp, have square -2, and preserve the original Gram.

**Scope:** word normalization and proved length bound, *not* a shorter word, no minimality proof, no generation theorem.

## Reproduce
Run `research/rqt/rqt193_full_stabilizer_factorization.py` to generate the full root list; then run `research/rqt/rqt194_word_audit.py`. Both require archived original X and Gram in `research/rqt/source/`. An independent self-contained ZIP containing both matrices, 25 roots, full script, note and report is downloadable from the conversation artifact.

## RQT-195
Bounded Hurwitz moves / nontrivial cancellation search for a 23-root word, then investigate integral Wall form for a genuine lower bound. Failed bounded searches must not be reported as nonexistence.
