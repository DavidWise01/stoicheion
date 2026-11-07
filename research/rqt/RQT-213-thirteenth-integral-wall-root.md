# RQT-213 — Thirteenth exact integral Wall root

2026-11-07. Source: original RQT-122 Gram and RQT-133 operator, RQT-198 index-64 basis, and twelve-root RQT-212 flag.

Let Q=BᵀG_KB and H=BᵀG_K(Y−I)⁻¹B. A=T12ᵀHᵀ has rank 12. Starting with RQT-212's saturated rank-10 integer kernel, a final unimodular row reduction gives pivot 1 and a saturated **rank-9** integer kernel. Its Gram determinant is **55925958066991376120**.

The thirteenth integral root in the RQT-198 basis:

`84,-238,-1156,94,130,170,306,358,1229,299,5,-44,269,534,176,2,-472,-250,532,-426,534`

The original 22-coordinate root:

`-494,-972,-823,-1156,94,130,170,306,358,1229,527,72,-44,269,534,176,-186,-472,-250,532,-318,534`

The reduced-kernel search witness is `39,-36,-2,-46,52,-23,-76,-48,-36`.

Exact verification establishes: norm −2, original h-orthogonality, twelve zero one-sided Wall constraints, thirteen independent roots, and an upper-unitriangular thirteen-root Wall form. Its new column is `0,-91,46,-532,8400,-16264,-1228,-277,-825,261,-439,183,1`. The associated integral reflection is an involution preserving original G and fixing h.

**PROVED:** rank-13 exact integral Wall root flag. **OPEN:** roots 14–21, full 21-reflection equality, minimality 21 versus 23.

The self-contained evidence ZIP accompanying this result includes all prior JSON reports, original matrices, saturation and reduced basis matrices, Python search/verification scripts, and the full 13×13 Wall matrix.

**RQT-214:** construct the saturated rank-8 integer kernel of the 13 Wall constraints and seek root 14.
