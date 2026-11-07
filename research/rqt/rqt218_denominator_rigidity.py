#!/usr/bin/env python3
"""RQT-218 reproducible exact arithmetic certificate, run in attached evidence ZIP."""
import ast,json
from functools import reduce
from math import gcd
from pathlib import Path
import sympy as s
P=Path(__file__).resolve().parent
read=lambda n:s.Matrix(ast.literal_eval((P/'source'/n).read_text().strip()[7:-1]))
G=read('gram-22x22.txt');X=read('X-22x22.txt')
I=s.eye(22);h=s.Matrix([1]*4+[0]*18)
K=s.Matrix.hstack(*[I[:,j]-I[:,0] if j<20 else I[:,j] for j in range(1,22)])
B=s.Matrix(json.loads((P/'RQT-198-report.json').read_text())['basis_21x21'])
Z=s.Matrix(json.loads((P/'RQT-216-reduced-basis.json').read_text()))
F=s.Matrix(json.loads((P/'RQT-216-reduced-gram.json').read_text()))
assert Z.T*B.T*K.T*G*K*B*Z==F and X.T*G*X==G and X*h==h
a=s.Matrix([0,0,2,0,1,-2]);d=1845
assert (a.T*F*a)[0]==-2*d*d and gcd(int(F.det()),d)==1
assert F.det()==-313982794406122741723132503868
u=F*a
assert list(map(int,u))==[1187012,257661,-392622,-821191,-2966076,1528365]
assert reduce(gcd,map(int,u),0)==1
assert s.ilcm(*[s.denom(z) for z in u/d])==d
v=K*B*Z*a
assert list(map(int,v))==[1626,528,2310,2035,-1136,-1462,-1460,998,140,815,-378,-563,-216,418,-1634,-1249,23,-173,-1546,924,-1398,-630]
assert (v.T*G*v)[0]==-2*d*d and (v.T*G*h)[0]==0
R=I+v*(v.T*G)/d**2
assert s.ilcm(*[s.denom(z) for z in R])==3404025
assert R*R==I and R.T*G*R==G and R*h==h
print('RQT-218 PASS: exact denominator rigidity; global integral root OPEN')
