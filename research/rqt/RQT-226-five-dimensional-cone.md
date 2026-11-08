# RQT-226 — Exact five-dimensional cone and finite exclusion

**2026-11-07.** Reconstruct the corrected RQT-225 saturated rank-five Wall kernel of the sixteen certified roots. Its Gram form F is exact, even integral and has determinant 614658467036485410516469524254677624 and signature (1,4).

Write x=(t,z) with t=x[0] and z=(x[1],x[2],x[3],x[4]). Let P=−F[1:5,1:5], b=F[1:5,0], v=P⁻¹b, beta=F[0,0]+bᵀP⁻¹b. Exact identity: xᵀ F x = beta t² − (z−vt)ᵀP(z−vt). P is positive definite, beta>0.

The exact rational v is
```
−13475044518882528957194892671533 / 34974256076427286519661440016052
 790453207300256768597331194119   / 17487128038213643259830720008026
 7076115499096049174851148931595  / 34974256076427286519661440016052
 4546920898566711915587641875797  / 17487128038213643259830720008026
```
and beta is `76832308379560676314558690531834703/34974256076427286519661440016052`.

For each coordinate i of z, exact inequality `v[i]²>(beta+2)*(P.inv())[i,i]` holds. Consequently all norm−2 integral roots must have one of the **two unbounded sign orthants**:
```
t>0 : (+,-,+,+,+)
t<0 : (-,+,-,-,-)
```
t=0 is impossible because P is positive definite.

**Complete finite exclusion:** For t from 1 to 6000, the exact rational ellipsoid inequalities yield integer intervals for z[0:3] containing all possible roots. Enumerate every integer triple and solve for z[3] by exact 128-bit integer discriminant, with that final coordinate unbounded. The completed reproducible run reports:
```
TOTAL 588300144 FOUND 0
```
Sign inversion covers negative t. Hence any integer norm−2 vector in the frozen rank-five basis **must have |x[0]|≥6001**. This is a genuine finite-domain exclusion, not an obstruction to all integral solutions.

**Status:** exact original matrix/basis identity PASS; global sign orthant theorem PASS; exact bounded search PASS. **OPEN:** root17, roots18–21, a 21-reflection product equality, minimality.

The standalone ZIP in the conversation includes original source matrices, original and reduced kernel bases, exact Gram, full 6000-slice bounds, C++ search, SymPy verifier, empty witness list and result ledger.

**Next RQT-227:** global integral orbit/construction or rigorous obstruction beyond this finite cone.