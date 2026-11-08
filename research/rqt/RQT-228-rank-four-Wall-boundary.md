# RQT-228 — Saturated rank-four Wall kernel

**2026-11-07 | Exact original-source audit.** Preserve all 17 RQT-227 integral Wall roots. For an eighteenth root impose b18ᵀQb18=−2 and b18ᵀHbi=0 for i=1..17.

The extra correctly oriented constraint in the RQT-225 rank-five coordinates is

`[-1622481684,-2177526381,-1405150251,3589101224,420794413] · x=0`.

The coefficient gcd is 1; exact unimodular column elimination produces a **saturated rank-four integer kernel**. Its reduced Gram matrix is

```
[-17801313208674,-15761198498141,15135416925109,7424607432690]
[-15761198498141,-18808565513138,15151261558975,6742605417749]
[15135416925109,15151261558975,-13901548148824,-5277176639089]
[7424607432690,6742605417749,-5277176639089,-6096520821564]
```

Exact determinant: **−7154513768473386414464298429235934347540076220**. Every 3×3 principal coordinate restriction is negative definite via exact Sylvester minors, hence the signature is (1,3) and **all four reduced coordinates are necessarily nonzero** for any norm−2 root.

Exact modular census: mod4 **128/256**, mod8 **1024/4096**, mod16 **8192/65536** compatible classes. No local obstruction at those levels.

Exact bounded audit: all **201³=8,120,601** integer choices for the first three reduced coordinates in [−100,100], solving the fourth-coordinate quadratic by integer discriminant-square and divisibility checks **without a bound on the fourth coordinate**. **Zero roots** within that domain; this is not a global impossibility proof.

**PASS:** constraint orientation, saturation, reduced form/determinant, all principal restrictions, modular census and finite exhaustive audit. **OPEN:** root eighteen; roots 19–21; complete 21-reflection factorization; shortest length 21 vs23.

The independent original-source replay, saturated basis matrices and all prior certificates are attached as a downloadable RQT-228 evidence ZIP in the conversation.

**Next RQT-229:** exact four-dimensional near-isotropic cone construction.
