# RQT-192 — 2-adic isotropic parity-coset lift

Original-source exact arithmetic (2026-11-06). Source X and Gram in research/rqt/source.

For stabilizer-preserving Eichler factorization, seek r∈K=h⊥∩M with u·r=0, a·r=-4, r²=-2; then s=a-r is another (-2) root orthogonal to u and h.

In the integral basis k_j=e_(j+1)-e0 (0≤j≤18), k19=e20, k20=e21, choose

r0=k0+k1+k3+k4+k5+k7+k8+k9+k10+k12+k15+k18+k19.

Original Gram test: u·r0=0, a·r0=-4, r0²=-382 ≡ -2 (mod 4).
Set d=k0: u·d=a·d=0, r0·d odd, d² even.

**Hensel lifting proof:** if r²≡-2 (mod 2^k), k≥2, add 2^(k-1)d if the next bit requires correction. The norm difference is
2^k(r·d)+2^(2k-2)d² ≡ 2^k (mod 2^(k+1)).
The exact linear equations persist, and the derivative parity remains odd. Thus a compatible inverse-limit r exists in K⊗Z₂ with r²=-2, a·r=-4 and u·r=0. Setting z=2r-a supplies a 2-adic isotropic point in the required parity coset a+2K.

**Measured:** exact modular lifts through 2^21 for r²+2 and 2^23 for z²; original matrices verified. See companion rqt192_2adic_lift.py and RQT-192-report.json.

**LIMIT:** This proves Z₂-solubility only. No ordinary integral root pair, complete stabilizer-only factorization, or odd-prime local result is claimed.

**RQT-193:** Global integer root witness or genuine arithmetic obstruction.
