# RQT-211 — Eleventh integral Wall root

**2026-11-07 · Exact original-source verification.**

The ten-root Wall flag from RQT-210 extends to **eleven** independent integral square−2 roots. Let Q=BᵀG_KB and H=BᵀG_K(Y−I)⁻¹B. The ten linear constraints A=T10ᵀHᵀ have rank ten and a saturated rank-eleven integral kernel, constructed with ten unit pivots. An exact reduced-kernel witness is `[-34,-35,-7,13,-17,26,-9,6,-8,7,2]`.

**Eleventh root in RQT-198 lattice coordinates:** `15,-49,-242,15,29,31,58,78,257,60,3,-10,61,115,41,2,-99,-56,114,-88,107`.

**Eleventh root in original 22-coordinate basis:** `-110,-204,-176,-242,15,29,31,58,78,257,113,22,-10,61,115,41,-37,-99,-56,114,-69,107`.

It has norm −2, is orthogonal to h, and satisfies all ten one-sided Wall equations. The eleven roots remain linearly independent; their Wall matrix is upper-unitriangular with final column `[5,-14,10,-124,1808,-3265,-256,-67,-139,27,1]`. The corresponding reflection is integral, fixes h, squares to the identity, and preserves the original Gram matrix.

The companion Python verifier uses the archived original RQT-122 Gram and RQT-133 operator, together with prior root certificates. The complete ZIP evidence bundle (available in the conversation) includes the saturated kernel basis and independent exact replay.

**Closed:** eleven-root Wall-compatible flag. **Open:** ten remaining roots; full 21-reflection equality; minimum word length 21 or 23.

**Next natural boundary — RQT-212:** twelfth root in the saturated rank-ten Wall kernel.
