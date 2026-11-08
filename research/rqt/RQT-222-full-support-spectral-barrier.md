# RQT-222 — Full-support and spectral-gap invariant

**2026-11-07 | Exact original-source certificate PASS.**

Use the RQT-216 saturated rank-six Wall kernel with reduced Gram F, reconstructed exactly by
`F = Z.T * B.T * K.T * G * K * B * Z`
from original RQT-122 Gram G, RQT-133 operator X, RQT-198 B and integer kernel Z. det F = −313982794406122741723132503868.

**Full-support theorem.** For each coordinate j=0,...,5 let F_j be the five-dimensional principal submatrix obtained by omitting j. All 30 leading principal minors of `−F_j − 10928*I_5` are strictly positive (certified exact integers and provided in the RQT-222 report). By Sylvester, all six such matrices are positive definite. Therefore for every nonzero integer vector x with at least one zero coordinate,
`x.T F x < −10928 * (x.T x) ≤ −10928.`
It follows that **any integral vector of square −2 must have all SIX coordinates nonzero** in the frozen reduced basis. This is an unbounded theorem, not a finite-search claim. It is basis-specific.

**Exact signature and positive eigenvalue.** The negative-definiteness of each five-coordinate restriction gives at least five negative eigenvalues; det F<0 forces exactly one positive eigenvalue. Thus signature=(1,5) without floating-point analysis. The exact determinants are

```
det(F−13I) = −15740534870424877855390570819
det(F−14I) =   7207415819344600406943933164
```

These opposite signs and the five negative directions prove **13 < lambda_positive(F) < 14**.

**Status:** Exact source replay, 30 Sylvester minors, full-support root necessity, signature (1,5), and positive spectral gap PASS. The sixteenth integral root, 21-root product, and shortest reflection length 21 versus 23 remain OPEN. The new theorem explains the failure of sparse searches; it neither produces a root nor proves global nonrepresentability.

**Reproduction:** The complete original-source RQT-222 ZIP contains the executable `rqt222_full_support_barrier.py`, all inputs and `RQT-222-report.json` with the thirty exact minors and checksums.

**Next RQT-223:** Search on the near-isotropic full-support cone, e.g. hyperbolic parametrization or an exact integral orbit method.