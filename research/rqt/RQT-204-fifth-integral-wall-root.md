# RQT-204 — Fifth integral Wall root

**2026-11-07 | Exact original RQT-122 Gram and RQT-133 operator.**

Continue RQT-203’s four-root flag in the index-64 RQT-198 lattice. Write Q=B^T G_K B and H=B^T G_K (Y-I)^(-1) B. Set T4=[b1,b2,b3,b4]. The one-sided Wall constraints A x=0 use A=T4^T H^T. The exact integer matrix A has rank 4, with unit-determinant pivot columns **(0,1,3,9)**. These yield a saturated integral kernel of rank 17.

The fifth root in RQT-198 basis coordinates is:

```
[-47,-6,-29,61,55,97,5,28,7,74,4,-38,-54,-55,-89,-1,13,50,1,26,82]
```

In the original 22-coordinate ambient basis the root is:

```
[-32,-27,-1,-29,61,55,97,5,28,7,-20,-34,-38,-54,-55,-89,62,13,50,1,134,82]
```

Exact original-matrix checks: x^T Q x = **−2**, Ax=0, rank[T4,x]=5, h^T G K B x=0. The corresponding integral reflection is an involution preserving the original Gram form and fixing h.

The five-element Wall form is **upper-unitriangular**:

```
[[1,0,0,0,-7],
 [0,1,0,3,-36],
 [0,0,1,-1,21],
 [0,0,0,1,62],
 [0,0,0,0,1]]
```

The Gram form equals the negative symmetrization. Exact search used a unimodular LLL change of basis within the saturated integer kernel. The reproducible 17-dimensional reduced coefficient vector is `[-41,97,-28,47,27,2,-41,-56,-51,-76,-1,50,13,1,26,82,4]`.

**PROVED:** five independent exact integral square−2 roots in the original h-orthogonal complement with upper-unitriangular Wall pairing.

**OPEN:** sixth root and extension through 21; a full 21-reflection equality; minimal length 21 versus 23; full reflection generation of stabilizer. The downloadable RQT-204 evidence bundle contains both original matrices, prior reports, exact executable SymPy audit, full JSON measurements, and this note.

**Next RQT-205:** sixth root in the saturated rank-16 integer Wall kernel.
