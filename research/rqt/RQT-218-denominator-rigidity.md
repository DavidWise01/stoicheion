# RQT-218 — Exact rational-root denominator rigidity

2026-11-07. Continue the RQT-215 fifteen-root flag and the RQT-216 saturated rank-six Wall kernel.

Let a=(0,0,2,0,1,-2)^T, d=1845=3²·5·41 and F the exact archived Gram matrix. Direct original-source calculation gives **aᵀ F a=−2d²**, so x=a/d is a rational norm−2 root satisfying the fifteen rational Wall constraints.

**Discriminant:** |det F| = 2²·19²·293·439·36919·115204693·397453583. Thus gcd(d,det F)=1.

**Pairing numerator:** F a = (1187012,257661,−392622,−821191,−2966076,1528365)^T, whose entries have gcd 1. Consequently pairings of x with the integral kernel have exact least denominator **1845**. The root x does not belong to its dual lattice. The additive extension L+Zx has index 1845 but has nonintegral pairings; it is *not* an integral overlattice.

**Original ambient numerator:**
```
(1626,528,2310,2035,-1136,-1462,-1460,998,140,815,-378,-563,-216,418,-1634,-1249,23,-173,-1546,924,-1398,-630)^T
```
The rational reflection R=I+vvᵀG/d² satisfies R²=I, RᵀGR=G and Rh=h, but the exact least denominator of its 22×22 entries is **3404025=d²**. Hence it is not an integral lattice automorphism.

**PROVED:** denominator rigidity of this *particular* rational root and obstruction to the naive adjoin/reflect promotion.

**OPEN:** whether some other integral norm−2 root exists in the rank-six Wall kernel, and whether a complete 21-reflection factorization equals X.

The self-contained RQT-218 archive includes original matrices, previous reports, the exact SymPy replay program and its generated JSON result.

**Next RQT-219:** investigate primitive integer orbits/spinor genera or find an explicit global integral root.