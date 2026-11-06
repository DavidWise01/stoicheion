# RQT-185 — Positive-plane orientation and reflection obstruction

**2026-11-06. Exact original-source audit.** Source: RQT-122 Gram matrix and RQT-133 integral 22×22 operator.

## Setup
The fixed vector h=(1,1,1,1,0^18) has norm 4. The primitive orthogonal complement K=h^⊥∩M has signature (2,19) and discriminant group Z/4. Its integral orthogonal group admits two signs: the discriminant sign ρ and the positive-2-plane orientation character χ_+.

Choose an oriented positive plane U=[v,w] inside K⊗Q, with the explicit **ambient** vectors

```
v=[5,-1,-3,-1,-7,-5,-10,-1,-1,4,3,2,3,7,7,11,-7,-2,-8,4,-17,-9]
w=[5,14,14,18,4,2,3,-4,-4,-22,-9,-4,-4,-7,-13,-10,8,10,7,-8,14,-5]
```

The exact original-source calculation confirms hᵀGU=0 and UᵀGU=[[2,1],[1,2]] (positive definite, determinant 3). For F∈O(K), define χ_+(F)=sign det(Uᵀ G F U). This is the orientation of the positive 2-plane, independent of the reference choice. It is multiplicative.

## Exact signed witnesses
- Identity: χ_+=+1.
- Original X and X²,X³: χ_+=+1.
- Reflections in square −2 roots e20 and e21: χ_+=+1.
- −I_K: χ_+=+1, ρ=−1.
- Integral square +2 reflection R_v=I−v(vᵀG): det=−1, fixes h, preserves G, χ_+=−1, ρ=+1.
- R_v(−I_K): (ρ,χ_+)=(−1,−1).

Therefore the homomorphism (ρ,χ_+):O(K)→C₂×C₂ is **surjective**. The commuting involutions −I_K (central) and R_v provide a subgroup isomorphic to C₂×C₂ that splits the quotient. In particular, O(M)_h=kerρ has both positive-plane orientation signs, with orientation-reversing representative R_v.

Every square −2 root reflection preserves the positive-2-plane orientation, hence their generated subgroup is contained in kerρ∩kerχ_+. The explicit R_v proves that such reflections **do not generate all of O(M)_h**.

## Scope and next boundary
This does **not** prove full generation of the index-two orientation-preserving kernel by negative roots, nor any new geometric theorem. Next: **RQT-186 — Character kernel and reflection index**, including an investigation of whether additional spinor or chamber invariants survive.

## Reproduction
Run `python research/rqt/rqt185_positive_orientation.py` (exact SymPy). All vector coordinates and tests are included in the executable certificate.
