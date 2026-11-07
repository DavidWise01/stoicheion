#!/usr/bin/env python3
"""RQT-201 exact support<=6 root enumeration and three-root Wall chain."""
import ast,itertools,json
from pathlib import Path
import numpy as np
import sympy as s
p=Path(__file__).resolve().parent
load=lambda n:s.Matrix(ast.literal_eval((p/'source'/n).read_text().strip()[7:-1]))
X=load('X-22x22.txt');G=load('gram-22x22.txt');I=s.eye(22);h=s.Matrix([1]*4+[0]*18)
K=s.Matrix.hstack(*[I[:,j]-I[:,0] if j<20 else I[:,j] for j in range(1,22)])
B=s.Matrix(json.loads((p/'RQT-198-report.json').read_text())['basis_21x21'])
GK=K.T*G*K;Y=(X*K)[1:22,:];W=GK*(Y-s.eye(21)).inv();Q=B.T*GK*B;H=B.T*W*B
assert X.T*G*X==G and X*h==h and abs(B.det())==64 and H.det()==1
assert H+H.T==-Q and all(v.q==1 for v in H)
q=np.array(Q.tolist(),dtype=np.int64);counts={};roots={}
for n in range(1,7):
 signs=np.array(list(itertools.product((-1,1),repeat=n)),dtype=np.int64)
 total=0
 for ids in itertools.combinations(range(21),n):
  block=q[np.ix_(ids,ids)]
  norm=np.full(len(signs),np.trace(block),dtype=np.int64)
  for a in range(n):
   for b in range(a+1,n):norm+=2*int(block[a,b])*signs[:,a]*signs[:,b]
  for j in np.flatnonzero(norm==-2):
   v=np.zeros(21,dtype=np.int64);v[list(ids)]=signs[j]
   t=tuple(map(int,v));roots[t]=True;total+=1
 counts[str(n)]=total
assert counts=={'1':2,'2':0,'3':0,'4':0,'5':2,'6':2}
assert len(roots)==6
vectors=[]
for parts in [[(20,1)],[(9,1),(12,-1),(14,-1),(17,1),(20,1)],[(1,1),(2,1),(3,-1),(5,-1),(17,-1),(20,-1)]]:
 v=s.zeros(21,1)
 for i,c in parts:v[i]=c
 assert tuple(map(int,v)) in roots
 vectors.append(v)
T=s.Matrix.hstack(*vectors);Z=K*B*T
assert T.rank()==3 and T.T*Q*T==-2*s.eye(3) and T.T*H*T==s.eye(3)
assert h.T*G*Z==s.zeros(1,3) and Z.T*G*Z==-2*s.eye(3)
for j in range(3):
 r=Z[:,j];R=I+r*(r.T*G)
 assert all(z.q==1 for z in r) and R**2==I and R.T*G*R==G and R*h==h
report={'RQT':201,'status':'EXACT_THREE_ROOT_WALL_FLAG','counts':counts,'rank':3,
'Q_on_roots':(-2*s.eye(3)).tolist(),'Wall_on_roots':s.eye(3).tolist(),
'coefficients':[[int(x) for x in v] for v in vectors],
'ambient_roots':[[int(x) for x in Z[:,j]] for j in range(3)],
'21_root_word':'OPEN'}
(p/'RQT-201-report.json').write_text(json.dumps(report,indent=2,default=int)+'\n')
print('RQT-201 PASS:',counts,'three independent Wall-orthogonal integral roots')
