# RQT-202 — Fourth-root Wall constraint: complete parity census and bounded integral audit

**2026-11-07 | Original RQT-122 Gram / RQT-133 operator; RQT-198 index-64 basis; RQT-201 three-root chain.**

Define K=h⊥∩M, Q=BᵀG_KB, H=BᵀG_K(Y−I)⁻¹B, and T=[b1,b2,b3] with TᵀQT=−2I₃, TᵀHT=I₃. The fourth-root conditions are **A x=0 and xᵀQx=−2**, with A=TᵀHᵀ. This is the correct one-sided Wall condition xᵀHT=0. Exact rank A=3, so the rational linear solution space has dimension 18.

### Exhaustive finite domains
- All coefficient vectors with support 1..7, nonzero entries ±1, tested against both exact equations: **zero** square−2 witnesses.
- All coefficient vectors with support 1..5, nonzero entries in {−2,−1,1,2}: **zero** square−2 witnesses.
- This is strictly a bounded non-finding, **not** a proof that a fourth root cannot exist.

### Complete mod-two and mod-four audit
- All 2,097,152 coordinate parity classes enumerated.
- **262,144** satisfy Ax=0 mod 2.
- **122,880** satisfy Ax=0 mod 2 and xᵀQx≡2 mod 4.
- An explicit mod-four lift x=x0+2y was found satisfying Ax=0 mod 4 and xᵀQx≡2 mod 4.
- Therefore **this congruence layer presents no obstruction** to extending the chain. No exact integral fourth root was found within either bounded domain.

### Status
**PASS** exact original-matrix constraints, exhaustive bounded searches, full parity census and mod-four lift. **OPEN** exact fourth root; 21-root Wall triangular flag; shortest length 21 vs 23.

### Next: RQT-203
Construct the full integral kernel of A and search with indefinite lattice reduction for a square−2 root. Alternatively obtain a genuine higher-modulus obstruction. Do not equate bounded search failure with global nonexistence.

The standalone original-source evidence bundle is linked in the conversation.
