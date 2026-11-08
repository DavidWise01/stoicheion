# RQT-237 — Branch 2 exact binary-lift flag to modulus 1024

**2026-11-08 | Original source matrices independently reconstructed: PASS.**

Continue the first fifteen certified integral roots plus RQT-224 alternative root16, Branch 2 `(-232,-246,223,729,-473,-242)`, in the exact saturated rank-five Wall lattice with Gram F5 and unimodular Wall H5.

## Sharper first-root gate

- Of `4^5=1024` residues mod4, **272** satisfy `rᵀF5r≡−2(mod8)`.
- RQT-236's complete modular flag test obstructs **120** of these from starting a length-five ordered flag modulo4, leaving 152.
- The norm equation modulo16 supplies a separate necessary condition: `q(r+4e)=q(r)+8eᵀF5r+16eᵀF5e`, so a norm-compatible mod4 class can lift to a norm-compatible mod8 representative iff `q(r)≡−2(mod16)` already or `F5r≠0(mod2)`.
- Exactly **20** of the 272 fail this norm lift. All 20 are among the earlier 152 mod-four survivors, and none overlap the previous 120.
- Hence **132** mod-four first-root classes pass both necessary tests. This does not assert that every survivor extends to an entire flag at higher moduli.

## Explicit five-column flag mod 1024

The **columns** of the following matrix form the exact modular witness in the frozen branch-2 reduced basis:
```
[ 200   164   880    61   305 ]
[ 820   704   501   796   486 ]
[1004   366  1004   760  1023 ]
[1020     5  1021  1023  1020 ]
[1021  1017  1020     2     1 ]
```
Exact arbitrary-precision arithmetic proves `det(V)≡1(mod1024)`, all five norms `(VᵀF5V)_ii≡−2(mod2048)` and

```
VᵀH5V mod1024 =
[1 60 340 384 40]
[0  1 862 819 234]
[0  0   1 143 233]
[0  0   0   1 496]
[0  0   0   0   1]
```

Thus Branch 2's *entire five-reflection word* passes the specified triangular modular test through 1024, not merely the first root. The witness is generated deterministically by eight successive GF(2) lifts from the RQT-235 mod4 flag, with the degenerate radical norm condition enforced at each stage.

**Independent replay:** `rqt237_construct.py` regenerates this exact matrix, and `rqt237_verify.py` invokes the original-source 22x22 matrix verifier, reproduces the 272/120/20/132 count and checks modular determinant, five norms and ten lower Wall pairings. The downloadable 38-file self-contained RQT-237 ZIP contains these scripts, original matrices, historical root reports and exact result JSON.

**LIMITATION:** A flag modulo1024 is not an exact integral norm−2 flag, nor a proof of an infinite 2-adic lift. The genuine Branch 2 seventeenth integral root and full 21-reflection word remain OPEN. The RQT-236 complete finite search exclusion |x[0]|≤10000 also remains valid.

**RQT-238:** use the 132-class necessary sieve and the near-isotropic cone to construct a genuine integral seventeenth root or establish a global obstruction.
