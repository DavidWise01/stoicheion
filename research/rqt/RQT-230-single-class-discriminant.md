# RQT-230 — Single eligible two-primary discriminant class

**2026-11-08 · Original-source exact verification PASS**

Preserve the 17-root Wall flag and the saturated rank-four integer Wall kernel of RQT-228. Its exact Gram determinant is **−7154513768473386414464298429235934347540076220** and its Smith diagonal is

`(1,1,2,3577256884236693207232149214617967173770038110)`.

The 2-primary discriminant group is `(Z/2)^2`. The order-two elements and their finite quadratic values modulo 2Z are:

| Parity vector | q | Eligible for a norm−2 root of pairing divisibility 2? |
| --- | --- | --- |
| (0,0,0,0) | 0 | no |
| (0,1,1,1) | 0 | no |
| **(1,0,0,1)** | **3/2** | **YES** |
| (1,1,1,0) | 1/2 | no |

Every primitive norm−2 vector must have pairing divisibility `d=1 or 2`. If `d=2`, its half-vector lies in the discriminant group with quadratic value `−1/2=3/2`; hence **the parity class (1,0,0,1) is the only eligible d=2 class**. The d=1 branch is still open.

Exact residue census (d1,d2): mod4 `(96,32)`; mod8 `(768,256)`; mod16 `(6144,2048)`. All 256 mod8 d2-compatible residues reduce to the single permitted parity class.

**2-adic lift:** Set a=(1,0,0,1), `r(t)=a+2t e3` with zero-based index. The exact norm equation is
`r(t)^T F r(t)+2 = 8(-1131077395607+664043305563t-3048260410782t²)`.
The derivative is odd; Hensel's lemma yields a unique 2-adic lift with `t ≡ 18233304022598118383 (mod 2^64)`, for which norm+2 vanishes modulo `2^67`.

The independent original-matrix replay proves all seventeen Wall constraints exactly and reproduces the finite quadratic form and 64-bit Hensel residue.

**PASS:** exact discriminant-class narrowing and 2-adic local representation.
**OPEN:** global integer norm−2 root eighteen, roots 19–21, 21-reflection product equality, minimum word length 21 or 23.

The downloadable RQT-230 evidence ZIP supplies original G/X, previous root reports, saturated basis mapping, executable `rqt230_verify.py`, and complete JSON results.

**Next RQT-231:** attempt global integral representation in the single d=2 parity branch and the remaining d=1 branch.