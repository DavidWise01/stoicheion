# RQT-196 — Reflection-lattice index invariant

**2026-11-07. Exact original-source arithmetic.**

Using the original RQT-133 22×22 integer operator X, the original RQT-122 Gram G and the independently verified RQT-195 23-root word:

Set K=h^perp∩M with rank 21 and det(G_K)=−4, Y=X|K. Exact computations show:

- det(I−Y)=16384=2^14.
- Smith(I−Y)=diag(1^14,4^7).
- The 23 existing square−2 roots span a rank-21 sublattice L23⊂K with Smith coordinate form diag(1^19,4,4), so [K:L23]=16.
- The exact 23-root reflection product equals the original X.

**New necessary condition:** If X admits a 21-reflection factorization in K, let B be the 21×21 integral matrix of its root columns. Expansion of the reflections R_r=I+r(rᵀG) yields Y=I+B C Bᵀ G_K with C triangular and det(C)=1. Thus det(I−Y)=(-1)^21 det(B)^2 det(G_K)=4 det(B)^2, forcing |det B|=64. So the hypothetical 21 roots must span an **index-64** sublattice of K, four times the index of the current 23-root witness.

This is a **necessary** arithmetic condition, not an obstruction to existence and not a proof that the minimum is 23. The minimum remains in {21,23}.

Reproduce via research/rqt/rqt196_reflection_index.py using archived originals and RQT-195-hurwitz-proof.json. Full original-source stand-alone bundle is downloadable from the conversation.

**RQT-197:** test the 2-primary Wall/Gram constraints for a candidate index-64 root basis, seeking either a 21-root construction or a rigorous new obstruction.
