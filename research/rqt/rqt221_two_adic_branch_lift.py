#!/usr/bin/env python3
"""RQT-221: exact 2-adic branch lifts (not ordinary integral norm -2 roots)."""
import ast,json
from pathlib import Path
import sympy as s
p=Path(__file__).resolve().parent
read=lambda n:s.Matrix(ast.literal_eval((p/'source'/n).read_text().strip()[7:-1]))
G=read('gram-22x22.txt');X=read('X-22x22.txt');I=s.eye(22)
h=s.Matrix([1]*4+[0]*18)
K=s.Matrix.hstack(*[I[:,j]-I[:,0] if j<20 else I[:,j] for j in range(1,22)])
B=s.Matrix(json.loads((p/'RQT-198-report.json').read_text())['basis_21x21'])
Z=s.Matrix(json.loads((p/'RQT-216-reduced-basis.json').read_text()))
F=s.Matrix(json.loads((p/'RQT-216-reduced-gram.json').read_text()))
assert X.T*G*X==G and X*h==h and Z.T*B.T*K.T*G*K*B*Z==F
assert F.det()==-313982794406122741723132503868
for a0,j,expected in [([0,0,1,1,0,1],3,6499668843087076870),([1,1,0,1,0,0],1,3886618388119862109)]:
 a=s.Matrix(a0);e=s.eye(6)[:,j]
 q=int((a.T*F*a)[0]);p0=int((a.T*F*e)[0]);fjj=int(F[j,j])
 assert (q+2)%8==0 and p0%2==0 and fjj%2==0
 c=(q+2)//8;b=p0//2;d=fjj//2
 assert b%2==1 and d%2==0
 t=0
 for bit in range(1,65):
  if (c+b*t+d*t*t)%(1<<bit):t+=1<<(bit-1)
  assert (c+b*t+d*t*t)%(1<<bit)==0
 assert t==expected
 r=a+2*t*e
 assert (int((r.T*F*r)[0])+2)%(1<<67)==0
 assert all(int(v)%2==0 for v in F*r)
 assert any(int(v)%4==2 for v in F*r)
 ambient=K*B*Z*r
 assert (int((ambient.T*G*ambient)[0])+2)%(1<<67)==0
 assert (h.T*G*ambient)[0]==0
print('RQT-221 PASS: both d=2 classes lift to Z_2; global integral root OPEN')
