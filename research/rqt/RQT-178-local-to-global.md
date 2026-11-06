# RQT-178 — Local-to-Global Conjugacy (2026-11-06)

**Status:** Structural theorem within the RQT-155–177 hypothesis class; five canonical examples verified with exact integer arithmetic. **Not** a result for arbitrary integral representations or the still-unretrieved original 22×22 matrix.

## Hypotheses
An integer lattice M ≅ Z^22 has X^4=I, norm N=I+X+X²+X³ of primitive rank one, and an orbit e0 with N(e0)=h=(1,1,1,1,0^18). We use the integral block classification developed in RQT-171:

X ≅ C4 ⊕ (-1)^(20-2b-g) ⊕ R^(b-1-g) ⊕ H^g,

where 1≤b≤10 and 0≤g≤min(20−2b,b−1). Here C4 is the 4-cycle permutation, R=[[0,-1],[1,0]], and H=[[-1,0,0],[0,0,-1],[1,1,0]].

## The local-to-global result
**Within this classified family**, two such actions X and Y are integrally conjugate if and only if they have equal (b,g). Therefore rational equivalence plus equivalence over Z_2 is sufficient to establish equivalence over Z, provided the RQT-171 integral classification applies.

Parameters can be measured directly:
- b=(22−tr(X²))/4 (rational cyclotomic multiplicity).
- u=rank_F2(X−I).
- g=u−b−2 (2-adic gluing rank).

At odd primes, the order 4 of the cyclic group is invertible, so no additional gluing appears in this classified family. At p=2 the gluing rank g distinguishes the coupled H blocks. Since the classified global form is determined by (b,g), matching local invariants give a common integral normal form.

**Scope caution:** Local-to-global integral conjugacy fails for general lattices and rings. Here the conclusion depends on the special C4 module structure and the integral normal-form theorem; it is not an unrestricted local-global principle.

## Exact canonical checks
Five examples were checked using SymPy exact integer arithmetic:
| b | g | Smith (1,2,4,0) | mod-2 ranks D,D²,D³ |
|---:|---:|---|---|
| 1 | 0 | (3,18,0,1) | (3,2,1) |
| 5 | 0 | (7,14,0,1) | (7,2,1) |
| 5 | 2 | (9,10,2,1) | (9,4,1) |
| 5 | 4 | (11,6,4,1) | (11,6,1) |
| 10 | 0 | (12,9,0,1) | (12,2,1) |

Each canonical matrix passes X^4=I, rank(N)=1 and N(e0)=h.

## Reproducibility
See the companion script `research/rqt/rqt178.py`. It reconstructs the block matrices and checks the norms, Smith factors and modular ranks.

## Next boundary
**RQT-179 — Original Matrix Acquisition and Independent Audit:** retrieve the original 22×22 X, calculate b and g, verify all frozen identities, construct an explicit unimodular conjugator, and mark any counterexample instead of silently changing assumptions.

## Attribution
RQT research series; David Lee Wise / STOICHEION; published as a reproducible mathematical research note, not as externally peer-reviewed discovery.
