# RQT-238 — Branch 2 cyclic discriminant and unique divisibility-two parity

**2026-11-08 | Exact original 22-dimensional source-matrix replay PASS.**

Continue fifteen certified Wall roots plus Branch 2's integral sixteenth root from RQT-224. The remaining saturated rank-five Gram matrix F5 has Smith invariants

`(1,1,1,1,312669187727137013416789354039323478)`.

Its discriminant determinant is `2 × 139801 × 7915189 × 646956613 × 218377739361227`. Therefore the finite discriminant group is cyclic and its 2-primary subgroup is `Z/2`.

There is exactly one nonzero radical parity class modulo2: **a=(0,0,0,0,1)**. The discriminant quadratic value of a/2 is **3/2 modulo 2Z**, matching norm−2 and pairing divisibility two.

Every integral norm−2 root r has pairing divisibility `d=gcd(F5 r)` dividing 2. For **d=2**, r must have parity a. There can be **at most one d=2 root in a unimodular ordered five-root flag**, since two roots with identical mod2 parity would make its column matrix singular modulo2.

Of the **132** mod4 first-root classes surviving RQT-237's independent completion and norm16 tests, exactly **120 have d=1** and **12 have d=2**.

**Exact 2-adic construction:** Let `r(t)=a+2t e0` with `e0=(1,0,0,0,0)`. Direct integer multiplication gives

```
(r(t)^T F5 r(t) + 2)/8
= -50401690 -162145929*t -165967762*t^2
```

The polynomial's derivative `-162145929-331935524*t` is odd for every t. Hence Hensel's lemma yields a unique 2-adic zero. Its residue modulo 2^128 is

```
216126377552887896659684962905481850670
```

Consequently `r(t)^T F5 r(t) ≡ -2 (mod 2^131)`. The same exact congruence holds under the original integral 22-dimensional lattice embedding; the first sixteen Wall constraints and h-orthogonality hold exactly.

**LIMITATION:** This is a 2-adic local root, *not* an ordinary integral norm−2 root; no exact integral seventeenth root or full 21-reflection word is claimed. The finite representative's norm defect is nonzero. The RQT-236 finite exclusion remains in force.

The attached standalone RQT-238 ZIP contains original G/X, previous root reports, saturated bases, the independent executable original-source verifier `rqt238_verify.py`, machine-readable report, and SHA256 checksums.

**RQT-239:** global integral realization using a rational isotropic construction or arithmetic group orbit, screened separately in the d1 and unique d2 branches.