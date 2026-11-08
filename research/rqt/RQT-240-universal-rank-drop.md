# RQT-240 — Universal rank-drop determinant identity

**2026-11-08 | Exact rank-five matrix replay PASS; existential theorem, not an explicit root.**

Preserve the sixteen certified integral Wall roots of RQT-239 Branch 2. The saturated rank-five moving lattice carries even integral Gram F5 and exact residual isometry D5. Define the correctly oriented unimodular Wall matrix H5=F5(D5-I)^(-1). Exact original-source replay gives:
- H5+H5ᵀ=−F5, det H5=1.
- D5ᵀ F5 D5=F5.
- D5-I=H5^(-1)F5 and det(D5-I)=det F5=312669187727137013416789354039323478, nonzero.

**Universal determinant theorem.** For any integral r, let q=rᵀF5r and s_r=I+r(rᵀF5). The rank-one determinant lemma gives

```
det(s_r D5-I)/det(D5-I)
 = 1 + rᵀF5 D5(D5-I)^(-1)r
 = 1 + q + rᵀH5r
 = 1 + q/2,
```

since H5+H5ᵀ=−F5 implies rᵀH5r=−q/2. Thus

```
det(s_r D5-I) = det(D5-I) * (1 + q/2).
```

When q=−2, s_r is an integral reflection, the determinant vanishes, and s_rD5-I is a rank-one update of invertible D5-I. Consequently **rank(s_rD5-I)=4**, exactly one less than rank(D5-I)=5.

**Existence consequence.** RQT-239 proved by Meyer's theorem and squarefree Gram determinant that an integral r with q=−2 exists in the saturated rank-five Wall lattice. Therefore at least one integral rank-reducing seventeenth reflection exists for Branch 2, though its coordinates are not yet constructed.

**Caution:** This does NOT certify that a rank-reducing root satisfies the 132-class downstream completion sieve, nor that its rank-four successor admits four more integral reflections. Explicit root17 and complete 21-reflection identity remain OPEN.

**Independent replay:** The standalone ZIP includes original 22×22 Gram and operator, Branch 2 root/basis certificates, `rqt235_verify.py`, `rqt239_verify.py`, and `rqt240_verify.py`. The latter checks the exact residual identities and determinant law with several integer vectors; the symbolic rank-one proof covers all integer vectors.

**Next RQT-241:** find explicit primitive integral isotropic u and construct r via the Bézout hyperbolic-plane formula, then screen the resulting root against the 132 modular first-root classes.
