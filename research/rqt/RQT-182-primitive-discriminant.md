# RQT-182 — Primitive fixed lattice and discriminant gluing

**2026-11-06 | Exact original-source audit**

## Input
Original RQT-133 integer operator `X` and RQT-122 even unimodular Gram matrix `G`, archived at `research/rqt/source/`.

Let `h=(1,1,1,1,0^18)^T`, `h^T G h=4`, and `K_h = h^perp ∩ Z^22`. Source SHA256 values:
- X: `f23bf0c7897bd89a6d3113cb72b6df9e61fbb1b1feaf6dbf50c2f0079138357c`
- Gram: `4ae9d82c774a950ffc1acaabd70ac8a79c66f4d67051363734d6e01d9ca33ceb`

## Exact results
- `h^T G = (1^20,0,0)`, primitive pairing and `div(h)=1`.
- A saturated basis of `K_h` consists of `k_j=e_j-<h,e_j>e_0`, for j=1,...,21.
- `rank(K_h)=21`, `det(G|K_h)=-4`, signature `(2,19)`.
- `SNF(G|K_h)=diag(1^20,4)`: discriminant group `A_K=Z/4`.
- `[M:Z h + K_h]=4`.
- Explicit discriminant generator: `t=e_0-h/4 ∈ K_h^*`, `4t=4e_0-h ∈ K_h`, but `2t∉K_h`.
- Exact norm: `t^2=-9/4`; hence `q_K([t])=-1/4 mod 2Z`.
- The fixed lattice `Zh` has discriminant generator `h/4` with `q=+1/4`.
- Original e0 glues the pair: `e0=h/4+t`; the associated diagonal subgroup of `A_{Zh} ⊕ A_K` is isotropic, of order four.
- X fixes h and acts trivially on A_K: `Xt-t=Xe0-e0∈K_h`.

## Interpretation
The primitive orthogonal direct sum has determinant `4*(-4)=-16`; adjoining the order-four glue reconstructs the unimodular lattice of determinant `-1`. This is concrete arithmetic gluing in the original integer matrix, not the same as an orthogonal block decomposition of the action.

The result concerns exact lattice algebra. No inference about the Hodge conjecture or independent geometric provenance is established.

## Reproduce
Run `python research/rqt/rqt182_primitive_discriminant.py` (SymPy required); it outputs the exact K Gram matrix and a JSON evidence report.

## Next natural boundary
**RQT-183 — Discriminant anti-isometry and primitive embedding uniqueness:** check the gluing subgroup and identify which orthogonal automorphisms of the complement extend to the unimodular lattice.
