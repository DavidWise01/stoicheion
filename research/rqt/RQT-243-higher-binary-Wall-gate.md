# RQT-243 — Exact higher-binary completion gate

**2026-11-08 | Original-source and complete finite GF(2) replay PASS**

Preserve RQT-241's **seventeen explicit integral Wall roots**. RQT-242's saturated rank-four Wall kernel has integral Gram F4 and unimodular Wall H4, with H4+H4ᵀ=−F4. The post-root residual image has index 2 inside the saturated kernel (Smith (1,1,1,2)); do not identify these lattices integrally.

**New exact sieve.** RQT-242 had 80 coordinate residues mod4 with norm −2 mod8, and 18,432 complete ordered four-column flags mod4. Enumerating all 4^4 vectors confirms only **64** of the 80 first-root residues lift the individual norm equation to −2 mod16. Requiring a full ordered four-root flag mod8 leaves only **40** mod4 first-root residues. Exactly **5,760 of 18,432** full mod4 flags admit at least one full mod8 lift.

**Proof method:** For each mod4 flag vectors r_i, lift r_i→r_i+4e_i with 16 binary unknowns. The four norm congruences mod16 and six lower Wall congruences mod8 become a 10×16 GF(2) linear system. Exhaustively check consistency by exact binary Gaussian elimination for all 18,432 flags. No numerical approximation or random sampling enters the count.

**Explicit modular witness:** The following matrix has columns representing four modular roots:
```
V =
[ 53  73 105  21]
[ 16   6  77  81]
[ 90 119  89 119]
[  5  57 101  22]
```
Exact checks: `det(V) ≡ 1 (mod128)`, every column norm `−2 (mod256)`, and
```
Vᵀ H4 V (mod128) =
[1 70 90 121]
[0  1 60  98]
[0  0  1  30]
[0  0  0   1]
```
This is a **local modular** flag, NOT four exact integral norm−2 roots. There is no claim of an infinite 2-adic lift.

The standalone ZIP `RQT-243-higher-binary-Wall-gate-evidence.zip` includes exact F4 and H4 from RQT-242, `rqt243_verify.py` with complete exhaustive GF2 replay, the exact 40-class whitelist, the actual RQT-241 original 22-dimensional source replay and source Gram/operator. Reproduced output:
```
PASS: 80 mod4 roots; 64 with norm mod16 lift; 40 with complete mod8 flag
PASS: 18432 mod4 flags; 5760 lift to mod8; witness mod128 exact
```

**OPEN:** actual integral root18, roots19–21, full 21-reflection product equality.

**Next RQT-244:** target integral root18 only in the 40 permitted first-root classes; inspect global rank-four arithmetic/odd-prime conditions and explicit root construction.
