#!/usr/bin/env python3
"""RQT-200: exact exhaustive binary quadratic census on RQT-198 lattice."""
import ast,itertools,json
from pathlib import Path
import numpy as np
import sympy as s
p=Path(__file__).resolve().parent
load=lambda n:s.Matrix(ast.literal_eval((p/'source'/n).read_text().strip()[7:-1]))
X=load('X-22x22.txt');G=load('gram-22x22.txt');I=s.eye(22)
h=s.Matrix([1]*4+[0]*18)
K=s.Matrix.hstack(*[I[:,j]-I[:,0] if j<20 else I[:,j] for j in range(1,22)])
B=s.Matrix(json.loads((p/'RQT-198-report.json').read_text())['basis_21x21'])
GK=K.T*G*K;Y=(X*K)[1:22,:];W=GK*(Y-s.eye(21)).inv();Q=B.T*GK*B;H=B.T*W*B
assert X.T*G*X==G and X*h==h and abs(B.det())==64
assert Q.det()==-16384 and H.det()==1 and all(z.q==1 for z in H)
assert H+H.T==-Q and all(int(Q[i,i])%2==0 for i in range(21))
n=21
def echelon(vectors):
 base={}
 for v in vectors:
  v=int(v)
  while v:
   k=v.bit_length()-1
   if k not in base:base[k]=v;break
   v^=base[k]
 return base
rows=[sum((int(Q[i,j])&1)<<j for j in range(n)) for i in range(n)]
assert len(echelon(rows))==8
# Compute the GF(2) radical and check the quadratic refinement vanishes.
a=rows[:];piv=[];r=0
for j in range(n):
 t=next((k for k in range(r,n) if (a[k]>>j)&1),None)
 if t is None:continue
 a[t],a[r]=a[r],a[t]
 for k in range(n):
  if k!=r and ((a[k]>>j)&1):a[k]^=a[r]
 piv.append(j);r+=1
rad=[]
for j in range(n):
 if j in piv:continue
 v=1<<j
 for i,k in enumerate(piv):
  if (a[i]>>j)&1:v|=1<<k
 rad.append(v)
def q4(v):
 ids=[i for i in range(n) if (v>>i)&1]
 return sum(int(Q[i,j]) for i in ids for j in ids)%4
assert len(rad)==13 and all(q4(v)==0 for v in rad)
# Exactly enumerate all 2^21 vectors in 32K chunks.
mod=np.array(Q.tolist(),dtype=np.int64)%4
count=0;rankspan={}
for lo in range(0,1<<n,32768):
 vals=np.arange(lo,lo+32768,dtype=np.uint32)
 bits=((vals[:,None]>>np.arange(n,dtype=np.uint32))&1).astype(np.int64)
 norms=np.einsum('ni,ij,nj->n',bits,mod,bits,optimize=True)%4
 hits=np.flatnonzero(norms==2)
 count+=len(hits)
 for idx in hits:
  v=int(vals[idx])
  while v:
   k=v.bit_length()-1
   if k not in rankspan:rankspan[k]=v;break
   v^=rankspan[k]
assert count==983040 and len(rankspan)==21
assert count==2**13*(2**7-2**3)
selected=[];basis={};counts={}
for support in (1,2):
 c=0
 for ids in itertools.combinations(range(n),support):
  v=sum(1<<i for i in ids)
  if q4(v)!=2:continue
  c+=1;w=v
  while w:
   k=w.bit_length()-1
   if k not in basis:basis[k]=w;selected.append(list(ids));break
   w^=basis[k]
 counts[str(support)]=c
assert counts=={'1':11,'2':122} and len(basis)==21
out={'RQT':200,'status':'EXACT_BINARY_QUADRATIC_CENSUS_PASS',
 'binary_classes':2**21,'norm_compatible_classes':count,'polar_rank':8,
 'radical_dimension':13,'Arf':0,'compatible_span_rank':21,
 'support_counts':counts,'21_independent_parities':selected,
 'actual_21_root_word':'OPEN','minimum_candidates':[21,23]}
(p/'RQT-200-report.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
