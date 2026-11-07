# RQT-219 — Primitive integral root-divisibility dichotomy

2026-11-07. Continue the exact saturated rank-six Wall kernel from RQT-216 / RQT-218. The even integral Gram matrix F has determinant −313982794406122741723132503868. The candidate norm equation is xᵀFx=−2 over x∈Z⁶.

**Proved primitive:** If x=k y for k>1, then k² divides 2, impossible.

**Proved pairing divisibility:** d(x)=gcd(components of F x) divides xᵀFx=−2; therefore d∈{1,2}.

**Exact binary census:** Of the 64 binary coordinate classes, 30 have norm congruent −2 mod4 and odd pairing (the d=1 necessary branch); 2 have norm congruent −2 mod4 and even pairing (d=2 necessary branch). The latter are (0,0,1,1,0,1) and (1,1,0,1,0,0). The mod-2 radical contains 4 classes.

**Full mod4 census:** d1 1920, d2 128, total 2048 of 4096.

**Full mod8 census:** d1 61440, d2 8192, total 69632 of 262144.

**Conditional complement discriminant:** If a primitive norm−2 x with pairing divisibility d exists, then its integral orthogonal complement has |det| = 2|det(F)|/d², by the index [L:Zx⊕x⊥]=2/d. Thus d=1 demands determinant 627965588812245483446265007736 and d=2 demands 156991397203061370861566251934.

All counts were obtained by exact integer enumeration; the full verification script and original Gram/operator sources are in the conversation's RQT-219 evidence ZIP.

**Status: PASS** arithmetic dichotomy and congruence census. **OPEN** actual sixteenth integral square−2 root, subsequent roots, complete 21-reflection equality, and minimal length 21 vs23. Neither modular branch is proved globally representable.

**RQT-220:** investigate the two primitive integral root branches via valid quadratic-form orbit or spinor-genus techniques.
