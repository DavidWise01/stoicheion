# RQT-220 — Exact 2-primary discriminant form of the sixteenth-root kernel

**2026-11-07.** Sources: original RQT-122 Gram, RQT-133 action, RQT-198 index-64 lattice and the RQT-216 saturated rank-six Wall kernel.

Let F be the exact even integral rank-six Gram matrix. det F = −313982794406122741723132503868, and its Smith absolute diagonal is (1,1,1,1,2,156991397203061370861566251934). Thus its two-primary discriminant group D(F)[2] ≅ (Z/2Z)^2. The exact quadratic form is **〈−1/2〉⊕〈−1/2〉 modulo 2Z**.

The order-two classes [x/2] with F x even are:
- (0,0,0,0,0,0), q = 0;
- (0,0,1,1,0,1), q = 3/2;
- (1,1,0,1,0,0), q = 3/2;
- (1,1,1,0,0,1), q = 1.

The bilinear pairing matrix modulo Z, in this order, is
```
[0,   0,   0,   0  ]
[0,   1/2, 0,   1/2]
[0,   0,   1/2, 1/2]
[0,   1/2, 1/2, 0  ]
```

Any eventual integral norm−2 root r with pairing divisibility d(r)=2 has [r/2] of exact order two and q([r/2])=−1/2=3/2 mod2, so its class **must** be one of the two q=3/2 classes above.

Exact replay over all 8^6=262144 residues shows precisely 4096 norm−2 mod8 lifts with even pairings for each eligible class, hence 8192 in total. Both remain locally feasible.

**PASS:** original-source identity F=ZᵀBᵀKᵀGKBZ, two-primary finite quadratic module, orthogonal order-two generator classes, exhaustive mod8 counts. **OPEN:** the actual integral norm−2 root, both primitive root divisibility branches, root sixteen, and the full 21-reflection factorization. The discriminant classification is necessary but not sufficient for global integral representability.

See the standalone RQT-220 evidence bundle for the original 22×22 matrices, prior reports, exact program, and JSON measurements.

**RQT-221 next:** seek a genuine global integral root or establish a defensible spinor-genus/integral-orbit obstruction.
