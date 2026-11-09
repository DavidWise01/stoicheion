# RQT-256 — First-reflection order-reduction invariant

**2026-11-08 | Exact reduced and original-source replay PASS**

Preserve the 17 explicitly certified integral norm−2 Wall roots of the RQT-241 Branch-2 prefix. The frozen RQT-242 saturated rank-four kernel has exact even integral Gram F4, unimodular Wall H4, and residual D4; the residual image has index two inside this saturated kernel.

There are exactly **eight norm-compatible binary root parities**. Exhaustive enumeration of all ordered four-root flags with lower one-sided Wall pairings zero modulo two gives exactly **36** binary flags. Only **five** of the eight parities can begin a complete flag:

| Parity | pairing d | complete binary flags beginning here | order of s_r D4 mod 2 | rank(s_r D4 − I) mod2 | admissible mod4 first-root residues after full mod8 gate |
|---|---:|---:|---:|---:|---:|
| 0011 | 1 | 0 | — | — | 0 |
| 0111 | 1 | 6 | 2 | 1 | 8 |
| 1001 | 1 | 6 | 2 | 1 | 8 |
| 1010 | 1 | 0 | — | — | 0 |
| 1011 | 2 | 9 | 3 | 2 | 8 |
| 1101 | 1 | 0 | — | — | 0 |
| 1110 | 1 | 6 | 2 | 1 | 8 |
| 1111 | 2 | 9 | 3 | 2 | 8 |

For every **actual** integer norm−2 root r in the residual lattice, its reflection is s_r=I+r(rᵀF4). If r mod2 is 0111, 1001, or 1110, then s_rD4 is a **nontrivial involution modulo two** and its binary moving rank is one. If the root parity is 1011 or 1111, then F4r=0 mod2 so s_r is identity modulo two, and s_rD4 retains the original order-three action and binary moving rank two.

This does not assert the existence of an explicit eighteenth root in any of the specified residue classes. Independently, for any actual exact norm−2 root, the rational moving rank drops 4→3 by the RQT-240 rank-one determinant identity.

**Higher lifting verification:** All 18,432 complete mod4 flags were audited by exact GF(2) equations. Exactly **5,760** admit a complete mod8 lift (norm mod16), distributed by first-root parity as **0111:960, 1001:960, 1011:1440, 1110:960, 1111:1440**. Exactly **40** distinct first-root residues mod4 occur, eight for each of the five viable binary parities.

**Evidence:** The conversation ZIP `RQT-256-first-reflection-order-reduction-evidence.zip` contains original 22×22 Gram/operator, frozen RQT-241 and RQT-242 certificates, `rqt256_verify.py`, original-residual replay `rqt242_verify.py`, machine-readable count table, execution logs and SHA256 manifest. Both replay tests passed.

**Status:** exact binary order-reduction and continuation gate proved; explicit integral root18, roots19–21 and complete 21-reflection equality remain **OPEN**.

**Next RQT-257:** target a genuine integral divisibility-one root18 with first parity 0111, 1001 or 1110, yielding simultaneous rational rank 4→3 and binary order 3→2. Then construct and test the rank-three successor.
