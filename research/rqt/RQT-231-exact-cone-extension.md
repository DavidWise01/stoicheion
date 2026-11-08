# RQT-231 — Exact four-dimensional cone search through pivot 50,000

**2026-11-08 | Original-source exact audit PASS**

Continue the 17-root Wall-compatible flag of RQT-227 and the saturated rank-four integer kernel of RQT-228. Any eighteenth root must satisfy xᵀF₄x=−2 with x∈Z⁴. The RQT-229 exact Schur decomposition establishes the global common-sign orthants (+,+,+,+) and (−,−,−,−), and the necessary pivot condition x[2]≠0.

**Extension of the exact finite search:** RQT-229 tested positive pivot slices 1–25000, examining 152127128 pairs, with zero roots. RQT-231 extends the identical exact cone-bounded integer-discriminant search through 50000, solving the fourth coordinate **without imposing a coordinate bound**:

| x[2] | Exact candidate pairs | Roots |
| --- | ---: | ---: |
| 25001–35000 | 251787368 | 0 |
| 35001–42000 | 284476220 | 0 |
| 42001–50000 | 460237476 | 0 |
| New total | **996501064** | **0** |
| Combined with RQT-229 | **1148628192** | **0** |

An independent exact rational SymPy script reconstructs F₄ from the original Gram/operator, RQT-198 index-64 lattice basis, the saturated intermediate kernels, and the 17 prior root vectors. It verifies all seventeen one-sided Wall constraints, recomputes the Schur-cone outward enclosures, confirms each exact segment count, and checks the empty witness files and complete C++ logs.

**Exact conclusion:** any integer norm−2 root in this frozen rank-four basis must satisfy **|x[2]|≥50001**. This bound is necessary, not sufficient. There is NO claim of global nonexistence or of a complete 21-root factorization.

**Status:** PASS original-source, exact cone-bound and new search audit. OPEN eighteenth integral root; roots 19–21; 21-reflection equality; minimal word length 21 or 23.

The complete 46-file standalone evidence ZIP accompanies this research result and includes original 22×22 matrices, root history, exact bounds for the three new segments, compiled-search source, search logs, empty witness outputs, and `rqt231_verify.py`.

**Next natural target RQT-232:** exploit lattice-orbit geometry or an arithmetic sieve to construct the first global integral root in the rank-four kernel, rather than simply widening the finite search again.
