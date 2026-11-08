# RQT-233 — Integral Residual-Image Identity

**2026-11-08 · Original 22×22 Gram and operator checked exactly.**

Let T17 be the certified seventeen-root Wall flag; let Y be X restricted to the rank-21 h-orthogonal lattice, P17 the ordered reflection product, D=P17⁻¹Y and C=D−I. Let V=B·Z be the frozen rank-four Wall-kernel basis in the original rank-21 coordinates, where Z combines the saturated RQT-216, RQT-225 and RQT-228 kernel bases.

Exact tests establish:
- `rank(C)=4`, `DᵀG_K D=G_K`, `det D=+1`.
- `SNF(C)=diag(1,1,1,1,0^17)` so its integral image is primitive in K.
- The 17 Wall constraints vanish on both V and C; thus their rational four-dimensional spaces coincide.
- More strongly, **C=VJ for a 4×21 integral matrix J with SNF(J)=(1,1,1,1)**. Consequently the **integral** image of D−I equals the exact saturated rank-four Wall kernel, not merely its rational span. Also `SNF(V)=(1,1,1,1)`.
- The residual preserves the lattice integrally: `DV=VD4` for an exact 4×4 integer isometry D4, `D4ᵀ F4 D4=F4`, and `det D4=1`. Its reciprocal quartic is the one measured in RQT-232.
- `det(I−D4)=det(F4)=−7154513768473386414464298429235934347540076220`.
- `det(I+D4)=476057350208202700158011390060930744995204=(689969093661594888802)^2`. This determinant-square compatibility check does not block a four-reflection decomposition; it does not prove one.

**PASS:** exact primitive residual image, integral lattice equality, four-dimensional residual action and determinant identities. **OPEN:** actual integral square−2 root number 18; roots 19–21; complete 21-reflection product equality; minimum length 21 or23.

The downloadable RQT-233 standalone archive contains original Gram/operator, every prior root report, the three kernel bases, `rqt233_verify.py`, original-matrix results and complete four-dimensional action/Gram matrices.

**Next RQT-234:** seek an integral norm−2 vector in the residual image that reduces moving rank 4→3, using the explicit D4 and exact lattice arithmetic.
