# RQT-255 — Order-three binary residual and reflection-product theorem

**2026-11-08 | Exact integral-matrix modulo-two audit PASS**

Preserve seventeen certified integral norm−2 Wall roots on RQT-241 Branch 2. The RQT-242 residual operator D4 acts on the saturated rank-four Wall kernel with Gram F4; its image is index two in that saturated kernel.

The exact binary residual is
```
D4 mod 2 =
[0 0 0 1]
[1 1 1 0]
[1 0 0 0]
[0 0 1 0]
```
It has **order three**: D4^3=I mod2, D4≠I mod2.

The radical of F4 mod2 is
```
(0,0,0,0)
(0,1,0,0)
(1,0,1,1)
(1,1,1,1)
```
D4 fixes the radical pointwise. With quotient basis e0 and e2, D4 induces
```
[0 1]
[1 1]
```
on the nondegenerate two-dimensional symplectic quotient, an order-three element of Sp(2,F2)≅S3.

Every pairing-divisibility-two root belongs to the binary Gram radical, so its integral norm−2 reflection `I+r(rᵀF4)` is the **identity modulo two**. The two d2 root parities must be exactly (1,0,1,1) and (1,1,1,1). The two d1 reflections provide the two nontrivial quotient transvections, whose ordered product is D4's order-three action.

**Conceptual exact count:** 6 selections of the two d2 positions × 3 ordered nonradical quotient-reflection pairs × 2 orders of the distinct radical vectors = **36** binary four-reflection flags. Independent enumeration confirms 36 binary flags, 6 for each position pattern, 3 ordered nonradical pairs, and **the product of all four binary reflection matrices equals the actual D4 mod2 for every one of the 36 flags.**

This is a stronger residual-specific invariant than Wall triangularity alone; it also explains the previously enumerated 36 backbones.

**OPEN:** explicit integral norm−2 root18, integral roots19–21 and original 21-reflection equality. All checks above are modulo two; no global integral completion follows.

The downloadable RQT-255 archive contains the exact RQT-242 frozen Gram/Wall/residual data, independently executed Python verifier, resulting report JSON, and SHA256 manifest.

**RQT-256:** use the quotient transvection orientation to target an actual integral d1 root18, derive its rank-three residual and test the three remaining reflections.