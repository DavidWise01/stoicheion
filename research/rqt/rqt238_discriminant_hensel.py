#!/usr/bin/env python3
"""RQT-238 small exact discriminant/Hensel check; full original-source replay is in the ZIP."""
import itertools,json
import sympy as s
from pathlib import Path
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ
p=Path(__file__).resolve().parent
d=json.loads((p/'branch_2.json').read_text())
F=s.Matrix(d['Gram_5x5'])
assert [abs(int(smith_normal_form(F,domain=ZZ)[i,i])) for i in range(5)]==[1,1,1,1,312669187727137013416789354039323478]
assert {tuple(v) for v in itertools.product(range(2),repeat=5) if all(int(k)%2==0 for k in F*s.Matrix(v))}=={(0,0,0,0,0),(0,0,0,0,1)}
a=s.Matrix([0,0,0,0,1]);e=s.eye(5)[:,0]
assert s.Rational((a.T*F*a)[0],4)%2==s.Rational(3,2)
screen=json.loads((p/'first_root_screen.json').read_text())
accepted=[]
for r in screen['viable_root17_residues']:
 v=s.Matrix(r);q=int((v.T*F*v)[0])
 if q%16==14 or any(int(k)%2 for k in F*v):accepted.append(r)
assert len(accepted)==132
assert sum(all(int(k)%2==0 for k in F*s.Matrix(v)) for v in accepted)==12
assert sum(any(int(k)%2 for k in F*s.Matrix(v)) for v in accepted)==120
A=int(((a.T*F*a)[0]+2)/8);B=int((a.T*F*e)[0]/2);C=int((e.T*F*e)[0]/2)
assert (A,B,C)==(-50401690,-162145929,-165967762)
t=0
for n in range(1,129):
 if (A+B*t+C*t*t)%(1<<n):t+=1<<(n-1)
 assert (A+B*t+C*t*t)%(1<<n)==0
assert t==216126377552887896659684962905481850670
assert ((a+2*t*e).T*F*(a+2*t*e))[0]% (1<<131)==((1<<131)-2)
print('PASS: cyclic discriminant, 120/12 split and mod-2^131 local root')
