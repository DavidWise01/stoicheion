# RQT-180 — Explicit six-block unimodular conjugacy certificate

**2026-11-06 · Executed against the original RQT-133 matrix, not a synthetic substitute.**

## Exact result
The original integer 22×22 matrix X satisfies

`P^-1 X P = C4 ⊕ H^6`

for a **constructed integer P with determinant +1**. The script reconstructs P reproducibly from the original source and checks all equations with exact SymPy arithmetic.

- `C4`: the rank-four cycle permutation matrix.
- `H=[[-1,0,0],[0,0,-1],[1,1,0]]`: the rank-three coupled block.
- Original matrix: `source/X-22x22.txt`, SHA-256 `f23bf0c7897bd89a6d3113cb72b6df9e61fbb1b1feaf6dbf50c2f0079138357c`.
- Conjugator text SHA-256: `b79c5edb3e13dd75572162efda344e2be5488537436e0ee105296d2f45fb7ed7`.

## Constructive algorithm
1. The orbit B=[e0, Xe0, X²e0, X³e0] has unit minor on rows (0,1,4,7).
2. Build an integer equivariant four-coordinate retraction to the orbit. Its unit minor uses columns (0,1,3,5).
3. Take an integral basis W for its rank-18 kernel.
4. With X_W the restricted action, choose seed indices (5,10,17,2,8,13). Each seed v generates the three vectors [v,-X_W(X_W+I)v,(X_W+I)v] that intertwine with H.
5. All six H-blocks form an integral residual basis of determinant +1.
6. Form P by concatenating B and the six H-blocks in ambient lattice coordinates.

## Evidence ledger
- det(P)=+1: PASS
- XP=P(C4⊕H^6): PASS
- P^-1 X P=C4⊕H^6: PASS
- NP=PNcan: PASS
- Smith(X-I)=diag(1^15,4^6,0): PASS

## Reproduction
`python research/rqt/rqt180_certificate.py`

The script writes `P-22x22.txt` and `RQT-180-report.json` locally. This note certifies integer representation equivalence; it does not establish any result about the general Hodge conjecture or upstream geometric assumptions.

## Next boundary
**RQT-181 — Reverse transport and provenance audit:** transport the original Gram form through P, verify integral isometry block relationships, and publish a reproducible certificate of the full form.
