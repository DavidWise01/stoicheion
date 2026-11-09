# RQT-254 — Independent unimodular height obstruction

**2026-11-08 | Exact integer audits PASS; integral root18 OPEN.**

Preserve 17 exact integral roots (RQT-241 Branch 2), and the RQT-242 saturated rank-four Gram F and Wall H. RQT-247's global existence theorem remains valid; this test excludes only a finite domain.

Exact unimodular row basis:
```
T =
[  31    4  -31  -18]
[-100  -13  100   58]
[  -9   -1    9    5]
[ 336   43 -335 -195]
```
det(T)=−1, J=T F Tᵀ, and x=Tᵀy where x is the frozen original rank-four coordinate vector. The reduced Gram J is:
```
[9208923577999086,-2890579252927294,-1029318396906446,276003667781247]
[-2890579252927294,-136287821825501156,-29512715198402862,11299357575842588]
[-1029318396906446,-29512715198402862,-1127313935375881122,-146309554088173376]
[276003667781247,11299357575842588,-146309554088173376,-5868287405277328266]
```

The first new reduced coordinate equals **y0=−24x0−22x1−17x2−17x3**, exactly. The lower-right negative Gram has a positive-definite opposite, giving a rigorous Schur cone for both exact norms −2 and 0.

For **all positive integer y0 from 1 to 1000**, an independently verified script generated outward exact rational bounds for y1 and y2. Their total is **33,614,572 candidate pairs**. In each, the fourth coordinate y3 is solved via exact 256-bit integer discriminant-square/divisibility tests, **without a bound on y3**. The same bounds enclose both the norm−2 and norm0 cones.

Executed, independently verified logs:
```
NORM -2: TOTAL 33614572 FOUND 0
NORM  0: TOTAL 33614572 FOUND 0
```

Because y0=0 is impossible for any nonzero isotropic or norm−2 vector (negative-definite transverse section), and negative y0 is covered by central symmetry, **every integral norm−2 vector and nonzero integral isotropic vector must satisfy**
```
|24x0+22x1+17x2+17x3| >= 1001.
```
This is a **second independent finite-height exclusion** alongside RQT-244's **|x0|>=10001**. It does not contradict global existence and does not prove global nonrepresentation.

The exact downloadable RQT-254 archive contains frozen RQT-242 source data, original and reduced Gram, the unimodular transform, rigorous cone-bound generator `prepare.py`, independently replayed checker `verify.py`, exact Boost C++ discriminant searches for both norms, 1000-slice bound file, executed search logs, zero-witness files, summary, and SHA256 manifest.

**NEXT RQT-255:** construct an explicit primitive integral isotropic vector beyond both height barriers using an exact rational quadric solver, apply Bézout to build root18 and verify the rank-three residual.
