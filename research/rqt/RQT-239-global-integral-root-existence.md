# RQT-239 — Global existence of an integral seventeenth Wall root

**2026-11-08. THEOREM — exact root exists; coordinates not yet constructed.**

Preserve the first 15 integral Wall roots and Branch 2's alternative 16th root from RQT-224. The exact saturated rank-five Wall kernel has even integral Gram F5 (in the self-contained evidence ZIP), signature **(1,4)**, and

```
det(F5) = 312669187727137013416789354039323478
        = 2 * 139801 * 7915189 * 646956613 * 218377739361227.
```

Every displayed factor is a distinct prime: **det(F5) is squarefree**.

## Proof: global norm−2 representation

1. **Meyer's theorem:** every indefinite rational quadratic form in at least five variables is isotropic over Q. Scale denominators and divide by coordinate gcd to obtain a **primitive integral isotropic** `u∈Z⁵` with `uᵀF5u=0`.
2. Let `d=gcd(F5 u)`. Extend primitive u to an integral unimodular basis. Its first Gram row/column are divisible by d and first diagonal entry is zero. Double determinant expansion gives `d² | det(F5)`. Squarefree determinant forces **d=1**.
3. Bézout gives `v∈Z⁵` with `uᵀF5v=1`. Evenness gives `vᵀF5v=2k` for some integer k. Set `w=v−ku`; then `w²=0`, `u·w=1` and `r=u−w` has **r²=−2**.
4. Mapping r through the exact integral saturated kernel basis gives a square−2 integral root orthogonal in the required one-sided Wall orientation to the first **16** certified roots. Therefore **a seventeenth integral Wall-compatible root is globally guaranteed to exist**.

Moreover the lattice splits integrally as `L5 ≅ U ⊕ N3`, where U is a unimodular hyperbolic plane with Gram `[[0,1],[1,0]]` and N3 is even, negative definite of rank 3.

**Distinction:** This is an exact *existence theorem*, not an explicit vector or a 17-reflection product. No explicit u/v/w/r has been computed. Nor does this prove that one can select r from RQT-237's 132 modular-completion-compatible classes or finish the remaining four reflections to reach 21.

## Exact unimodular basis reduction

```
B =
[-16, -2, -11,  58, 144]
[ -2,  0,  -1,   7,  17]
[  7,  1,   5, -25, -63]
[  1,  0,   1,  -4,  -9]
[  7,  1,   5, -26, -65]
```

`det B=−1`, and `J=BᵀF5B` is

```
[ -8319932, -3097057,  2813438, -1794298,  -149943]
[ -3097057,-15432094, -1413796,   393685,  5285590]
[  2813438, -1413796,-19053854,  3128649, -2048137]
[ -1794298,   393685,  3128649,-10194696,  4874825]
[  -149943,  5285590, -2048137,  4874825, 10734700]
```

The exact quadratic-discriminant audit checked every assignment of the first four new coefficients in [−40,40] (**81⁴ = 43,046,721**), solving the fifth with no bound, and found zero integral norm−2 roots in this *finite* box. This does not contradict the theorem.

**Independent original-source verification:** `rqt235_verify.py` reconstructs F5 from the original 22×22 Gram/operator and all preceding root reports; `rqt239_existence_verify.py` verifies evenness, signature, exact squarefree determinant and J/B. The attached self-contained RQT-239 evidence ZIP includes both and the exhaustive C++ search source and log.

**Next natural target RQT-240:** implement an *exact constructive Meyer-isotropic-vector solver* and derive `r=u−(v−(v²/2)u)` with explicit integer coordinates; screen the resulting root modulo4 for continued 21-reflection viability.

**STATUS:** global integral root17 EXISTENCE PROVED; explicit root17 coordinates OPEN; full 21-reflection equality OPEN.
