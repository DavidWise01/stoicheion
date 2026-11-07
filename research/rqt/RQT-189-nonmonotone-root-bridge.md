# RQT-189 — A verified non-monotone root bridge

**2026-11-06 | Exact original RQT-122/133 matrices**

Following the 19-reflection partial factorization of RQT-188, let F19 be the residual isometry with rank(F19-I)=2 and image Gram diag(0,-6).

## The non-monotone bridge

Let u be the primitive integral isotropic vector spanning im((F19-I)^2):

```
u = [-4,-5,-5,-7,0,1,2,0,1,6,3,2,1,1,4,2,-1,-3,0,2,-1,4]
```

In the original basis, r=e20 and r+u are integral roots of square -2, both orthogonal to h. Define R_s=I+s(s^T G) for square -2 roots.

`F20 = R_e20 F19` and `F21 = R_(e20+u) F20`.

The **exact rational ranks** of F-I are **2 → 3 → 2**. Both reflections are involutive integral Gram isometries that fix h. The cumulative certificate reconstructs X from the previous 19 plus these two reflections followed by F21. The residual F21 is still nonidentity.

## An instructive change in the obstruction

The saturated rational image `V21=im_Q(F21-I)` has an integral basis with Gram form

```
[[0,0],
 [0,-8]]
```

The Smith form of this 22×2 image basis is (1,1), proving it is already saturated in Z^22. The quadratic form on V21 is `-8*y²`. It represents -2 rationally (y=1/2), but **not integrally** (y∈Z). Therefore there is no integral square -2 root in the rational image and no next strictly rank-reducing negative-root reflection at F21 either.

This illustrates that the earlier *rational* nonrepresentation obstruction can disappear under a nonmonotone bridge, while an *integral* obstruction remains.

## Exact test status
- 19 previous root reflections: verified.
- 2 nonmonotone bridge roots: verified.
- Rank bridge 2→3→2: verified.
- Residual image Gram and saturated Smith form: verified.
- Full reconstruction X=R1...R21 F21: verified.
- **Complete root factorization of X remains OPEN.**

## Reproduction
See `rqt189_nonmonotone_bridge.py`. It recreates all 21 reflections from the archived original X and Gram matrices and checks each identity over the integers.

## Next natural boundary
**RQT-190 — Eichler transvection and root-lattice congruence.** Identify the rank-two unipotent F21 as a lattice transvection, then seek a root-generated translation that cancels it. Do not equate monotone descent failure with nonfactorability.
