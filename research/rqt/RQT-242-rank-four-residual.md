# RQT-242 — Rank-four residual survives the modular completion gate

**2026-11-08 | Exact original 22-dimensional matrix replay PASS.**

Preserve the **17 explicit integral Wall roots** on the Branch-2 path, including the RQT-241 constructive seventeenth root. In the frozen rank-five coordinates the eighteenth-root Wall constraint is

```
[2881138847081037894248,-3357377810365097181265,
 2406018307631401931478,781323253998555020064,
 3053035747518714853552] · x = 0.
```

The coefficients have **gcd 1**. Integral unimodular elimination and exact LLL give the full saturated rank-four basis (columns):

```
[  83818    45069  -235713  -69545]
[   4718   139330  -132564  192606]
[ -87723   221623   104270   -5559]
[-154383   -32986  -146890   19007]
[  34731   -55526    32082  276952]
```

Its reduced Gram determinant is **−8281492574115056973770683990411769007319047636247715225543944839911172**. The restricted integral Wall form is unimodular, `det H4=1`, and `H4+H4ᵀ=−F4`. Its reduction modulo4 is:

```
[2 1 3 1]
[3 2 1 1]
[2 1 0 1]
[0 3 2 2]
```

**Exact residual:** Set `D5=I+H5^-1 F5`, `s_r=I+r(rᵀF5)`, `R=s_rD5`. Then `rank(R−I)=4`, `RᵀF5R=F5`, and the induced integral 4x4 action `D4` preserves F4, with `F4(D4−I)^−1=H4` and `det D4=1`.

**Important correction to any analogy with RQT-233:** The integer image of `R−I` has **Smith invariants (1,1,1,2)** when expressed in the saturated kernel basis. Its **index is 2**; the residual image and saturated Wall kernel agree only over Q, **not integrally**.

**Complete mod-four completion census:** Of 4^4=256 residues, **80** satisfy norm−2 modulo8; **1,504** ordered pairs have zero lower Wall pairing modulo4; **9,216** compatible ordered triples and **18,432** ordered four-root flags exist. **All 18,432** flags have odd determinant. One example, with columns as ordered roots:

```
[0 1 1 1]
[1 0 0 1]
[1 0 1 1]
[1 1 3 3]
```

Therefore the RQT-234 mod-four obstruction **does not recur** for this exact seventeen-root prefix. Modular pass does **not** certify integral norm−2 roots or a four-reflection product.

**PASS:** original 17 roots, saturated rank-four kernel, residual action and restricted Wall identity, exact residue census.
**OPEN:** explicit integral root18, roots19–21, exact 21-reflection identity and 21-versus-23 minimality.

**Reproducible evidence:** the downloadable **RQT-242-rank-four-residual-mod4-evidence.zip** accompanies this turn with 37 files: original Gram/operator, prior roots, exact full rank-four basis and Gram/Wall matrices, source-matrix verifier, new 4x4 modular enumeration, result JSON and SHA256 manifest.

**Next RQT-243:** exploit the index-two residual image and modularly admissible four-root flags to construct an actual eighteenth norm−2 integral vector; test its rank-3 residual.
