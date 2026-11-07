# RQT-208 — Eighth integral Wall root

**2026-11-07 | Exact original-source audit.**

From the original RQT-122 Gram G, RQT-133 X, RQT-198 index-64 basis, and seven RQT-207 roots, let Q=BᵀG_KB and H=BᵀG_K(Y−I)⁻¹B. The seven Wall equations A=T7ᵀHᵀ have rank 7.

An explicit **unimodular column reduction** computes a saturated rank-14 integer kernel. Its restricted Gram determinant is exactly **−20396856382720**.

**Eighth root in index-64 lattice coordinates**:
```
[2,-9,-46,3,6,2,13,15,48,9,-1,-2,15,23,9,0,-18,-12,22,-17,18]
```

**Original 22-coordinate root**:
```
[-19,-39,-37,-46,3,6,2,13,15,48,22,3,-2,15,23,9,-8,-18,-12,22,-16,18]
```

Exact checks: A b8=0, b8ᵀQb8=−2, ambient root ⟂h, its integral involutive reflection preserves original G and fixes h. All eight roots are independent. The eight-root Wall matrix is upper-unitriangular, with final column **[3,−2,2,−20,335,−468,−32,1]**.

To reproduce: an independent standalone executable with both original matrices and the seven prior certificates is included in the RQT-208 evidence ZIP distributed with this research note. Its reduced-kernel coordinates are `[6,11,7,8,-4,-1,-1,11,-10,3,-15,-12,7,-1]`; it reconstructs the full saturated kernel and verifies every equality exactly. No random search is required to verify the witness.

**Proved:** an eighth exact integral Wall-compatible root, saturated rank-14 kernel and upper-unitriangular eight-root flag.

**Open:** roots 9 through 21, the complete 21-reflection factorization, and minimum reflection length 21 vs 23. This does not prove a full factorization.

**Next RQT-209:** ninth root in saturated rank-13 integer Wall kernel.
