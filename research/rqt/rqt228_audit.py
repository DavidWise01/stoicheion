#!/usr/bin/env python3
"""RQT-228: verify reduced Gram, exact full support, finite exhaustive root search."""
import json,math,itertools
from pathlib import Path
import sympy as s
p=Path(__file__).resolve().parent
F=s.Matrix(json.loads((p/'RQT-228-gram-4x4.json').read_text()))
assert F==F.T and F.det()==-7154513768473386414464298429235934347540076220
for omitted in range(4):
 ids=[i for i in range(4) if i!=omitted]
 A=-F.extract(ids,ids)
 assert all(A[:k,:k].det()>0 for k in range(1,4))
f=[[int(F[i,j]) for j in range(4)] for i in range(4)]
for mod,expect in [(4,128),(8,1024),(16,8192)]:
 n=0
 for x in itertools.product(range(mod),repeat=4):
  y=[sum(f[i][j]*x[j] for j in range(4)) for i in range(4)]
  n+=(sum(x[i]*y[i] for i in range(4))+2)%mod==0
 assert n==expect
a=f[3][3];roots=[]
for x in itertools.product(range(-100,101),repeat=3):
 b=2*sum(f[3][i]*x[i] for i in range(3))
 c=2+sum(f[i][i]*x[i]*x[i] for i in range(3))+sum(2*f[i][j]*x[i]*x[j] for i in range(3) for j in range(i+1,3))
 d=b*b-4*a*c
 if d<0:continue
 t=math.isqrt(d)
 if t*t!=d:continue
 for sign in [-1,1]:
  z=-b+sign*t
  if z%(2*a)==0:roots.append(x+(z//(2*a),))
assert not roots
print('RQT-228 PASS: exact rank-four Gram, full-support theorem, 8,120,601 triples, zero roots.')
