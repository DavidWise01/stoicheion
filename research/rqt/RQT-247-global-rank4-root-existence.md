# RQT-247 — Global existence of an integral eighteenth Wall root

**2026-11-08 | Exact arithmetic PASS; existence theorem, not explicit coordinates**

Preserve the RQT-241 Branch-2 prefix of **17 explicitly certified integral norm−2 Wall roots**. The RQT-242 saturated rank-four Wall kernel has integral even Gram F4, unimodular Wall H4 satisfying `H4+H4.T=-F4`, and moving residual D4 with `rank(D4-I)=4`. Its image is index two inside the saturated Wall kernel.

### Exact determinant and local isotropy

```
-det F4 = 8281492574115056973770683990411769007319047636247715225543944839911172
        = 2^2 * 3^2 * 4966811 * 140001169580740529
          * 330823854880640721967014002817981344723960683.
```

All three odd factors beyond 3 are distinct primes. The signature is (1,3).

For the integral quadratic polynomial `Q(x)=x.T F4 x/2`, smooth primitive isotropic classes are:
- modulo 2: `a=(0,0,0,1)`, `Q(a)=0 mod2`, `F4*a=(1,0,1,0) mod2`;
- modulo 3: `a=(0,1,0,1)`, `Q(a)=0 mod3`, `F4*a=(2,1,1,2) mod3`.

Hensel's lemma lifts both. At each of the three other determinant primes the Gram matrix has **rank three modulo p**, so the nondegenerate ternary portion has a nonsingular isotropic vector over Fp. At all other odd primes the Gram matrix has full rank four, which likewise guarantees nonsingular finite-field isotropy. Real isotropy follows from signature (1,3). The **Hasse–Minkowski theorem** yields a nonzero rational isotropic vector.

### Weak approximation forces primitive pairing-divisibility one

A smooth projective rational quadric with a rational point satisfies weak approximation. Choose a rational isotropic projective point simultaneously sufficiently close to the displayed primitive smooth Z2 and Z3 isotropic points. Scaling to a primitive integral vector `u` preserves both local unit pairing conditions:
```
u.T F4 u = 0; gcd(u)=1;
F4*u != 0 modulo 2 and modulo 3.
```
Set `d=gcd(F4*u)`. Extend u to an integer unimodular basis. The first Gram diagonal is zero and all other first-row/column entries are divisible by d; determinant expansion yields **d² divides det F4**. From the factorization d divides 6, while the imposed local unit conditions exclude 2 and 3; thus **d=1**.

Choose integer v with `u.T F4 v=1`, let `k=(v.T F4 v)/2` (integer because the lattice is even), set `w=v-k*u` and `r=u-w`. Then `u²=w²=0`, `u·w=1`, and **r.T F4 r=−2**. The integral unimodular hyperbolic plane U spanned by u,w splits:
```
L4 ≅ U ⊕ N2,
```
where N2 is even negative definite of rank two. Since `H4=F4(D4-I)^(-1)`, the exact rank-one determinant lemma implies any such norm−2 root reduces the residual moving rank **4→3**.

**Proved:** existence of an eighteenth integral norm−2 Wall-compatible root and an integral rank-reducing reflection. **NOT proved:** an explicit root18 vector, compatibility of that vector with RQT-243's 40 modular four-root completion classes, or existence of integral roots19–21 and equality of a 21-reflection product to the original operator.

### Evidence and references

The self-contained downloadable conversation archive `RQT-247-global-rank4-integral-existence-evidence.zip` includes frozen source matrices, prior certificates and residual data, `rqt247_verify.py`, exact numerical proof prerequisites, and verification log. It confirms determinant factorization, primality, matrix ranks, H4/D4 identities and smooth mod2/mod3 points.

External theorem references:
- Hasse–Minkowski: https://repository.uantwerpen.be/docman/irua/21c9b2/156147.pdf
- Weak approximation for smooth projective quadrics: https://www.aimath.org/WWN/qptsurface2/qptsurface2.pdf

**Next RQT-248:** constructive rank-four rational-isotropic solver to produce explicit u, v and root18; screen its mod4 class, then test the rank-three successor.
