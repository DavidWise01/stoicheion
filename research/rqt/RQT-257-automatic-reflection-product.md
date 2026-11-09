# RQT-257 — Automatic reflection-product theorem

**2026-11-08 | Exact original-source replay, symbolic proof, complete modular audit PASS.**

Preserve the seventeen RQT-241 Branch-2 certified integral norm−2 Wall roots. On the saturated rank-four RQT-242 lattice let F be the even integral Gram, H the unimodular Wall matrix with H+Hᵀ=−F, and D=I+H⁻¹F the residual isometry.

**Exact sufficiency theorem.** Suppose four integer vectors r1,...,r4 obey `riᵀ F ri=−2` and `rjᵀ H ri=0` for each j>i. Let V consist of these four columns. Its Wall form A=VᵀHV is upper-unitriangular with diagonal 1 because `riᵀ H ri=−(riᵀF ri)/2=1`. Thus `1=det A=(det V)^2 det H=(det V)^2`, proving `det V=±1`: the four roots automatically give an **integral basis**.

In that basis F' =−A−Aᵀ. The ordered norm−2 reflection product has the universal Coxeter–Seifert identity
```
s1*s2*s3*s4 = −A⁻¹ Aᵀ = I+A⁻¹ F'.
```
Conjugating by unimodular V gives **`s_r1*s_r2*s_r3*s_r4 = I+H⁻¹F = D` exactly**. Therefore after finding four exact integral roots satisfying the norm and six lower Wall equations, no separate nonlinear matrix-product test is necessary. With the frozen first 17 reflections this would certify the original 21-word factorization automatically.

**Modular version:** if norms equal −2 modulo 2m and all six lower one-sided Wall pairings vanish modulo m=2^k, then the same product equality holds modulo m. The diagonal Wall entries are 1 mod m and det V is odd; this is not an actual integral product.

**Executed independent arithmetic audit:**
1. Reconstructed the exact RQT-242 saturated rank-four Gram, Wall, and residual from the frozen original-source certificate, with unchanged report SHA256.
2. Symbolically verified universal Coxeter–Seifert identity for n=1,2,3,4 with arbitrary integer upper-unitriangular Wall entries.
3. Exhaustively checked **all 18,432 ordered norm-compatible Wall flags modulo 4**; **all 18,432 products equal D modulo 4**, zero mismatches.
4. Independently verified the RQT-249 four-column witness: its norm congruences modulo `2^257` and lower Wall congruences modulo `2^256` imply and explicitly satisfy **the full four-reflection product equals D modulo `2^256`**.

**Status:** mathematical sufficiency theorem and finite modular product checks PASS. **OPEN:** integral root18, roots19–21, and actual integral 21-reflection word. RQT-247 only guarantees existence of individual norm−2 roots, not a full upper-unitriangular 4-column flag.

Evidence ZIP attached in the conversation has exact source matrices, 17th root witness, rank-four Gram/Wall/residual, RQT-249 high-precision certificate, independent symbolic and exhaustive verifier, and replay logs.

**Next RQT-258:** construct a completion-compatible integral eighteenth root and rank-three continuation using only exact norm/Wall equations.
