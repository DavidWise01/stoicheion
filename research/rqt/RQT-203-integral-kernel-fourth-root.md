# RQT-203 — Fourth integral Wall root via saturated kernel

**2026-11-07 | Original RQT-122 Gram and RQT-133 operator verified exactly.**

Take the index-64 RQT-198 lattice with Q=BᵀG_KB and integral Wall pairing H=BᵀG_K(Y−I)^−1B. Retain the exact three-root RQT-201 flag T, with TᵀQT=−2I₃ and TᵀHT=I₃.

The next one-sided Wall condition is Av=0, A=TᵀHᵀ. Here rank A=3. The pivot columns (3,9,20) have determinant +1, giving an **exact saturated integral kernel of rank 18**. Integer LLL changes its basis unimodularly; a search in this kernel yielded the explicit integral witness

`v=[3,1,3,-4,-4,-8,1,-1,1,-4,0,2,3,3,6,0,-2,-4,1,-3,-5]`

in RQT-198 coordinates. Its original ambient 22-coordinate vector is

`KBv=[4,2,0,3,-4,-4,-8,1,-1,1,1,1,2,3,3,6,-5,-2,-4,1,-11,-5]`.

Exact matrix checks give:

`vᵀQv=−2`, `vᵀHT=0`, rank[T,v]=4, and

```
[T,v]^T H [T,v] = [[1,0,0,0],[0,1,0,3],[0,0,1,-1],[0,0,0,1]]
[T,v]^T Q [T,v] = [[-2,0,0,0],[0,-2,0,-3],[0,0,-2,1],[0,-3,1,-2]]
```

The new ambient root is integral, orthogonal to h and of norm −2; its integral reflection is an involution preserving G and fixing h.

**PROVED:** an exact four-element Wall-upper-unitriangular root flag within the index-64 candidate. **OPEN:** a fifth root, a 21-root complete flag, an exact 21-reflection product, and minimal root-word length (21 or 23).

**Reproduce:** `rqt203_integral_kernel_root.py`, with the original matrices and prior JSON evidence. Full self-contained source-and-result ZIP provided in the conversation.

**Next natural invariant: RQT-204 — fifth integral root in the four-constraint Wall kernel.**
