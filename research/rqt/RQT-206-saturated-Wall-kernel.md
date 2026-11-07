# RQT-206 — Saturated rank-15 Wall kernel and parity audit

2026-11-07. Exact source: original RQT-122 Gram G, RQT-133 X, RQT-198 candidate lattice basis and six previously certified roots.

Let Q=Bᵀ G_K B and H=Bᵀ G_K (Y−I)⁻¹B; let T6 be the 6-root flag. A=T6ᵀ Hᵀ has exact rank 6. In order to find a seventh root b7, we require A b7=0 and b7ᵀQb7=−2.

**New invariant:** Pivot columns (1,2,6,9,11,13) have determinant **+2**, and there is no unit 6×6 minor in A. The naive rational nullspace is not an integer basis. The pivot construction leaves 15 free coordinates subject to one mod-2 congruence. An explicit determinant-2 free-coordinate correction yields a *saturated* 21×15 integer kernel basis M, with A M=0. The full exact basis and restricted Gram are included in the standalone RQT-206 evidence bundle.

**Restricted form:** det(MᵀQM)=393184631552. Numerical inertia is (1,14); the reported determinant is exact, while that inertia was evaluated numerically.

**Exhaustive parity census:** all 2^15=32768 binary classes in the integer kernel; 15360 have quadratic norm ≡−2 mod4 and span the full 15-dimensional binary space. Thus this parity layer provides no root obstruction.

**Bounded integer search:** signed-support ±1 with supports 1,2,3 in the saturated basis found zero norm−2 roots. A separate finite randomized search also found no witness. These failures do not establish nonexistence.

**Status:** exact saturated kernel and parity-layer audit PASS; seventh root OPEN; 21-vs-23 minimal root length OPEN. No seventh root and no 21-reflection word is claimed.

**Reproduce:** Download the complete original-source ZIP from the accompanying research response; it contains `rqt206_exact_kernel.py`, all prerequisite JSON reports, original X and Gram, the full 15-dimensional kernel, and exact output.

**RQT-207:** use hyperbolic splitting / indefinite lattice methods on the saturated kernel to seek an actual integral square−2 vector.
