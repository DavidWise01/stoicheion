# RQT-244 — Rank-four cone, exact finite exclusion and 2-adic root

**2026-11-08 | Exact original-source audit PASS.**

Preserved: RQT-241 Branch-2 prefix of 17 certified integral norm−2 Wall roots. Use RQT-242's saturated rank-four kernel, Gram F4 and unimodular Wall H4. Its moving residual image has **index two** inside this kernel.

## Exact global sign invariant

Write x=(t,z) with t=x[0], z=(x[1],x[2],x[3]). P=−F4[1:4,1:4] is positive definite, v=P⁻¹F4[1:4,0], beta=F4[0,0]+vᵀPv>0. Then xᵀF4x=beta*t²−(z−vt)ᵀP(z−vt). Exact rational inequalities v_i²>(beta+2)*(P⁻¹)_ii hold for each transverse coordinate. The center is approximately **(0.12736545326744117,−1.002090646513571,−0.5823883943583268)**. Therefore every global integral norm−2 root has signs **(+,+,−,−)** or **(−,−,+,+)**. t=0 is impossible.

## Completed finite exact search

For every t=1..10000, exact rational inequalities were outward-rounded to integer ranges for x[1] and x[2]. All **15,240,808** integer pairs were evaluated. The final coordinate x[3] was solved using an **unbounded arbitrary-precision integer quadratic discriminant-square and divisibility test** (Boost multiprecision C++). Executed log:

```
TOTAL 15240808 FOUND 0
elapsed 8.11
```

The negative t values are excluded by central symmetry; t=0 is impossible. Thus any integral root18 must satisfy **|x[0]|≥10001** in this basis. This is NOT a proof of global nonrepresentation.

## Pairing-divisibility and parity

F4 has Smith invariants `(1,1,2,4140746287057528486885341995205884503659523818123857612771972419955586)`. The order-two radical parities and their norms modulo 8 are `0000→0`, `0100→4`, `1011→6`, `1111→6`. Of RQT-243's **40** mod-four first-root classes that admit a full four-reflection flag modulo8, **24 have pairing divisibility one** and **16 have pairing divisibility two**. The d2 classes have parity 1011 or 1111.

## Explicit local first-root construction

Choose a=(0,1,1,5), the first column of RQT-243's actual complete ordered flag modulo8. Set r(t)=a+8t e2 (zero-based index2). Exact identity:

```
(r(t)^T F4 r(t)+2)/16
 = -14562385908299609109
 + 16793193759917226115*t
 - 21080344320033532160*t*t
```

The polynomial derivative is always odd; binary Hensel lifting yields a unique t mod 2^256:

```
93878330334900477488557551447004581630314366809978929771196499707722623893639
```

The resulting vector has norm **−2 modulo 2^260** while retaining its first-root residue modulo8. Its image in the original Branch-2 rank-five lattice satisfies all **17 previous one-sided Wall constraints exactly**, with the same norm congruence; the associated reflection squares to identity mod 2^260. **This is NOT an integral norm−2 witness.**

The 36-file self-contained conversation ZIP includes exact source Gram/operator, historical roots, Gram/Wall/basis data, original 22D replay, `rqt244_verify.py`, `rqt244_bounds.py`, `rqt244_search.cpp`, all 10,000 bounds, completed logs, report and SHA256 manifest.

**PASS:** original 17-root prefix, sign theorem, parity census, 2-adic construction, exact finite search. **OPEN:** integer root18, integral roots19–21, full 21-reflection product and global minimality.

**Next RQT-245:** arithmetic-guided global construction of an exact root18 within the two necessary sign orthants, screened by the 40 completion-compatible classes.
