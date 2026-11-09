# RQT-251 — Uniform binary backbone lifting

**2026-11-08. Exact exhaustive arithmetic PASS.**

Preserve 17 certified integral norm−2 roots from RQT-241 Branch 2. The RQT-242 rank-four saturated Wall lattice has integral Gram F, unimodular Wall H, and **index-two** residual image. Do not conflate this image and its saturation.

**Theorem:** The 36 ordered complete four-root flags modulo two each have 512 complete modular flags modulo four. Of those 512, precisely **160** admit a four-column lift modulo eight with all four norms equal to −2 modulo 16 and all six lower one-sided Wall pairings vanishing modulo eight. **All 36 backbones survive.**

For a mod-four root column r, lift r→r+4e. The four norm congruences and six pairwise congruences linearize to 10 equations in 16 bits. Exhaustive exact GF(2) elimination of all 18,432 mod-four flags gives exactly **5,760** consistent flags, every consistent system having rank **7**. Hence each has exactly 2^(16−7)=**512** distinct mod-eight lifts.

```
binary backbones                        36
mod4 flags / binary backbone           512
mod4 flags passing mod8 lift / backbone 160
consistent mod4 systems              5,760
GF2 rank for every consistent system     7
mod8 lifts / consistent mod4 flag      512
total complete mod8 flags         2,949,120
mod8 flags / binary backbone        81,920
```

Every one of the six position patterns for two forced d=2 roots occurs exactly **960** times among the consistent mod-four flags and **491,520** times among all mod-eight flags. Exactly **40** first-root residues modulo four occur.

**Explicit witness** as four columns in the frozen rank-four coordinates:
```
(4,5,5,1)
(1,4,6,1)
(5,0,3,3)
(1,1,1,3)
```
All norms =−2 mod16; all ordered lower Wall pairings 0 mod8; determinant odd.

Independent `rqt242_verify.py` original-residual replay and `rqt251_verify.py` exhaustive GF2 replay passed in the conversation evidence archive `RQT-251-uniform-binary-lift-evidence.zip`. The ZIP contains source 22×22 matrices, RQT-241 witness, frozen rank-four basis/Wall/Gram, runnable scripts, full per-backbone census and logs, SHA256 manifest.

**OPEN:** ordinary integral eighteenth root; roots 19–21; full exact 21-reflection factorization. These modular counts are not an integral factorization, nor proof of infinite 2-adic lifting.

**Next RQT-252:** higher binary backbone lifting and explicit global integral root construction.
