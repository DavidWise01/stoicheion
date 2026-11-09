#!/usr/bin/env python3
"""Exact RQT-250 binary and mod4 flag census; needs RQT-242-preliminary.json."""
import itertools,json
from pathlib import Path
from collections import Counter
import sympy as s
src=json.loads((Path(__file__).resolve().parent/'RQT-242-preliminary.json').read_text())
F=s.Matrix(src['F4']); H=s.Matrix(src['W4'])
assert H.det()==1 and H+H.T==-F
def dot(M,x,y,m):return sum(x[i]*int(M[i,j])*y[j] for i in range(4) for j in range(4))%m
def radical(x):return all(sum(int(F[i,j])*x[j] for j in range(4))%2==0 for i in range(4))
def flags(E,m):
 S={a:[b for b in E if dot(H,b,a,m)==0] for a in E}
 for a in E:
  for b in S[a]:
   for c in S[a]:
    if c not in S[b]:continue
    for d in S[a]:
     if d in S[b] and d in S[c]:yield(a,b,c,d)
E2=[v for v in itertools.product(range(2),repeat=4) if dot(H,v,v,2)==1]
F2=list(flags(E2,2))
assert len(E2)==8 and len(F2)==36
assert {x for x in E2 if radical(x)}=={(1,0,1,1),(1,1,1,1)}
assert all(sum(radical(x) for x in flag)==2 for flag in F2)
assert all(int(s.Matrix.hstack(*map(s.Matrix,flag)).det())%2 for flag in F2)
E4=[v for v in itertools.product(range(4),repeat=4) if dot(F,v,v,8)==6]
C=Counter(tuple(tuple(t%2 for t in x) for x in flag) for flag in flags(E4,4))
assert len(E4)==80 and len(C)==36 and sum(C.values())==18432
assert set(C)==set(F2) and set(C.values())=={512}
print('RQT-250 PASS: 8 binary roots, 36 binary flags, 512 lifts each')
print('RQT-250 PASS: 80 mod4 root residues, 18432 mod4 flags')
print('Integral root18 and 21-reflection equality: OPEN')
