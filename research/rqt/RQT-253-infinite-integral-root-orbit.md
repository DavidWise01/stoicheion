# RQT-253 — Infinite integral norm−2 root orbit and binary-complement invariant

**2026-11-08 | Exact source arithmetic and symbolic orbit verification PASS**

Preserve the 17 explicitly certified integral Wall roots of the RQT-241 Branch-2 prefix. Work inside the **saturated** rank-four RQT-242 Wall kernel, not its index-two residual image.

RQT-247 proved that this even integral lattice of signature (1,3) has a primitive integral isotropic vector of pairing divisibility one, hence splits integrally as `L4 ≅ U ⊕ N2` where `Gram(U)=[[0,1],[1,0]]` and N2 is even negative-definite rank2.

Exact determinant:
```
det(F4)=-8281492574115056973770683990411769007319047636247715225543944839911172
```
Write `Gram(N2)=[[-2a,c],[c,-2b]]`. Since `det(N2)=|det F4|` is divisible by4, c must be even. Set c=2k. The **binary complement** must have Gram `-2[[a,-k],[-k,b]]` with
```
a*b-k*k=2070373143528764243442670997602942251829761909061928806385986209977793.
```

Choose integral u,w spanning U with `u²=w²=0`, `u·w=1` and basis e1,e2 of N2 orthogonal to U. For arbitrary m,n∈Z, let `z=m e1+n e2` and
```
w_z = w+z-(z²/2)u
r(m,n)=u-w_z.
```
Since N2 is even, every vector is integral. Direct polynomial identities yield `w_z²=0`, `u·w_z=1`, `r(m,n)²=-2`, `r(m,n)·u=-1`. Thus every root is primitive and **pairing divisibility one**, and the map Z²→roots is injective by the e1/e2 coordinates.

Moreover the integral Eichler transvections
```
T_z(x)=x+(x·u)z-(x·z)u-(z²/2)(x·u)u
```
are Gram-preserving with determinant one and satisfy `T_z T_t=T_(z+t)`; `T_z(u-w)=r(m,n)`. Thus **an infinite Z² unipotent isometry orbit** supplies infinitely many eligible *norm-and-Wall-compatible* integral eighteenth roots. The RQT-240 rank-one determinant theorem implies every one reduces the residual moving rank 4→3.

**Important limitation:** u,w,e1,e2 have not yet been computed explicitly in the frozen rank-four coordinate basis. These are symbolic polynomial formulas **in an existential integral basis**, not explicit original-coordinate root18 witnesses. Neither membership in the 40 downstream completion-compatible mod4 classes nor integral roots19–21 or the complete 21-reflection word is established.

Verification: `rqt253_verify.py` symbolically proves norm, primitivity, group law, isometry and determinant; `rqt253_source_audit.py` verifies the frozen F4/H4/D4 identities and signature. Both executed successfully. The standalone conversation evidence ZIP includes these files, frozen RQT-242 matrices, and RQT-247 existence proof.

**RQT-254:** explicitly compute a U⊕N2 unimodular splitting basis, instantiate the polynomial family in the frozen coordinates, and screen for a root18 that permits integral roots19–21.
