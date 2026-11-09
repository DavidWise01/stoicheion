#!/usr/bin/env python3
"""RQT-254 independent exact reduced-lattice identity check (SymPy).
The full original-source certificates, outward search-bound generator,
completed integer search logs and C++ search are in the evidence ZIP.
"""
import sympy as s
F=s.Matrix([
[-4523390658618420908,2239380521691398176,-2422224054680331217,-3109472006028867029],
[2239380521691398176,-6703602364620082676,-1185189370853509030,4418426561730616356],
[-2422224054680331217,-1185189370853509030,-5270086080008383040,4649693842155823637],
[-3109472006028867029,4418426561730616356,4649693842155823637,-12373412455412906476]])
T=s.Matrix([[31,4,-31,-18],[-100,-13,100,58],[-9,-1,9,5],[336,43,-335,-195]])
J=s.Matrix([
[9208923577999086,-2890579252927294,-1029318396906446,276003667781247],
[-2890579252927294,-136287821825501156,-29512715198402862,11299357575842588],
[-1029318396906446,-29512715198402862,-1127313935375881122,-146309554088173376],
[276003667781247,11299357575842588,-146309554088173376,-5868287405277328266]])
assert T.det()==-1 and T*F*T.T==J and J.det()==F.det()
assert list(T.inv().T[0,:])==[-24,-22,-17,-17]
P=-J[1:4,1:4]; v=P.inv()*J[1:4,0]
beta=J[0,0]+(v.T*P*v)[0]
assert all(P[:i,:i].det()>0 for i in range(1,4)) and beta>0
print('RQT-254 PASS: exact integral basis, determinant, secondary height functional.')
print('Search certificates: 33,614,572 exact pairs for norm -2 and norm 0; files in ZIP.')
print('Root eighteen explicit coordinates remain OPEN.')
