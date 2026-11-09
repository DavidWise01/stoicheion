# RQT-250 — The 36-flag binary backbone

**2026-11-08 — Exact integer audit PASS.**

Preserve RQT-241's 17 explicitly certified integral roots. Work in the RQT-242 saturated rank-four residual Wall lattice with Gram F4 and integral unimodular Wall H4; keep distinct its index-two residual image.

Exact reductions modulo 2:

```
F4 mod 2          H4 mod 2
0 0 1 1           0 1 1 1
0 0 0 0           1 0 1 1
1 0 0 1           0 1 0 1
1 0 1 0           0 1 0 0
```

Enumerate all 16 binary vectors. Exactly **8** satisfy `rᵀH4r=1 mod2`; among those exactly two are radical `F4r=0 mod2`, the parities `(1,0,1,1)` and `(1,1,1,1)`.

Enumerate ordered 4-column flags of those 8 vectors under `r_jᵀH4r_i=0 mod2` for j>i. Exactly **36** flags exist. Each has odd determinant and **necessarily contains exactly those two radical parities**, each once. This proves that RQT-248's forced two-divisibility composition is already visible at the binary layer.

Next enumerate all 256 vectors mod4. Exactly **80** satisfy `rᵀF4r=−2 mod8`. The ordered Wall triangularity condition mod4 permits exactly **18,432** full flags. Reducing each flag mod2 gives one of the 36 binary flags. **Every binary flag has precisely 512 admissible mod4 lifts**, with no exceptional fiber:

```
36 × 512 = 18,432.
```

The six choices of the two radical positions each occur 3072 times among the mod4 flags.

**Certified:** exact binary flag classification, forced two distinct d2 parities, and uniform lifting multiplicity 512. **Not claimed:** an explicit integral root18 or a complete integral 21-reflection factorization.

The independently executed `rqt250_verify.py` and `RQT-250-report.json`, original Gram/operator, frozen rank-four matrices, root17 reference, source log, and SHA256 manifest are in the self-contained downloadable evidence ZIP.

**Next RQT-251:** intersect the 36 binary backbones with the mod8 continuation-compatible classes and seek a genuine integral eighteenth root.
