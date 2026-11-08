# RQT-241 — Explicit seventeenth integral Wall root (Branch 2)

**2026-11-08 | Exact original 22×22 matrix audit PASS.**

A major advance beyond RQT-239/240: construct the *actual integral root seventeen* instead of only proving its existence. Preserve the first fifteen certified roots and Branch 2's alternative integral root sixteen.

### Explicit isotropic/Bezout construction
In RQT-239's unimodular reduced Gram J, take

```
u = [240,45,-135,-545,786]
v = [12,-143,4,54,-9]
w = [39770729434332,7457011768792,-22371035306801,-90312698090381,130249138897389]
r = [-39770729434092,-7457011768747,22371035306666,90312698089836,-130249138896603]
```

Here `u^T J u=0`, `u^T J v=1`, `w=v−(v^T J v/2)u`, `w^T J w=0`, `u^T J w=1`, and **`r=u−w`, `r^T J r=−2`**. The constructive search fixed first four isotropic rational coordinates `(48,9,−27,−109)` and solved a perfect-square discriminant `2503623320²`; fifth rational coordinate `786/5` gives primitive u. The integer Bezout partner v is obtained by unimodular column reduction and LLL/nearest lattice vector.

In the frozen Branch-2 rank-five coordinates, **root seventeen** is

```
[-13112575205790704,-1524876051051881,5773881356966028,793591763582657,5944066936669398]
```

The exact original 22-dimensional ambient root is

```
[-81063977012102286234,-153892023405221254112,-132067200787998198463,-185245221115581814246,
 16383707096216432726,21120884186178917215,25625554797703072911,50078338891768650985,
 60508471858444630856,191699679577122427194,83293030118575271770,11417878305766798118,
 -6290320518382323831,44858867800146464867,82508336889992162559,27082442786787395429,
 -28264397546118826981,-71648763066825579167,-38992279547178481555,82886990690706539959,
 -51050518961627658773,81715467130859631337]
```

### Exact original-matrix verification
- All 17 roots integral and square−2, all 16 earlier one-sided Wall equations `b17ᵀ H b_i=0`.
- Full 17×17 Wall matrix upper-unitriangular, 17 roots linearly independent.
- Ambient root orthogonal to h and square−2 in the original G; reflection `I+r(rᵀG)` integral, involutive, G-preserving and h-fixing.

### Downstream modular gate
The actual root mod4 is `(0,3,0,1,2)`. An ordered complete modular flag beginning with it is

```
(0,3,0,1,2)
(0,0,0,0,1)
(0,0,2,1,1)
(1,0,0,3,2)
(1,2,3,0,1)
```

Each column has norm−2 mod8, lower Wall pairings 0 mod4 and the flag determinant is **3 mod4** (odd). This root therefore passes the modular completion gate; the four later *integral* roots are NOT constructed.

### Reproducibility
The conversation evidence bundle `RQT-241-explicit-seventeenth-integral-wall-root-evidence.zip` contains original source matrices, historical root reports, exact Branch 2 lattice, deterministic `rqt241_construct.py`, original-source `rqt241_verify.py`, report JSON, and complete search trace. Running both scripts produces the exact witness and PASS.

**RQT-242 natural target:** saturate this specific root17's rank-four Wall kernel, derive the residual, check the mod4 obstruction, and attempt root18. The 21-reflection equality and global 21-vs-23 minimality remain OPEN.
