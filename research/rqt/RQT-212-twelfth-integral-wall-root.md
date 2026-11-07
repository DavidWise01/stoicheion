# RQT-212 — Twelfth integral Wall root

**2026-11-07 | Exact original-source certificate PASS**

Let Q=BᵀG_KB and H=BᵀG_K(Y−I)⁻¹B, with the RQT-198 index-64 basis and the eleven exact roots previously certified by RQT-211. The 11 linear constraints A=T11ᵀHᵀ have rank 11. From the *saturated* 21×11 kernel of the first ten constraints (RQT-211), apply exact unimodular reduction to the final constraint; its integer pivot has absolute value **1**. The resulting lattice kernel is **saturated rank 10**, and its restricted Gram determinant is **−869552306284552708**.

The **twelfth root**, in RQT-198 lattice coordinates:

`-27,101,467,-34,-58,-69,-120,-148,-492,-117,-1,17,-109,-214,-71,1,184,98,-214,170,-214`

In the original 22-coordinate lattice:

`211,391,336,467,-34,-58,-69,-120,-148,-492,-213,-32,17,-109,-214,-71,70,184,98,-214,126,-214`

The candidate was found by an LLL-reduced integer-kernel search with reduced coefficients `[24,10,20,23,23,35,16,-18,8,19]`. The exact replay confirms its squared norm is **−2**, its eleven one-sided Wall equations vanish, and its ambient vector is orthogonal to h. The twelve roots are independent; the upper-unitriangular Wall matrix has final column

`[-4,34,-23,219,-3496,6287,503,114,321,-92,130,1]`.

The integral reflection `I+r(rᵀG)` is an involutive G-isometry fixing h.

**PASS:** 12-root Wall upper-unitriangular flag; saturated rank-10 integral kernel; original-matrix audit. **OPEN:** roots 13 through 21; complete 21-reflection equality; minimum length 21 vs 23.

The downloadable RQT-212 archive contains both original source matrices, previous certificates, saturated kernel, 12×12 Wall matrix, and an executable exact verification.

**Next RQT-213:** thirteenth root via the saturated rank-nine Wall kernel.
