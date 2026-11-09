#!/usr/bin/env python3
"""RQT-255 exact binary residual order-three and 36 product identities."""
import itertools,json,collections
from pathlib import Path
d=json.loads((Path(__file__).resolve().parent/'RQT-242-preliminary.json').read_text())
F=[[int(t)%2 for t in row] for row in d['F4']]
H=[[int(t)%2 for t in row] for row in d['W4']]
D=[[int(t)%2 for t in row] for row in d['D4']]
I=[[int(i==j) for j in range(4)] for i in range(4)]
def mul(A,B):return [[sum(A[i][k]*B[k][j] for k in range(len(B)))%2 for j in range(len(B[0]))] for i in range(len(A))]
def vm(A,v):return [sum(A[i][j]*v[j] for j in range(len(v)))%2 for i in range(len(A))]
def dot(A,x,y):return sum(x[i]*A[i][j]*y[j] for i in range(len(x)) for j in range(len(y)))%2
def refl(v):
 fv=[sum(v[k]*F[k][j] for k in range(4))%2 for j in range(4)]
 return [[(int(i==j)+v[i]*fv[j])%2 for j in range(4)] for i in range(4)]
assert mul(mul(D,D),D)==I and D!=I
assert mul([list(x) for x in zip(*D)],mul(F,D))==F
R=[v for v in itertools.product(range(2),repeat=4) if vm(F,v)==[0]*4]
assert R==[(0,0,0,0),(0,1,0,0),(1,0,1,1),(1,1,1,1)]
assert all(vm(D,v)==list(v) for v in R)
e0=(1,0,0,0);e2=(0,0,1,0)
assert tuple((x+y)%2 for x,y in zip(vm(D,e0),e2)) in R
assert tuple((x+y+z)%2 for x,y,z in zip(vm(D,e2),e0,e2)) in R
Q=[[0,1],[1,1]]
assert mul(mul(Q,Q),Q)==[[1,0],[0,1]] and Q!=[[1,0],[0,1]]
E=[v for v in itertools.product(range(2),repeat=4) if dot(H,v,v)==1]
assert len(E)==8
rad=[v for v in E if v in R]
assert rad==[(1,0,1,1),(1,1,1,1)] and all(refl(v)==I for v in rad)
patterns=collections.Counter();pairs=set();count=0
for vs in itertools.product(E,repeat=4):
 if any(dot(H,vs[j],vs[i]) for j in range(1,4) for i in range(j)):continue
 S=I
 for v in vs:S=mul(S,refl(v))
 assert S==D
 patterns[tuple(i for i,v in enumerate(vs) if v in R)]+=1
 pairs.add(tuple(v for v in vs if v not in R))
 count+=1
assert count==36 and len(patterns)==6 and set(patterns.values())=={6}
assert len(pairs)==3
print('RQT-255 PASS: order-three quotient, 36 flags, all 36 products equal D mod2')
print('Global integral roots18–21 OPEN')
