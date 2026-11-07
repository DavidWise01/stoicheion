# RQT-197 — Exact 2-primary Wall pairing for the 21-root boundary

**2026-11-07 | Original RQT-122/133 matrices.**

Let K=h⊥ in M and Y=X|K. Define the rational Wall pairing W=G_K(Y−I)^−1.

Measured exactly:
- det(G_K)=−4 and det(Y−I)=−16384;
- W+Wᵀ=−G_K;
- det(W)=1/4096=2^−12;
- minimal common denominator of W is 4;
- SNF(4W)=diag(1^6,4^15).

**New necessary condition for 21 roots.** Suppose Y=R_(b1)...R_(b21) with 21 integral roots in K, all of norm −2. Let B be their square root-column matrix. Product expansion gives Y−I=B C Bᵀ G_K, where C is integral *upper unitriangular*. Because Y−I is invertible, B is invertible rationally. Thus W=B^(−T) C^−1 B^−1 and BᵀWB=C^−1 must be integral, unimodular and upper unitriangular. Determinants force |det B|=64, hence the 21 roots must span an index-64 sublattice. This strengthens RQT-196 with an ordered Wall-integral basis criterion.

For cross-check, the proven RQT-195 23-root word has a 23×23 Wall pairing with 397 integral entries, 36 entries of denominator 2, and 96 of denominator 4; its (1,14) entry is −3/4. The 23 roots are dependent (rank21), so the 21-root criterion does NOT apply directly and the fractional entry is not an obstruction to the existing valid word.

**Proved:** exact Wall invariant and conditional 21-root basis theorem. **Open:** existence of such an index-64 ordered root basis and whether minimal length is 21 or 23.

**Reproduce:** `research/rqt/rqt197_wall_form.py` using original source matrices plus `RQT-195-hurwitz-proof.json`. The downloadable original-source ZIP contains all inputs and the exact audit.

**RQT-198:** Seek an index-64 Wall-integral root basis with upper-unitriangular pairing, or establish a genuine arithmetic obstruction. Avoid promoting bounded search failures into nonexistence claims.
