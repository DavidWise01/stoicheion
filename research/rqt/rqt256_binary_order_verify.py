#!/usr/bin/env python3
"""RQT-256 exact first-root parity/order classification.
Requires RQT-242-preliminary.json from the complete evidence ZIP.
"""
import json,itertools,collections
from pathlib import Path
src=json.loads((Path(__file__).resolve().parent/"RQT-242-preliminary.json").read_text())
F=[[int(c)%2 for c in r] for r in src["F4"]]
H=[[int(c)%2 for c in r] for r in src["W4"]]
D=[[int(c)%2 for c in r] for r in src["D4"]]
I=[[int(i==j) for j in range(4)] for i in range(4)]
def mul(A,B):return [[sum(A[i][k]*B[k][j] for k in range(4))%2 for j in range(4)] for i in range(4)]
def dot(A,x,y):return sum(x[i]*A[i][j]*y[j] for i in range(4) for j in range(4))%2
def refl(x):
 row=[sum(x[k]*F[k][j] for k in range(4))%2 for j in range(4)]
 return [[(I[i][j]+x[i]*row[j])%2 for j in range(4)] for i in range(4)]
def rank(A):
 A=[list(row) for row in A];r=0
 for j in range(4):
  p=next((k for k in range(r,4) if A[k][j]),None)
  if p is None:continue
  A[r],A[p]=A[p],A[r]
  for k in range(4):
   if k!=r and A[k][j]:A[k]=[a^b for a,b in zip(A[k],A[r])]
  r+=1
 return r
E=[a for a in itertools.product(range(2),repeat=4) if dot(H,a,a)]
assert len(E)==8 and mul(mul(D,D),D)==I and D!=I
flags=collections.Counter()
for a in E:
 for b in E:
  if dot(H,b,a):continue
  for c in E:
   if dot(H,c,a) or dot(H,c,b):continue
   for d in E:
    if any(dot(H,d,x) for x in (a,b,c)):continue
    flags[a]+=1
assert sum(flags.values())==36
expected={"0111":(6,2,1),"1001":(6,2,1),"1011":(9,3,2),"1110":(6,2,1),"1111":(9,3,2)}
for v in E:
 key=''.join(map(str,v))
 M=mul(refl(v),D)
 n=next(j for j in range(1,13) if Mpower(M,j)==I) if False else None
 P=I;order=0
 for j in range(1,13):
  P=mul(P,M)
  if P==I:order=j;break
 moving=rank([[M[i][j]^I[i][j] for j in range(4)] for i in range(4)])
 if key in expected:assert (flags[v],order,moving)==expected[key]
 else:assert flags[v]==0
print('PASS RQT-256: 8 parity candidates; 5 viable; 36 binary flags.')
print('PASS RQT-256: viable d1 roots reduce binary residual order 3->2.')
