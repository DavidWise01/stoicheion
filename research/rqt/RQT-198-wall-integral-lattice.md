# RQT-198 — An explicit index-64 Wall-integral lattice

**2026-11-07 | Exact original RQT-122/133 source audit.**

Let K be the original rank-21 primitive orthogonal complement, Y=X|K, W=G_K(Y−I)^−1 and Z=4W. Previously: det(W)=2^−12 and Smith(Z)=diag(1^6,4^15).

## Construction

Define L={x∈K : Zᵀx≡0 (mod 2)}, with coordinates taken in the original integral K basis. Row-reduction of Zᵀ mod 2 has rank 6 and pivot columns (0,1,9,10,15,19); an explicit 21×21 integer basis matrix B is built by solving the six parity constraints.

Exact results:
- |det(B)|=64, hence [K:L]=64;
- **Bᵀ W B is integral with determinant 1**;
- det(Bᵀ G_K B)=−16384;
- W+Wᵀ=−G_K and all diagonals of 4W vanish modulo 4;
- (4W)+(4W)ᵀ≡0 (mod 4).

The mod-Z fractional Wall pairing on K is alternating; the parity-kernel construction provides a maximal isotropic sublattice for the fractional pairing. Thus **index 64 and Wall integrality/unimodularity are simultaneously achievable**. This does not ensure an ordered square-(-2) root basis or the upper-unitriangular Wall form required for a 21-root factorization.

## Bounded short-root check

For the displayed basis B, exhaustively enumerate all signed-support coordinate vectors of size one, two, and three. Exact norm −2 counts are respectively **2, 0, 0**, and the resulting roots have span rank **1**. This is a *bounded search in the displayed basis*, not a global claim about L, its root generation, or the existence of another index-64 lattice satisfying the full 21-root condition.

## Scope

**PASS:** explicit index-64 Wall-integral unimodular lattice, verified on original matrices.
**OPEN:** 21-element root basis with triangular Wall pairing; minimal reflection length remains 21 or 23.

## Reproduce
Run `research/rqt/rqt198_wall_integral_lattice.py` with the two archived original source files. The standalone evidence bundle contains its full 21×21 basis and JSON results.

## Next boundary: RQT-199 — Wall-unitriangular root-chain search
Find a square−2 root chain whose one-sided Wall pairings vanish in the required triangular order, or prove a genuine obstruction. Do not infer nonexistence from a bounded sparse search.
