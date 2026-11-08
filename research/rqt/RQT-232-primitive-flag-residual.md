# RQT-232 — Primitive 17-root flag and rank-four moving residual

**2026-11-08 | Exact source-matrix replay PASS.**

Reconstructed original 22×22 Gram G, operator X, index-64 RQT-198 basis B, Wall matrix H, and the seventeen certified norm−2 roots. All tests use integer/rational arithmetic.

**New invariant 1 (primitive flag):** The 21×17 integer matrix T17 of the archived roots has Smith diagonal `(1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1)`. Therefore its span is primitive in the rank-21 index-64 lattice. There is no saturation/index obstruction from these roots alone.

**New invariant 2 (rank-four residual):** In the recorded root order let `P17=s_b1 ... s_b17`, where `s_b=I+b(bᵀ G)` is the norm−2 reflection. Define `D=P17^{-1}X`. Its restriction to the primitive rank-21 fixed-vector complement satisfies:
- `Dᵀ G_K D = G_K`
- `det D = +1`
- `rank(D−I) = 4`; fixed-subspace dimension **17** on K, **18** on original rank 22.

**New invariant 3 (exact reciprocal quartic):** Characteristic polynomial of the restriction to K:
```
(λ−1)^17 [λ^4
 −1788747456455898654291114110156498819571267856 λ^3
 −3577018855561589105882070208922936708397540510 λ^2
 −1788747456455898654291114110156498819571267856 λ
 +1]
```
Calculated by exact Newton trace identities and checked directly against rank(D−I)=4. The quartic is reciprocal, consistent with determinant one and isometry.

**Consequence:** The continuation problem becomes finding an **integral four-reflection factorization of the residual isometry D**. At least four reflections are required by rank(D−I)=4. This reduction does **not** prove that four integral norm−2 reflections exist or that a 21-reflection product equals X. Minimum length 21 versus23 stays open.

Full independent original-source reproducer `rqt232_verify.py` and machine-readable `RQT-232-report.json` are in the self-contained evidence ZIP linked in the conversation.

**RQT-233 target:** factor the rank-four moving residual over the integral lattice and check source-matrix product equality.
