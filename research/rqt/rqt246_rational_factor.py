#!/usr/bin/env python3
"""RQT-246: deterministic rational Cartan–Dieudonné factorization.
Requires the frozen RQT-242-preliminary.json in the same directory.
Uses exact SymPy arithmetic: no floating point.
"""
import itertools,json
from pathlib import Path
import sympy as s

p=Path(__file__).resolve().parent
src=json.loads((p/'RQT-242-preliminary.json').read_text())
F=s.Matrix(src['F4']);D=s.Matrix(src['D4']);I=s.eye(4)
assert F==F.T and D.T*F*D==F and D.det()==1 and (D-I).rank()==4

R=D; product=I; roots=[]; norms=[]
probes=[s.Matrix([0,0,-1,1]),s.Matrix([-1,0,0,1]),
        s.Matrix([1,0,0,0]),s.Matrix([0,1,0,0])]
for i,v in enumerate(probes):
 r=(R-I)*v
 q=(r.T*F*r)[0]
 assert q!=0
 S=I-2*r*(r.T*F)/q
 assert S*S==I and S.T*F*S==F and S.det()==-1
 R=S*R
 product=product*S
 assert (R-I).rank()==3-i
 roots.append(r);norms.append(q)
assert product==D and R==I
norm_product=s.prod(norms)
assert s.sqrt(norm_product).is_Integer
assert s.sqrt((I+D).det()).is_Integer
print('PASS: D4 equals four rational reflections exactly; ranks 4,3,2,1,0')
print('Norm product square root:',s.sqrt(norm_product))
print('det(I+D4) square root:',s.sqrt((I+D).det()))
print('Integral norm-minus-two completion remains OPEN')
