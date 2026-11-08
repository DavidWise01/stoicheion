# RQT-224 — Global sixteenth integral Wall root (PASS)

**2026-11-07 | Original 22×22 Gram and operator verified exactly.**

RQT-216's saturated rank-six integral Wall kernel **does represent −2 over Z**, resolving the global existence question left open in RQT-216 through RQT-223.

**First integral witness (frozen rank-six basis)**:
```
[-183,-198,174,572,-368,-188]
```
This satisfies `xᵀ F x = −2` exactly, all six coordinates are nonzero and the sign pattern matches the global RQT-223 orthant restriction. Mapping through the exact integral kernel into the original rank-22 lattice gives:
```
[199942,383386,329827,461310,-41442,-52679,-65082,-125589,-153660,-481817,-207896,-25459,18678,-110547,-206072,-66620,69930,182115,99059,-207384,126089,-206587]
```

With `Q=BᵀG_KB`, `H=BᵀG_K(Y−I)⁻¹B`, and `T15` the previous fifteen certified roots, the new root is integral, norm −2, perpendicular to h and satisfies `b16ᵀHT15=0`. The expanded 16-root flag has rank16 and an upper-unitriangular Wall matrix. Its 16th Wall column is
```
[1020,39487,-14547,212026,-3205259,6441606,519103,126237,350030,-123886,220199,-188410,313329,-821813,322871,1]
```
The new reflection is an integral involution preserving original Gram G and fixing h.

**Constructive exact search:** For pivot `x[3]=301..1000`, exact rational Schur bounds enclose all four other bounded coordinates; the final coordinate `x[5]` is solved without any coordinate bound by testing the discriminant of an integer quadratic. C++ evaluates it with signed 128-bit integer arithmetic. Exhaustively checked **82,147,690** quadruples, found **8 global integral roots**. All eight were independently replayed against the original matrices with SymPy.

Witnesses in rank-six coordinates:
```
[-183,-198,174,572,-368,-188] d=1
[-230,-246,215,712,-461,-232] d=1
[-232,-246,223,729,-473,-242] d=1
[-237,-246,230,745,-479,-248] d=1
[-275,-299,269,865,-558,-288] d=1
[-285,-303,278,894,-577,-302] d=1
[-295,-311,274,906,-588,-302] d=1
[-320,-338,295,973,-634,-323] d=2
```
Thus both previously necessary primitive pairing-divisibility classes `d∈{1,2}` are now **globally realized**.

**PROVED:** sixteen independent exact integral Wall roots; all eight witnesses and both divisibility types. **OPEN:** roots 17 to 21; a complete 21-reflection product equality with X; minimum length 21 versus 23.

The standalone RQT-224 ZIP in the conversation contains original G/X, all prior root reports, complete exact Python cone-bound generator, C++ discriminant search and independent SymPy verification, search bounds, full witness ledger and this note.

**Next RQT-225:** construct the saturated rank-five integer kernel of the sixteen Wall constraints and seek root 17.
