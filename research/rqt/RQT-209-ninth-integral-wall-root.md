# RQT-209 — Ninth integral Wall root

**2026-11-07 | Exact original RQT-122 Gram and RQT-133 operator**

The eight certified RQT-208 roots extend to nine independent integral square-(−2) roots in RQT-198's index-64 candidate lattice.

Let Q=BᵀG_KB and H=BᵀG_K(Y−I)⁻¹B. With T8 the prior eight roots, the Wall constraints A=T8ᵀHᵀ have rank 8. A unimodular column reduction produces a **saturated integer kernel of rank 13** with pivot diagonal (1,1,1,1,1,1,1,1). Its restricted Gram determinant is **112630007601408**.

An exact ninth root in the RQT-198 basis:

```
[2,-21,-111,8,14,8,30,38,116,23,-1,-5,34,54,18,0,-42,-30,56,-40,45]
```

Its original 22-coordinate vector:

```
[-48,-97,-88,-111,8,14,8,30,38,116,51,10,-5,34,54,18,-16,-42,-30,56,-35,45]
```

The root was recovered from the saturated-kernel LLL-reduced coordinates

`[-45,3,10,-1,44,27,22,36,-34,22,12,-28,-22]`.

**Exact checks:** square −2; orthogonal to h; satisfies all prior eight one-sided Wall equations; the nine roots are independent; the nine-root Wall matrix remains upper-unitriangular. The final Wall column is

`[8,-4,4,-50,846,-1285,-81,-15,1]`.

The corresponding reflection preserves the original Gram form, fixes h, squares to identity and is integral.

**Status:** ninth integral Wall-compatible root **PROVED**. Twelve further roots remain to reach 21. A full 21-reflection product and minimality of 21 versus 23 remain **OPEN**.

**Reproduce:** `research/rqt/rqt209_verify.py`, using the original matrices plus RQT-198, 201, 203, 204, 205, 207, 208 reports. The standalone evidence bundle contains all inputs, the executable verifier, and the exact JSON report.

**RQT-210:** extend the nine-root flag using a saturated rank-12 Wall kernel, checking for a tenth exact integral root.
