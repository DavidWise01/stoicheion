#!/usr/bin/env python3
"""RQT-209 exact ninth integral Wall root certificate, SymPy."""
import ast,json,hashlib
from pathlib import Path
import sympy as s
P=Path(__file__).resolve().parent
load=lambda n:s.Matrix(ast.literal_eval((P/'source'/n).read_text().strip()[7:-1]))
rep=lambda n:json.loads((P/f'RQT-{n}-report.json').read_text())
G=load('gram-22x22.txt');X=load('X-22x22.txt');I=s.eye(22);h=s.Matrix([1]*4+[0]*18)
K=s.Matrix.hstack(*[I[:,j]-I[:,0] if j<20 else I[:,j] for j in range(1,22)])
B=s.Matrix(rep(198)['basis_21x21']);GK=K.T*G*K;Y=(X*K)[1:22,:]
Q=B.T*GK*B;H=B.T*GK*(Y-s.eye(21)).inv()*B
T=s.Matrix.hstack(*[s.Matrix(v) for v in rep(201)['root_coefficients_in_index64_basis']])
for n,k in [(203,'fourth_root_coefficients'),(204,'fifth_root_lattice_coordinates'),(205,'root_lattice_coordinates'),(207,'root_lattice_coordinates'),(208,'root_lattice_coordinates')]:
 T=T.row_join(s.Matrix(rep(n)[k]))
A=T.T*H.T
assert X**4==I and X.T*G*X==G and X*h==h and K*Y==X*K
assert abs(B.det())==64 and H.det()==1 and H+H.T==-Q
assert T.rank()==A.rank()==8
C=A.copy();V=s.eye(21)
for i in range(8):
 for j in range(i+1,21):
  a,b=int(C[i,i]),int(C[i,j])
  if b==0:continue
  if a==0:C.col_swap(i,j);V.col_swap(i,j);continue
  x,y,g=s.gcdex(a,b);x=int(x);y=int(y);g=int(g)
  ci,cj=C[:,i],C[:,j];vi,vj=V[:,i],V[:,j]
  C[:,i]=x*ci+y*cj;C[:,j]=(-b//g)*ci+(a//g)*cj
  V[:,i]=x*vi+y*vj;V[:,j]=(-b//g)*vi+(a//g)*vj
assert A*V==C and C[:,8:]==s.zeros(8,13) and abs(V.det())==1
N=V[:,8:];assert N.rank()==13 and A*N==s.zeros(8,13)
RED,U=N.T.lll_transform();assert abs(U.det())==1
coeff=s.Matrix([-45,3,10,-1,44,27,22,36,-34,22,12,-28,-22]);v=RED.T*coeff
expected=[2,-21,-111,8,14,8,30,38,116,23,-1,-5,34,54,18,0,-42,-30,56,-40,45]
assert list(map(int,v))==expected and A*v==s.zeros(8,1) and (v.T*Q*v)[0]==-2
T9=T.row_join(v);J=T9.T*H*T9
assert T9.rank()==9 and all(J[i,i]==1 for i in range(9))
assert all(J[i,j]==0 for i in range(9) for j in range(i)) and T9.T*Q*T9==-J-J.T
assert list(map(int,J[:,8]))==[8,-4,4,-50,846,-1285,-81,-15,1]
r=K*B*v
assert list(map(int,r))==[-48,-97,-88,-111,8,14,8,30,38,116,51,10,-5,34,54,18,-16,-42,-30,56,-35,45]
assert all(x.q==1 for x in r) and (r.T*G*r)[0]==-2 and (h.T*G*r)[0]==0
R=I+r*(r.T*G)
assert R**2==I and R.T*G*R==G and R*h==h
out={'RQT':209,'status':'NINTH_EXACT_INTEGRAL_WALL_ROOT_PASS','constraint_rank':8,
'saturated_kernel_rank':13,'kernel_Gram_determinant':str((N.T*Q*N).det()),
'reduced_kernel_coefficients':list(map(int,coeff)),'root_lattice_coordinates':expected,
'root_original_coordinates':list(map(int,r)),'Wall_column_nine':list(map(int,J[:,8])),
'Wall_matrix_9x9':[[int(z) for z in row] for row in J.tolist()],
'full_21_root_word':'OPEN','minimal_word_candidates':[21,23],
'source_sha256':{n:hashlib.sha256((P/'source'/n).read_bytes()).hexdigest() for n in ['X-22x22.txt','gram-22x22.txt']}}
(P/'RQT-209-report.json').write_text(json.dumps(out,indent=2)+'\n')
print('RQT-209 PASS: ninth exact integral Wall root; full 21-word OPEN')
