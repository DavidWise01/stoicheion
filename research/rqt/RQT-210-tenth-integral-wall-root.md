# RQT-210 — Tenth integral Wall root

**2026-11-07 | Original RQT-122 Gram / RQT-133 integer operator.**

The nine-root Wall flag extends to ten independent integral square-(−2) roots inside the RQT-198 index-64 lattice.

With Q=BᵀG_KB, H=BᵀG_K(Y−I)⁻¹B, and T9 the previous nine roots, the nine Wall constraints A=T9ᵀHᵀ have rank 9. Integer-preserving row reduction and unimodular column elimination give a **saturated rank-12 integral kernel** with unit pivot diagonal. Its restricted Gram determinant is **−3593047499752688**.

Tenth root in index-64 lattice coordinates:
```
[-5,18,87,-7,-10,-11,-22,-29,-95,-22,-1,3,-23,-41,-15,-2,38,21,-42,33,-41]
```

Original 22-coordinate root:
```
[39,76,64,87,-7,-10,-11,-22,-29,-95,-41,-5,3,-23,-41,-15,13,38,21,-42,25,-41]
```

Exact checks: squared norm −2, all nine one-sided Wall equations satisfied, root orthogonal to h, ten-root rank ten, upper-unitriangular Wall pairing. The tenth Wall column is **[−3,6,−1,46,−713,1154,98,24,46,1]**. Its integral reflection squares to the identity, preserves original Gram G, and fixes h. Reproduce from original source matrices and archived RQT-198/201/203/204/205/207/208/209 reports. The reduced-kernel coefficient witness is `[-4,-8,-17,11,-7,8,18,-11,0,18,8,-6]`.

**PROVED:** ten-root Wall-compatible flag. **OPEN:** 11 further roots, complete 21-reflection factorization, and shortest word length 21 vs 23.

**Next natural invariant: RQT-211**, construct saturated rank-11 kernel and eleventh integral Wall root.
