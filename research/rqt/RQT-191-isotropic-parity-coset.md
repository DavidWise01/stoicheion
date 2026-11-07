# RQT-191 — Stabilizer-preserving Eichler root decomposition and isotropic parity coset

**2026-11-06 | Exact arithmetic on original RQT-122/133 matrices.**

## The new invariant

The RQT-190 residual is `T(u,a)`, where u and a belong to K=h^⊥∩M, u²=u·a=0, and a²=-8. Seeking two integral roots r,s ∈ K∩u^⊥ with a=r+s and r²=s²=-2 is equivalent to seeking **z ∈ a+2K** such that z²=z·u=z·a=0. The equivalence is elementary:

- Given roots, let z=r-s=2r-a. Then z∈a+2K, z²=0, z·a=0, z·u=0.
- Given z with these conditions, r=(a+z)/2 and s=(a-z)/2 lie in K, are perpendicular to u, sum to a, and have square (a²+z²±2a·z)/4=-2.

Thus the **isotropic parity coset** is an exact necessary-and-sufficient criterion for the sought **two-root** stabilizer-preserving decomposition. It does not decide whether longer stabilizer root factorizations exist.

## Original-source witnesses

u = [-4,-5,-5,-7,0,1,2,0,1,6,3,2,1,1,4,2,-1,-3,0,2,-1,4]

a = [-17,-22,-24,-29,0,5,5,0,6,24,13,8,1,9,18,10,-4,-10,-3,10,-8,11]

Ambient RQT-190 root r0 = -e0-e1-e2-e12+e20, s0=a-r0. Both have square -2, but (h·r0,h·s0)=(-4,+4). The isotropic vector z0=2r0-a satisfies z0²=z0·u=z0·a=0 and z0≡a mod 2M, **but h·z0=-8**, so z0 does not belong to K.

## Reproducible bounded exclusion

Using K-basis k_j=e_(j+1)-e0 for j=0..18, k19=e20, k20=e21, the condition u·r=0 eliminates k6, leaving 20 eligible basis directions. Exhaustively enumerated all 87,440 signed-support vectors of size 1 through 4. Of these, 1,084 obeyed a·r=-4. None had r²=-2. These exact counts verify the **bounded** search only. No global absence of such roots is claimed.

## What is closed and what is open

**PROVED:** exact parity-coset equivalence for a two-root factorization; ambient isotropic witness fails K; bounded sparse search finds none.

**OPEN:** existence of a point in the entire isotropic parity coset; any longer decomposition of a into K-roots; a full stabilizer-preserving factorization of X. An exhaustive short-vector search is never a global nonexistence certificate in this indefinite lattice.

## Next boundary: RQT-192 — Local solubility of the isotropic parity coset

Analyze z≡a (mod 2K), z²=z·a=z·u=0 over Z₂ and odd p-adic lattices. Determine whether a genuine local obstruction exists, or else construct a global isotropic witness using lattice reduction and hyperbolic plane decomposition.
