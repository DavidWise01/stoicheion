#!/usr/bin/env python3
"""RQT-212 exact verification. Input: original matrices and prior RQT reports."""
import ast,json
from pathlib import Path
import sympy as s
p=Path(__file__).resolve().parent
read=lambda n:s.Matrix(ast.literal_eval((p/'source'/n).read_text().strip()[7:-1]))
rep=lambda n:json.loads((p/f'RQT-{n}-report.json').read_text())
G=read('gram-22x22.txt');X=read('X-22x22.txt');I=s.eye(22);h=s.Matrix([1]*4+[0]*18)
K=s.Matrix.hstack(*[I[:,j]-I[:,0] if j<20 else I[:,j] for j in range(1,22)])
B=s.Matrix(rep(198)['basis_21x21']);GK=K.T*G*K;Y=(X*K)[1:22,:]
Q=B.T*GK*B;H=B.T*GK*(Y-s.eye(21)).inv()*B
T=s.Matrix.hstack(*[s.Matrix(v) for v in rep(201)['root_coefficients_in_index64_basis']])
for n,key in [(203,'fourth_root_coefficients'),(204,'fifth_root_lattice_coordinates'),(205,'root_lattice_coordinates'),(207,'root_lattice_coordinates'),(208,'root_lattice_coordinates'),(209,'root_lattice_coordinates'),(210,'root_lattice_coordinates'),(211,'root_lattice_coordinates')]:
 T=T.row_join(s.Matrix(rep(n)[key]))
A=T.T*H.T;N11=s.Matrix(json.loads((p/'RQT-211-kernel-basis.json').read_text()))
assert X**4==I and X.T*G*X==G and X*h==h and K*Y==X*K
assert abs(B.det())==64 and H.det()==1 and H+H.T==-Q
assert T.rank()==A.rank()==11 and N11.rank()==11
assert (T[:,:10].T*H.T*N11)==s.zeros(10,11)
a=A[10,:]*N11;C=a.copy();V=s.eye(11)
for j in range(1,11):
 aa,bb=int(C[0,0]),int(C[0,j])
 if not bb:continue
 if not aa:C.col_swap(0,j);V.col_swap(0,j);continue
 x,y,g=s.gcdex(aa,bb);x=int(x);y=int(y);g=int(g)
 ci,cj=C[:,0],C[:,j];vi,vj=V[:,0],V[:,j]
 C[:,0]=x*ci+y*cj;C[:,j]=(-bb//g)*ci+(aa//g)*cj
 V[:,0]=x*vi+y*vj;V[:,j]=(-bb//g)*vi+(aa//g)*vj
assert abs(V.det())==1 and abs(C[0,0])==1 and C[:,1:]==s.zeros(1,10)
from sympy.matrices.normalforms import hermite_normal_form
N=hermite_normal_form(N11*V[:,1:]);assert N.rank()==10 and A*N==s.zeros(11,10)
Z=N.T.lll().T;S=Z.T*Q*Z;assert S.det()==-869552306284552708
v=Z*s.Matrix([24,10,20,23,23,35,16,-18,8,19])
assert list(map(int,v))==[-27,101,467,-34,-58,-69,-120,-148,-492,-117,-1,17,-109,-214,-71,1,184,98,-214,170,-214] and A*v==s.zeros(11,1)
assert (v.T*Q*v)[0]==-2
U=T.row_join(v);J=U.T*H*U
assert U.rank()==12 and J.det()==1
assert all(J[i,i]==1 for i in range(12)) and all(J[i,j]==0 for i in range(12) for j in range(i))
assert U.T*Q*U==-J-J.T and list(map(int,J[:,11]))==[-4,34,-23,219,-3496,6287,503,114,321,-92,130,1]
r=K*B*v;assert list(map(int,r))==[211,391,336,467,-34,-58,-69,-120,-148,-492,-213,-32,17,-109,-214,-71,70,184,98,-214,126,-214]
assert (r.T*G*r)[0]==-2 and (h.T*G*r)[0]==0
R=I+r*(r.T*G);assert R*R==I and R.T*G*R==G and R*h==h
print('RQT-212 PASS: exact 12-root Wall flag; 21-root product remains OPEN')
