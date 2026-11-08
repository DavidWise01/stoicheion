# RQT-235 — Eight-way sixteenth-root rebranch and exact mod-four gate

**2026-11-08 · original Gram/operator replay PASS.**

RQT-234 obstructs the *frozen seventeen-root* prefix; it does not rule out all 21-reflection words. Rebranch after the first fifteen certified roots using the eight exact RQT-224 sixteenth-root candidates (indexes 0–7).

For **every** candidate, original 22×22 verification establishes:
- a primitive additional Wall equation (gcd 1), producing a saturated rank-five integral residual kernel;
- residual moving rank **5**;
- the integral image of residual-minus-identity equals this kernel, with Smith invariants **(1,1,1,1,1)**;
- its reduced integral Wall form `H5=F5(D5−I)⁻¹` equals restriction of the original H and has determinant **1**.

Therefore any completion by five integral norm−2 reflections must give an ordered 5-column flag modulo 4, with each root norm `−2 mod8`, lower Wall pairings `0 mod4`, and an automatically odd determinant.

| RQT-224 root16 choice | Root residues | Compatible ordered pairs | Compatible ordered triples | Complete 5-flag mod4? |
|--:|--:|--:|--:|:--:|
| 0 (old) | 288 | 19,456 | 311,296 | YES |
| 1 | 192 | 8,192 | 65,536 | **NO** |
| 2 | 272 | 17,920 | 281,600 | YES |
| 3 | 272 | 17,920 | 281,600 | YES |
| 4 | 272 | 17,920 | 281,600 | YES |
| 5 | 192 | 8,192 | 65,536 | **NO** |
| 6 | 256 | 15,360 | 172,032 | **NO** |
| 7 | 272 | 18,432 | 313,344 | YES |

**Obstruction theorem:** branches **1, 5 and 6** have zero compatible ordered quadruples modulo 4, hence cannot finish in five further integral square−2 reflections. Since rank=5 and residual determinant −1, any completion preserving one of these 16-root prefixes would require **at least seven** more reflections (at least **23 total**), if any integral completion exists.

**Modular survivors:** branches **0, 2, 3, 4, 7** each have a certified complete five-root mod-four flag. Passing the modular gate is only a necessary condition; it is **not** an actual 21-root factorization.

The historical seventeenth root from RQT-227 has the correct one-sided Wall pairing only with root16 choice **0**; the resulting particular seventeen-root flag is obstructed by RQT-234. A different seventeenth root is needed even if choice 0 is retained.

**Branch 2 is the next target.** Its 16th root in the RQT-216 rank-six coordinates is `(-232,-246,223,729,-473,-242)`. Its saturated rank-five Gram determinant is `312669187727137013416789354039323478` (smallest absolute determinant among all eight). A concrete ordered mod-four five-root flag has columns

```
[0 0 0 1 1]
[0 0 1 0 2]
[0 2 0 0 3]
[0 1 1 3 0]
[1 1 0 2 1]
```

The exact Wall matrix of these five columns modulo four is

```
[1 0 0 0 0]
[0 1 2 3 2]
[0 0 1 3 1]
[0 0 0 1 0]
[0 0 0 0 1]
```

Every column norm is 6 modulo 8, and the column determinant is odd. This is **local arithmetic admissibility only**.

**Exact replay evidence:** the attached RQT-235 self-contained 38-file ZIP carries original source matrices, historical root reports, each reduced rank-five Gram/Wall/action and Smith certificate, eight modular branch reports, and the executable original-matrix verifier `rqt235_verify.py`.

**OPEN:** integral new root17 in a viable branch, roots18–21, full 21-reflection identity, minimal length21 vs23. **RQT-236:** use the branch-2 modular witness to guide a constructive integral root17 search.