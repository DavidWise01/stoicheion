# RQT-190 — Eichler transvection and a complete ambient root factorization

**2026-11-06 · Original RQT-122 Gram / RQT-133 order-four operator.**

## Exact result

A 25-reflection certificate has been constructed and verified against all 484 entries of the original 22×22 matrix:

`X = R_(r1) R_(r2) ... R_(r25)`, where every `rj` is an **integral vector of square −2 in the full ambient lattice M** and `R_r=I+r(r^T G)`.

The complete product equals X exactly; applying all 25 reflections to X on the left returns the identity. **Important distinction:** the first 21 vectors belong to `K=h^perp` and individually fix h. The final four ambient roots have h-pairings `(−4,−4,+4,+4)`; they do *not* individually fix h, although their combined product does. Therefore **a full root factorization inside the stabilizer O(M)_h remains OPEN**. This note does not assert one.

## Construction

RQT-187 and RQT-188 give 19 certified K-root reflections, leaving a rank-two unipotent residual. RQT-189 gives a non-monotone two-reflection bridge with residual F21 and rank sequence 2→3→2.

For the residual F21, let `D=F21−I` and choose the primitive isotropic `u` as the first columnspace generator of D, with `<e7,u>=1`. Set `a=D e7`. Exact arithmetic verifies `u²=0`, `<u,a>=0`, `a²=−8` and

`F21 = T(u,a)`,

where the Eichler transvection acts by

`T(u,z)=I + z(u^T G) − u(z^T G) − (z²/2)u(u^T G)`.

The following **ambient** vectors sum to a:

```
r = -e0 - e1 - e2 - e12 + e20
s = a - r
```

Exact checks: `r²=s²=−2`, `<r,u>=<s,u>=0`, `<r,s>=−2`, `<r,h>=−4`, `<s,h>=+4`.

Thus

`T(u,a)=T(u,r) T(u,s)`

and, by the root transvection identity,

`T(u,r)=R_(r+u)R_r`, `T(u,s)=R_(s+u)R_s`.

This produces the last four roots `(r+u,r,s+u,s)`. The full 25-reflection product is checked exactly against the original X.

## Certification boundaries

- Exact integer root norms: **25/25 PASS**
- Exact Gram isometries: **25/25 PASS**
- Exact equality to original X: **PASS**
- Residual after all 25 reflections: **I**
- Roots individually fixing h: **first 21 only**
- Full factorization in O(M)_h using only K roots: **OPEN**
- Minimality of 25 factors: **not claimed**

This resolves the ambient root-factorization question for this particular X, not the stronger K-root reflection-generation problem or any general Hodge conjecture.

## Reproduction

Use `research/rqt/rqt190_eichler_full_factorization.py` (SymPy) with the archived source matrices at `research/rqt/source/X-22x22.txt` and `research/rqt/source/gram-22x22.txt`. The script produces an exact 25-root JSON certificate.

## Next natural boundary

**RQT-191 — Stabilizer-preserving root factorization.** Determine whether the Eichler translation vector can be decomposed into roots in `u^perp∩h^perp` and, if not, characterize the resulting arithmetic obstruction. Do not confuse the ambient product with a stabilizer-only product.
