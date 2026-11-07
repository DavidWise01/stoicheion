# RQT-217 — All-prime local solubility, exact rational witness

**2026-11-07 | RQT-216 saturated rank-six Wall kernel.**

Preserve the fifteen RQT-215 roots. The next root must be an integral vector x in the six-dimensional saturated kernel satisfying xᵀ F x = −2, where F is RQT-216's exact reduced Gram matrix.

## Exact rational witness

Take a=(0,0,2,0,1,−2). The exact norm is aᵀ F a = −6,808,050 = −2·1845². Therefore x=a/1845 is a rational square−2 vector, and the archived independent audit maps it through the saturated kernel to the original 22-coordinate lattice, verifying all fifteen Wall constraints and norm−2. **This is not an integral root.**

## Smith certificate

Exact Smith normal form of F:
`diag(1,1,1,1,2,156991397203061370861566251934)`.

At every odd prime p, rank(F mod p)≥5. Nonsingular quadratic forms of dimension≥3 over odd finite fields represent every residue, with nonsingular lifts; hence −2 is represented over Z_p for **every odd prime**.

## Explicit 2-adic lift

For x=e₀+t e₂, the equation xᵀ F x=−2 is
`f(t)=−234390+178351t−426914t²=0`.
f(0)=0 (mod 2), and f'(t)=178351−853828t is always odd, so Hensel lifting gives a 2-adic solution. The exact verified residue is `t≡4727422553192030530 (mod 2^64)`; it satisfies the root norm congruence modulo 2^65.

## Conclusion

**PROVED:** rational representation of −2; real representation; representation over Z_p for every prime p, plus original Wall-kernel mapping. **OPEN:** exact integral representation of −2; sixteenth integral root; full 21-reflection word and length minimality. No global integral solution is inferred from the local checks.

The complete RQT-217 evidence ZIP contains the original Gram/operator, prior reports, original kernel and reduced Gram, exact SymPy verifier, resulting JSON, and research note.

**RQT-218:** investigate integral orbits via hyperbolic splitting, quadratic-form automorphisms, or valid integral spinor-genus obstruction.
