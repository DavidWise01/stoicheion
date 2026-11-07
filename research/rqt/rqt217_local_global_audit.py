#!/usr/bin/env python3
"""RQT-217 local/global norm -2 certificate. Requires archived RQT-216-reduced-gram.json."""
import json
from pathlib import Path
import sympy as s
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ
F=s.Matrix(json.loads((Path(__file__).parent/'RQT-216-reduced-gram.json').read_text()))
assert F==F.T and all(F[i,i]%2==0 for i in range(6))
a=s.Matrix([0,0,2,0,1,-2]);k=1845
assert (a.T*F*a)[0]==-2*k*k
assert ((a/k).T*F*(a/k))[0]==-2
d=[int(smith_normal_form(F,domain=ZZ)[i,i]) for i in range(6)]
assert d==[1,1,1,1,2,156991397203061370861566251934]
assert F.det()==-313982794406122741723132503868
assert F[0,0]//2+1==-234390 and F[0,2]==178351 and F[2,2]//2==-426914
t=0
for power in range(1,65):
 if (-234390+178351*t-426914*t*t)%(1<<power):t+=1<<(power-1)
 assert (-234390+178351*t-426914*t*t)%(1<<power)==0
assert t==4727422553192030530
x=s.Matrix([1,0,t,0,0,0])
assert ((x.T*F*x)[0]+2)%(1<<65)==0
print('RQT-217 PASS: rational norm -2 and prime-local solvability; integral root OPEN')
