#!/usr/bin/env python3
"""Exact RQT-197 Wall form necessary condition, original source."""
import ast,json,hashlib
from collections import Counter
from functools import reduce
from math import lcm
from pathlib import Path
import sympy as s
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ
p=Path(__file__).resolve().parent
load=lambda n:s.Matrix(ast.literal_eval((p/'source'/n).read_text().strip()[7:-1]))
X=load('X-22x22.txt');G=load('gram-22x22.txt');I=s.eye(22)
h=s.Matrix([1]*4+[0]*18)
K=s.Matrix.hstack(*[I[:,j]-I[:,0] if j<20 else I[:,j] for j in range(1,22)])
GK=K.T*G*K;Y=(X*K)[1:22,:];D=Y-s.eye(21)
assert K*Y==X*K and GK.det()==-4 and D.det()==-16384
W=GK*D.inv()
assert W+W.T==-GK and W.det()==s.Rational(1,4096)
assert reduce(lcm,(int(q.q) for q in W),1)==4
Z=4*W
assert all(q.q==1 for q in Z)
SN=smith_normal_form(Z,domain=ZZ)
snf=[abs(int(SN[i,i])) for i in range(21)]
assert snf==[1]*6+[4]*15
roots=[s.Matrix(v) for v in json.loads((p/'RQT-195-hurwitz-proof.json').read_text())['final_roots']]
assert len(roots)==23
B=s.Matrix.hstack(*[r[1:22,0] for r in roots])
assert K*B==s.Matrix.hstack(*roots)
P=I
for r in roots:
 assert (r.T*G*r)[0]==-2 and (h.T*G*r)[0]==0
 P=P*(I+r*(r.T*G))
assert P==X and B.rank()==21
M=B.T*W*B
assert M+M.T==-B.T*GK*B
assert all(M[i,i]==1 for i in range(23))
counts={str(k):v for k,v in sorted(Counter(int(q.q) for q in M).items())}
assert counts=={'1':397,'2':36,'4':96} and M[0,13]==-s.Rational(3,4)
result={'boundary':'RQT-197','status':'EXACT_WALL_FORM_NECESSARY_CONDITIONS','det_W':'1/4096','wall_denominator':4,'smith_4W':snf,'candidate_21_basis_index':64,'candidate_21_basis_condition':'B^T W B upper-unitriangular integral','existing_23_wall_entry_denominators':counts,'example':'W(r1,r14)=-3/4','21_word':'OPEN'}
(p/'RQT-197-report.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
