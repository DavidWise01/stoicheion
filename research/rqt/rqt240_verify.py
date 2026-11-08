#!/usr/bin/env python3
"""RQT-240 exact residual rank-descent identity; full original-source replay in ZIP."""
import json
from pathlib import Path
import sympy as s
p=Path(__file__).resolve().parent
a=json.loads((p/'branch_2.json').read_text())
F=s.Matrix(a['Gram_5x5']); H=s.Matrix(a['Wall_5x5'])
D=s.Matrix(a['reduced_residual_action_5x5']); I=s.eye(5)
assert F==F.T and all(int(F[i,i])%2==0 for i in range(5))
assert F.det()==312669187727137013416789354039323478
assert H.det()==1 and H+H.T==-F and D.T*F*D==F
assert D-I==H.inv()*F
assert (D-I).det()==F.det()
for coords in ([1,0,0,0,0],[0,1,2,0,1],[2,-3,5,-7,11],[1,1,1,1,1]):
 r=s.Matrix(coords); q=(r.T*F*r)[0]
 sr=I+r*(r.T*F)
 assert (sr*D-I).det()==(D-I).det()*(1+q/2)
 assert (r.T*H*r)[0]==-q/2
 assert (r.T*F*D*(D-I).inv()*r)[0]==q/2
print('PASS: exact residual, universal determinant identity; explicit root17 remains OPEN')
