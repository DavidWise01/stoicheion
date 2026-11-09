#!/usr/bin/env python3
"""RQT-252 exact verifier. Inputs: RQT-242-preliminary.json and
RQT-252-mod64-report.json in same directory (both in the archived evidence ZIP).
Reconstructs all binary flags independently and checks each integer matrix.
"""
import itertools,json
from pathlib import Path
import sympy as s
p=Path(__file__).resolve().parent
d=json.loads((p/'RQT-242-preliminary.json').read_text())
F=s.Matrix(d['F4']); H=s.Matrix(d['W4'])
data=json.loads((p/'RQT-252-mod64-report.json').read_text())
assert H.det()==1 and H+H.T==-F
assert data['modulus']==64 and data['total']==36
def dot(M,a,b):return (s.Matrix(a).T*M*s.Matrix(b))[0]
roots=[a for a in itertools.product(range(2),repeat=4) if dot(H,a,a)%2==1]
flags=set()
for a in roots:
 for b in roots:
  if dot(H,b,a)%2:continue
  for c in roots:
   if dot(H,c,a)%2 or dot(H,c,b)%2:continue
   for z in roots:
    if dot(H,z,a)%2 or dot(H,z,b)%2 or dot(H,z,c)%2:continue
    V=s.Matrix.hstack(*(s.Matrix(t) for t in (a,b,c,z)))
    assert V.det()%2==1
    flags.add((a,b,c,z))
assert len(flags)==36
seen=set()
for item in data['witnesses']:
 key=tuple(tuple(a) for a in item['binary'])
 assert key in flags and key not in seen
 seen.add(key)
 C=[s.Matrix(v) for v in item['columns']]
 V=s.Matrix.hstack(*C)
 assert all(tuple(int(t)%2 for t in v)==x for v,x in zip(C,key))
 assert all(0<=int(t)<64 for v in C for t in v)
 assert V.det()%2==1
 assert all((dot(F,v,v)+2)%128==0 for v in C)
 assert all(dot(H,C[j],C[i])%64==0 for j in range(1,4) for i in range(j))
 assert all((dot(H,v,v)-1)%64==0 for v in C)
assert seen==flags
print('PASS all 36 binary flags, each with one 4-column witness mod64')
print('PASS all norms -2 mod128, all lower Wall products 0 mod64')
print('Integral root18: OPEN')
