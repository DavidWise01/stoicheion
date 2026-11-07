# RQT-201 — Integral root lifting and three-element Wall-orthogonal flag

**2026-11-07 | Exact original RQT-122/133 matrices, original RQT-198 index-64 basis.**

Let K=h-perp∩M and B the index-64 basis of RQT-198. Let Q=BᵀG_KB and H=BᵀG_K(Y−I)⁻¹B. Exact original-source checks: H integral unimodular, H+Hᵀ=−Q.

## Exhaustive finite root census
For every 21-coordinate coefficient vector having support s=1..6, with every nonzero coefficient ±1, check xᵀQx=−2 exactly. The counts by s are **2,0,0,0,2,2**, respectively. These six signed roots comprise three pairs ±b_i.

## Exact lifted roots, zero-based indices in the RQT-198 integral basis
- b1 = e20
- b2 = e9 − e12 − e14 + e17 + e20
- b3 = e1 + e2 − e3 − e5 − e17 − e20

Let T=[b1 b2 b3]. Exact arithmetic yields:

**rank T=3, TᵀQT=−2I₃, TᵀHT=I₃.**

The images KBT are integral ambient 22-coordinate roots, orthogonal to h. Each individual root reflection is an integral isometry of G fixing h. The three reflections commute.

**Interpretation:** This certifies an exact three-element Wall-unitriangular root chain, not a complete 21-root basis. The enumeration is exhaustive only for support at most 6 with coefficients ±1 in this specific basis. Other, denser roots may exist. The minimal root-reflection length of original X remains **21 or 23**.

## Reproduction
Use the attached RQT-201 evidence archive, with original X and Gram files, exact RQT-198 21x21 basis, executable rqt201_integral_root_chain.py and JSON containing all three roots in 22 ambient coordinates.

## Next boundary
**RQT-202 — Extend the Wall-orthogonal three-root flag** using integral root search constrained by one-sided Wall pairings; insist on exact full operator equality for any claimed 21-root product.
