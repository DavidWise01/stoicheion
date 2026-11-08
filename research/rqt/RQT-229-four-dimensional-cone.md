# RQT-229 — Exact rank-four cone, orthant and 25,000-slice exclusion

**2026-11-08 | Original-source exact verification**

Preserve the seventeen previously certified integral Wall-compatible roots. In RQT-228's saturated rank-four kernel with even Gram F, an eighteenth root must be an integer x with xᵀFx=−2. The determinant is **−7154513768473386414464298429235934347540076220** and signature (1,3).

Set t=x[2], z=(x[0],x[1],x[3]), P=−F[[0,1,3],[0,1,3]], b=F[[0,1,3],2], v=P⁻¹b, beta=F[2,2]+bᵀP⁻¹b. The **exact rational identity**

`xᵀ F x = beta*t² − (z−v*t)ᵀP(z−v*t)`

holds, with P positive definite and beta>0. The exact rational center v≈(0.6723912186003367, 0.373384400663929, 0.36621672399264504). The exact inequalities `v[i]² > (beta+2)*(P⁻¹)[i,i]` prove that any norm−2 integer vector must have one of only **two global sign patterns**: `(+,+,+,+)` for t>0 or `(−,−,−,−)` for t<0. t=0 is impossible. These are unbounded, basis-specific necessities.

For **all integer t=1,...,25000**, exact rational ellipsoid bounds generate outward-rounded integer ranges for x[0],x[1]. Every integer pair was enumerated and an exact signed 128-bit integer quadratic discriminant test solved the final coordinate x[3] **with no bound**. The completed C++ run reports:

```
TOTAL 152127128 FOUND 0
```

Central symmetry covers negative t, t=0 is impossible, so **any eventual integer norm−2 root must satisfy |x[2]|≥25001**. This is a *certified finite-domain exclusion*, NOT a global obstruction or proof of nonrepresentation.

Exact SymPy replay verified source X/G, index-64 basis, earlier saturated kernels and all 17 one-sided Wall constraints, cone identity, and the bound metadata. The complete archived evidence ZIP supplied in the conversation contains both original matrices, prior root reports, exact `cone.json`, 25,000-slice `bounds.txt`, `build_bounds.py`, `search.cpp`, `verify229.py`, result log, and source checksums.

**PASS:** preserved 17-root flag, exact hyperbolic cone, global sign theorem, complete slice enumeration. **OPEN:** eighteenth integral root; roots 19–21; 21-reflection equality; minimal word length 21 or 23.

**Next RQT-230:** exploit the near-isotropic cone arithmetically, by integral-orbit methods or continued-fraction/congruence sieving beyond the finite search.
