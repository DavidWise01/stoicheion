#!/usr/bin/env python3
"""RQT-198 exact construction of index-64 Wall-integral lattice."""
import ast,itertools,json
from pathlib import Path
import sympy as s
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ
p=Path(__file__).resolve().parent
load=lambda n:s.Matrix(ast.literal_eval((p/'source'/n).read_text().strip()[7:-1]))
X=load('X-22x22.txt');G=load('gram-22x22.txt');I=s.eye(22)
h=s.Matrix([1]*4+[0]*18)
K=s.Matrix.hstack(*[I[:,j]-I[:,0] if j<20 else I[:,j] for j in range(1,22)])
GK=K.T*G*K;Y=(X*K)[1:22,:];W=GK*(Y-s.eye(21)).inv();Z=4*W
assert X.T*G*X==G and X**4==I and X*h==h
assert K*Y==X*K and GK.det()==-4 and W.det()==s.Rational(1,4096)
assert W+W.T==-GK
assert [abs(int(v)) for v in smith_normal_form(Z,domain=ZZ).diagonal()]==[1]*6+[4]*15
assert all((Z[i,j]+Z[j,i])%4==0 and Z[i,i]%4==0 for i in range(21) for j in range(21))
A=[[int(Z[j,i])%2 for j in range(21)] for i in range(21)]
piv=[];rank=0
for col in range(21):
 row=next((i for i in range(rank,21) if A[i][col]),None)
 if row is None:continue
 A[rank],A[row]=A[row],A[rank]
 for i in range(21):
  if i!=rank and A[i][col]:A[i]=[x^y for x,y in zip(A[i],A[rank])]
 piv.append(col);rank+=1
assert rank==6 and piv==[0,1,9,10,15,19]
E=s.eye(21);cols=[]
for j in range(21):
 if j in piv:v=2*E[:,j]
 else:
  v=E[:,j]
  for row,pi in enumerate(piv):
   if A[row][j]:v+=E[:,pi]
 cols.append(v)
B=s.Matrix.hstack(*cols);H=B.T*W*B;Q=B.T*GK*B
assert abs(B.det())==64 and all(v.q==1 for v in H)
assert H.det()==1 and Q.det()==-16384 and H+H.T==-Q
assert all((Z.T*B)[i,j]%2==0 for i in range(21) for j in range(21))
counts={};roots=[]
for n in range(1,4):
 count=0
 for ids in itertools.combinations(range(21),n):
  for signs in itertools.product((-1,1),repeat=n):
   norm=sum(signs[i]*signs[j]*int(Q[ids[i],ids[j]]) for i in range(n) for j in range(n))
   if norm==-2:
    count+=1;v=s.zeros(21,1)
    for i,sign in zip(ids,signs):v[i]=sign
    roots.append(v)
 counts[str(n)]=count
assert counts=={'1':2,'2':0,'3':0} and s.Matrix.hstack(*roots).rank()==1
out={'RQT':198,'status':'EXACT_WALL_INTEGRAL_INDEX64_PASS','pivots':piv,'index':64,
'det_W_on_L':1,'det_G_on_L':-16384,'root_counts_by_support':counts,
'sparse_root_span_rank':1,'minimum_candidates':[21,23],
'root_basis_upper_triangular':'OPEN','basis':[[int(q) for q in row] for row in B.tolist()]}
(p/'RQT-198-report.json').write_text(json.dumps(out,indent=2)+'\n')
print('RQT-198 PASS: index-64 Wall-integral unimodular lattice. 21-root factorization OPEN.')
