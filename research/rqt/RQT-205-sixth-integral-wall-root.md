# RQT-205 — Sixth integral Wall root

**2026-11-07 | Exact RQT-122 Gram and RQT-133 operator**

In RQT-198's index-64 lattice, let Q=BᵀG_K B, H=BᵀG_K(Y−I)⁻¹B, and T5 consist of RQT-201's first three roots and RQT-203/204's fourth and fifth. Define A=T5ᵀHᵀ. Exact calculation: rank(A)=5 and pivot columns (0,1,5,9,20) have determinant −1. The corresponding integer null lattice is saturated, rank 16.

**Sixth root in the RQT-198 21-coordinate lattice basis:**
```
[-60,-207,-819,-7,83,-28,220,288,811,50,-60,-24,369,425,202,-14,-202,-245,380,-286,207]
```

**Original 22-coordinate ambient root:**
```
[-417,-770,-719,-819,-7,83,-28,220,288,811,445,103,-24,369,425,202,-95,-202,-245,380,-365,207]
```

The original-matrix tests prove norm −2, all five one-sided Wall pairings zero, new flag rank 6, and integrality of an involutive Gram-preserving reflection fixing h.

**Six-root Wall matrix**:
```
[1,0,0,0,-7,115]
[0,1,0,3,-36,-11]
[0,0,1,-1,21,-17]
[0,0,0,1,62,-457]
[0,0,0,0,1,5116]
[0,0,0,0,0,1]
```

This matrix is upper-unitriangular and its negative symmetrization is the corresponding Gram matrix.

**Status:** six exact roots proven; 15 more needed for a 21-root certificate. Minimal root-word length remains one of {21,23}; no 21-product equality or minimality is claimed. Exact standalone archive is attached in the conversation.

**Next RQT-206:** saturated rank-15 Wall kernel and a seventh integral root.
