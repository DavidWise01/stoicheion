# RQT-187 — Constructive negative-root factorization: six-reflection prefix

**2026-11-06 · Exact original-matrix audit**

The original RQT-133 integer action X (22×22) is an isometry of the original RQT-122 Gram form G. The primitive norm-4 invariant h defines K=h-perp of signature (2,19).

## Verified partial factorization

Set F0=X. Six explicit integral square-(−2) roots r1,...,r6 in K yield reflection matrices Rj=I+rj(rj^T G), and recursively Fj=Rj F(j−1).

Each root satisfies rj^T G rj=−2 and h^T G rj=0. Each Rj is an integral involution, determinant −1, fixes h and preserves G exactly. Exact rational ranks:
**rank(Fj−I)=21,20,19,18,17,16,15** for j=0,...,6.

Since Rj²=I, exact reconstruction is **X=R1 R2 R3 R4 R5 R6 F6**. The residual F6 is a nontrivial integral isometry; this is **not a full factorization of X**.

## Explicit root coordinates

Define the 21-coordinate orthogonal basis `k_j=e_{j+1}-e_0` for j=0,...,18 and `k_19=e_20`, `k_20=e_21`. The six roots are:

1. `r1=k19`
2. `r2=k20`
3. `r3=k8-k16+k20`
4. `r4=k5-k16+k19+k20`
5. `r5=k14-k17-k19-k20`
6. `r6=k7+k8-k10-k16+k20`

These were found from a bounded sparse-root exploration. A smaller search of one- through five-coordinate roots supplied candidate witnesses; the chosen six form a constructive decreasing-rank path. The rank-reduction condition and full matrix equalities are independently rechecked in the committed script, not inferred from the search.

## What is and is not proved

**Proved by exact arithmetic:** six original-lattice square-(−2) reflections; integer and isometry properties; strict rank descent; exact reconstruction with residual F6.

**Still open:** a complete factorization F6 into square-(−2) root reflections, whether X lies in the full root-reflection subgroup, and whether that subgroup generates the relevant character kernel. Failure of a bounded search is **not** an obstruction certificate.

## Reproduction

`python research/rqt/rqt187_root_factorization.py` (SymPy required). Reads the original matrix and Gram source in `research/rqt/source/` and writes `RQT-187-report.json`.

## Next natural boundary

**RQT-188 — Residual obstruction or continued descent.** Search for square-(−2) roots orthogonal to the newly fixed subspace of F6, enlarge bounded root radius, and test whether further reflection descent is possible; require a mathematically proven obstruction before any no-factorization claim.
