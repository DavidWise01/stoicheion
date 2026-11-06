# RQT-181 — Gram transport and exact isometry audit

**Date:** 2026-11-06. **Source:** actual RQT-122 22×22 Gram matrix, RQT-133 operator, and RQT-180 integral conjugator.

## Exact results
The integer matrices satisfy X^4=I, det(P)=+1 and P^-1 X P=Y=C4⊕H^6. Transport G by Gcan=P^T G P. The original and transformed Gram matrices are symmetric and satisfy X^T G X=G and Y^T Gcan Y=Gcan.

- det G=det Gcan=**−1**
- lattice parity: **even** (all diagonal entries even)
- signature: **(3,19)**, calculated with exact rational symmetric congruence elimination
- regular C4-sector Gram block: diag −2, off-diagonal +1; determinant **−27**
- pairings among the seven canonical action blocks: **19 nonzero cross-block pairs**, 2 zero
- zero cross-block pairs (block indices starting at 0): **(0,3)** and **(0,4)**.

## Mathematical interpretation
The original integral form is an even unimodular lattice of signature (3,19), hence abstractly isometric to the **K3 lattice** U^3 ⊕ E8(−1)^2, by the standard uniqueness theorem for indefinite even unimodular lattices. This is a **lattice-theoretic statement**, not independent proof that the input matrix arises from a specific geometric K3 surface, nor a proof of the Hodge conjecture.

The isometry action splits as C4⊕H^6, but Gcan is **not orthogonally block diagonal**. The module splitting and orthogonal splitting are different questions.

## Reproduce
Run `python research/rqt/rqt181_gram_transport.py` (SymPy required). The script uses original source X and Gram files; it reuses RQT-180 certificate script to regenerate P if needed, and writes `G-canonical-22x22.txt` and `RQT-181-report.json`.

## Next boundary
**RQT-182 — Primitive invariant sublattice and discriminant gluing.** Analyze fixed vector h, its orthogonal complement, primitive saturation and the order-four discriminant coupling, without confusing module and orthogonal decompositions.
