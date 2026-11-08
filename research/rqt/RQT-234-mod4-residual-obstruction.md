# RQT-234 — Exact mod-four obstruction to four-reflection completion

**2026-11-08 | Exact source-matrix replay: PASS**

The ordered RQT-227 prefix has 17 certified integral norm−2 reflections. Set D=P17^(-1)X. RQT-233 established that the integer image of D−I is precisely the primitive rank-four Wall-kernel lattice L4, with Gram F4 and integral isometric action D4.

The residual Wall form H4=F4(D4−I)^(-1) satisfies H4∈GL4(Z), det H4=1, H4+H4^T=−F4. The correct orientation uses (D4−I), not (I−D4).

Exact H4 mod 4:
```
[1,0,3,0]
[1,1,2,0]
[0,3,0,1]
[2,3,0,2]
```

**Necessity:** Suppose D=s(r1)s(r2)s(r3)s(r4) with integral square−2 roots. As rank(D−I)=4, the four normals span im_Q(D−I). Primitivity of the image and the inclusion im_Z(D−I)⊆ΣZ r_i imply that the four roots form a unimodular basis of L4. In that ordered basis H4 must be upper-unitriangular, hence each root has norm −2 mod8 and all lower Wall pairings vanish mod4.

**Complete finite modular census:** Iterate all 4^4=256 vectors v modulo4, retain those with v^T F4 v≡−2 (mod8). There are exactly **64**. The exact one-sided modular pairing gives **768 ordered compatible pairs**, but **0 ordered compatible triples**. Therefore four ordered integral roots cannot exist for this residual, independently of coefficient bounds.

**THEOREM:** This *specific* frozen 17-root prefix cannot be completed to a 21-reflection word using only four more norm−2 integral reflections. The residual determinant is +1 and moving rank4, so any integral reflection decomposition of this same residual, if one exists, must have even length **at least six**. Thus a continuation preserving the prefix needs at least **23** total reflections.

**CAUTION:** This does **not** rule out a different 21-reflection factorization of the original operator X; global minimal length remains unresolved. Nor does it prove existence of a six-reflection decomposition of this residual.

The self-contained RQT-234 evidence ZIP contains original 22x22 Gram and operator, all prior root reports, `rqt233_verify.py` reconstructing D4 and F4, `rqt234_verify.py`, and `RQT-234-report.json`.

**Next RQT-235:** change the 17-root prefix if targeting 21, or seek an integral six-reflection residual decomposition when preserving it.
