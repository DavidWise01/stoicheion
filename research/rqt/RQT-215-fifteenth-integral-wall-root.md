# RQT-215 — Fifteenth exact integral Wall root

**2026-11-07 | Original RQT-122 Gram / RQT-133 operator**

Let Q=BᵀG_KB and H=BᵀG_K(Y−I)⁻¹B and let T14 be the previous fourteen certified roots. The linear constraint A=T14ᵀHᵀ has exact rank **14**. Beginning with RQT-214's saturated integer kernel of rank eight, a unimodular elimination with pivot **1** produces a saturated rank-seven integer kernel. Its restricted Gram determinant is **18369518910500574521749122**.

**Fifteenth root in RQT-198 basis:** `1455,-4653,-23402,2094,2636,3257,6296,7701,24421,5828,28,-905,5688,10595,3465,44,-9304,-5021,10574,-8456,10492`.

**Original ambient 22-vector:** `-10125,-19459,-16795,-23402,2094,2636,3257,6296,7701,24421,10600,1347,-905,5688,10595,3465,-3663,-9304,-5021,10574,-6420,10492`.

**Reduced kernel coefficients:** `[-176,-74,51,-13,94,8,-71]`.

**Wall column 15:** `[-3,-2013,740,-10916,163288,-328774,-26295,-6344,-17638,6255,-11093,9128,-14749,37553,1]`.

Exact source-matrix tests confirm norm −2, 14 zero one-sided Wall equations, orthogonality to h, 15 independent roots, upper-unitriangular 15×15 Wall matrix, and integral reflection R=I+r(rᵀG) satisfying R²=I, RᵀGR=G, Rh=h.

**PROVED:** exact fifteenth integral Wall root and saturated rank-seven kernel.

**OPEN:** six more roots, equality of a full 21-reflection product with X, and minimal reflection word length 21 versus 23. A partial upper-unitriangular root flag does not by itself certify a full factorization.

**Reproduction:** a complete standalone ZIP is attached to the conversation with original 22×22 matrices, prior RQT reports, 21×7 saturated and reduced kernel bases, 15×15 Wall matrix, original discovery script, and exact SymPy verifier. Next RQT-216 seeks root sixteen in a saturated rank-six Wall kernel.
