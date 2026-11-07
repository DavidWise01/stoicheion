# RQT-188 — Extended negative-root descent and rank-two monotonic obstruction

**2026-11-06 | Exact audit of original RQT-133 X and original RQT-122 Gram G.**

## Measured result

The six root reflections from RQT-187 extend by 13 further integral square-(−2) reflections in the fixed-vector orthogonal complement K. Exact rank sequence of F_j−I (j=0..19):

`21,20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2`.

Each reflection R_r=I+r(rᵀG) is integral, satisfies r²=−2, fixes h, has determinant −1 and preserves G. Reversing the 19 transformations reconstructs the original 22×22 X **exactly**:

`X=R1 R2 ... R19 F19`.

This is a **partial factorization**, not yet a product exclusively of negative-root reflections.

## Reproducible new witness coefficients

Let K have basis k_j=e_(j+1)−e0 for j=0..18 and k19=e20, k20=e21. For each j=7..19 define r_j=(F_(j−1)−I)Kc_j and F_j=R_(r_j) F_(j−1).

Coefficients:
- c7=k20
- c8=k5−k14
- c9=k2−k17
- c10=k0−k5
- c11=k0−k1
- c12=k0
- c13=k15
- c14=k13
- c15=k7
- c16=k4
- c17=k8
- c18=k9
- c19=k12

See `rqt188_residual_descent.py` for the first six roots and all subsequent exact arithmetic checks.

## Stronger final boundary — monotone descent obstruction

The residual F19 has rank(F19−I)=2, determinant +1, and is unipotent. In an exact rational basis of V=im_Q(F19−I), the Gram matrix is

```
[[0, 0],
 [0,-6]]
```

Hence every rational r∈V has r²=−6q². Requiring r²=−2 gives q²=1/3, impossible over Q. Thus V contains **no rational −2 root**.

For a rank-one correction R_rF−F=r(rᵀGF), strictly reducing rank(F−I) requires r∈im_Q(F−I). Consequently **there is no next strictly rank-reducing integral −2 reflection** starting at F19. This is a proof that the *particular monotone rank-decreasing method* is exhausted.

It does **not** prove that F19 is outside the negative-root reflection group: a longer non-monotone factorization is still possible. No claim of impossibility for arbitrary products of root reflections follows.

## Status
- 19-reflection exact partial factorization: **PASS**.
- Rank-two image and quadratic-form obstruction: **PROVED**.
- Complete factorization: **OPEN**.

## Next natural boundary
**RQT-189 — Non-monotone root bridge or independent group-theoretic obstruction.** Test short root insertions that temporarily increase rank, with exact final reconstruction. Consider independent invariants of the residual before asserting full root-generation.
