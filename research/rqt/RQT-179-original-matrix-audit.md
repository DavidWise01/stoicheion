# RQT-179 — Original Matrix Acquisition and Independent Audit

**Date:** 2026-11-06. **Evidence level:** exact computational audit on the original 22×22 integer operator from RQT-133.

## Original source and provenance
- Archived original: `research/rqt/source/X-22x22.txt`
- Origin: RQT-133 geometric Fermat/Pham-cycle transport artifact.
- SHA256 of the original text file: `f23bf0c7897bd89a6d3113cb72b6df9e61fbb1b1feaf6dbf50c2f0079138357c`
- The original RQT-133 script builds the operator using RQT-121 and RQT-132 dependencies, with a Gram-matrix isometry assertion. This audit checks the operator, not the upstream geometry.

## Computed exact integer results

| Invariant | Value |
|---|---|
| Matrix shape | 22×22 |
| det(X) | -1 |
| X^4=I | PASS |
| Norm N=I+X+X²+X³, rank | 1 |
| N(e0)=(1,1,1,1,0^18) | PASS |
| Xh=h | PASS |
| Rank_Q(X-I) | 21 |
| tr(X) | -6 |
| tr(X²) | -6 |
| b=(22-tr(X²))/4 | **7** |
| rank_F2(X-I) | 15 |
| rank_F2((X-I)²) | 8 |
| rank_F2((X-I)³) | 1 |
| g=rank_F2(X-I)-b-2 | **6** |
| SNF(X-I) | diag(1^15,4^6,0) |
| SNF([e0,Xe0,X²e0,X³e0]) | diag(1,1,1,1) |
| Orbit saturation index | 1 |
| Coinvariant torsion | (Z/4)^6 |

## Interpretation and limits

The measured parameters are (b,g)=(7,6). Under the **RQT-171 integral block-classification theorem**, the proposed global normal form is **C4 ⊕ H^6**, with no pure sign or pure rotation blocks. This is compatible with all calculated invariants.

**Not yet independently certified:** an explicit unimodular 22×22 P satisfying XP=P(C4 ⊕ H^6). The above invariant checks are not a substitute for that concrete certificate. Also not audited here: the upstream geometric origin of the RQT-133 matrix or any general Hodge conjecture.

## Reproduce
Run `python research/rqt/rqt179_independent_audit.py` after installing SymPy. The script reads the original source and verifies all entries exactly.

## Next natural boundary
RQT-180 — Construct an explicit integral conjugator for the actual matrix, with determinant ±1 and full transport certificates.
