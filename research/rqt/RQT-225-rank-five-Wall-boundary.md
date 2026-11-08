# RQT-225 — Corrected saturated rank-five Wall kernel

**2026-11-07 | Exact original-matrix audit PASS**

Continue the RQT-224 sixteen-root flag, RQT-198 index-64 candidate lattice, and RQT-216 saturated rank-six Wall kernel. The seventeenth-root constraints use the **one-sided orientation** `T16.T * H.T * b17 = 0` and `b17.T * Q * b17 = -2`, with `H=B.T G_K (Y-I)^(-1) B`.

Inside the frozen rank-six coordinates `b17=Z*z`, the additional linear equation is

```
[933123,-510896,161471,-25969,-571236,818364] * z = 0
```

**Orientation warning:** `b16.T * H * Z` is the opposite pairing and is *not* the required condition. The exact replay uses `b16.T * H.T * Z`.

This row has gcd **1**. A unimodular reduction to `(1,0,0,0,0,0)` produces a **saturated rank-five integer kernel**. An integer LLL reduction provides a compact basis `U`, with exact Gram `J=U.T F U` and determinant

```
614658467036485410516469524254677624
```

The signature is **(1,4)** exactly. For each of the five four-coordinate principal restrictions `J_j`, the four leading Sylvester minors of `-J_j-88000 I4` are strictly positive. Thus **every norm−2 root must use all five reduced coordinates**. Any nonzero integer vector missing a coordinate has norm strictly below −88000.

**Exhaustive finite audit:** all `61^4=13,845,841` assignments of first four reduced coordinates in [−30,30] were tested with an exact signed-128-bit integer quadratic discriminant; the fifth coordinate is **unbounded** and solved exactly from the quadratic. **Zero roots** in this domain. This is not proof of global nonrepresentation.

**Exact residue counts:** mod4 `512/1024` compatible; mod8 `9216/32768` compatible. No local obstruction at these levels.

**PASS:** original matrices, sixteen roots, correct one-sided Wall constraint, saturated rank-five kernel, exact determinant, full-support necessity, modular counts and complete bounded search. **OPEN:** seventeenth integral root, full 21-root product equality and reflection-length minimality.

The reproducible ZIP attached to the conversation has original Gram and operator, prerequisite root reports, frozen kernel/reduced Gram JSON, SymPy verification, C++ exact search, and a research note.

**Next RQT-226:** investigate the near-isotropic five-dimensional cone beyond the certified finite domain.