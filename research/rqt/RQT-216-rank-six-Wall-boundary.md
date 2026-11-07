# RQT-216 — Saturated rank-six Wall kernel and bounded root audit

**2026-11-07.** Exact original sources: RQT-122 Gram G, RQT-133 operator X, RQT-198 index-64 basis and the RQT-215 fifteen-root flag. Let Q=BᵀG_KB, H=BᵀG_K(Y−I)⁻¹B, A=T15ᵀHᵀ.

## Exact kernel
- rank A=15; the saturated integer null lattice has rank 6.
- Constructed from the previously saturated rank-7 kernel by exact unimodular elimination; final pivot gcd=1.
- The reduced kernel Gram F has exact determinant **−313982794406122741723132503868**.
- Numerical signature F=(1,5). The determinant and kernel equations are certified by exact arithmetic.

## Complete bounded root search
The exact equation is xᵀFx=−2. Enumerate **all 61⁵=844596301** tuples with the first five reduced coordinates in [−30,30]. For each tuple, solve the quadratic equation for sixth coordinate via integer discriminant-square and divisibility tests, with **no bound** on the sixth coordinate. **Zero roots found.** Also no roots in the complete coefficient boxes {−1,0,1}⁶ and {−2,−1,0,1,2}⁶. All are rigorous finite-domain results, not a global impossibility proof.

## Complete congruence census
- mod 4: **2048 of 4096** coordinate residue classes satisfy q≡−2.
- mod 8: **69632 of 262144** coordinate residue classes satisfy q≡−2.
- Neither layer obstructs a sixteenth root.

## Status
**PASS:** original source matrices, saturated rank-six kernel, determinant, finite exhaustive norm audit, and mod4/mod8 census.
**OPEN:** sixteenth integral root; full 21-reflection product; minimum length 21 versus 23. Fifteen-root Wall flag preserved.

**Reproduce:** standalone RQT-216 archive contains both original matrices, prerequisite JSON reports, saturated and reduced basis, the restricted Gram, `rqt216_verify.py`, `exhaustive216_30.py` and complete results.

**Next RQT-217:** use exact rational hyperbolic splitting, integral quadratic-form methods, or an authentic local obstruction to address norm −2 beyond the audited domain.
