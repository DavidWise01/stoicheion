# RQT-223 — Exact Schur Cone, Orthant Rigidity, and Exhaustive Slice Exclusion

**2026-11-07 | Exact original-matrix audit PASS.**

Starting from the 15 exact roots of RQT-215 and the saturated 6-dimensional Wall kernel of RQT-216, let F denote its exact even integral Gram matrix. The next root must satisfy x∈Z⁶ and xᵀFx=−2.

## Exact cone identity

Let t=x[3] (zero-based) and z=(x[0],x[1],x[2],x[4],x[5]). Put P=−F[others,others], b=F[others,3], v=P⁻¹b, β=F[3,3]+bᵀP⁻¹b. The matrix P is positive definite by exact Sylvester minors, β>0, and

xᵀFx = βt² − (z−vt)ᵀP(z−vt).

The exact rational coefficient β is 78495698601530685430783125967 / 3114078605308829265576642505. The full exact center ray is in the attached certificate.

For a norm−2 vector, each coordinate obeys
(zᵢ−vᵢt)² ≤ (βt²+2)(P⁻¹)ᵢᵢ.

All five strict rational inequalities vᵢ²>(β+2)(P⁻¹)ᵢᵢ hold. For nonzero integer t, this forces the signs of all other coordinates to match vᵢt. At t=0 the form is strictly negative definite. Hence **every norm−2 integer vector has one of precisely two possible sign patterns**:

- t>0: (−,−,+,+,−,−)
- t<0: (+,+,−,−,+,+)

This is an unbounded global necessity in this frozen coordinate basis.

## Exhaustive exact cone search, |t|≤300

For every integer t=1,...,300, use the exact rational ellipsoid inequality to construct outward-rounded integer coordinate intervals containing **all** possible norm−2 candidates for that t. The full table is bundled. The exact int64 C++ evaluator checked every candidate:

```
CERTIFIED_CASES 13521104 ROOT_COUNT 0
```

Every coordinate product fits signed 64-bit for the frozen intervals. By central symmetry, negative t is covered as well; t=0 is analytically excluded. Thus **any integer norm−2 root must satisfy |x[3]|≥301**.

**Status:** exact global sign theorem PASS, certified bounded-coordinate exclusion PASS, 15-root prior certificate preserved. **OPEN:** integral sixteenth root, full 21-reflection equality, minimal length {21,23}. The finite exclusion does not prove global nonrepresentation.

Reproduction: `rqt223_cone_certificate.py` and `search223.cpp`, original 22×22 matrices, index-64 basis, exact kernel Gram, and generated bounded table in the complete ZIP accompanying the conversation.

**RQT-224 target:** narrow-cone search beyond |x[3]|=300, or rigorous global root/obstruction.
