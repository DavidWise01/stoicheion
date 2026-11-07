#!/usr/bin/env python3
"""RQT-211 exact source-matrix verification of the 11th root."""
import ast,json
from pathlib import Path
import sympy as s
p=Path(__file__).resolve().parent
load=lambda n:s.Matrix(ast.literal_eval((p/'source'/n).read_text().strip()[7:-1]))
rep=lambda n:json.loads((p/f'RQT-{n}-report.json').read_text())
X=load('X-22x22.txt');G=load('gram-22x22.txt');I=s.eye(22);h=s.Matrix([1]*4+[0]*18)
K=s.Matrix.hstack(*[I[:,j]-I[:,0] if j<20 else I[:,j] for j in range(1,22)])
B=s.Matrix(rep(198)['basis_21x21'])
GK=K.T*G*K;Y=(X*K)[1:22,:];Q=B.T*GK*B;H=B.T*GK*(Y-s.eye(21)).inv()*B
T=s.Matrix.hstack(*[s.Matrix(z) for z in rep(201)['root_coefficients_in_index64_basis']])
for n,key in [(203,'fourth_root_coefficients'),(204,'fifth_root_lattice_coordinates'),(205,'root_lattice_coordinates'),(207,'root_lattice_coordinates'),(208,'root_lattice_coordinates'),(209,'root_lattice_coordinates'),(210,'root_lattice_coordinates')]:
 T=T.row_join(s.Matrix(rep(n)[key]))
A=T.T*H.T
v=s.Matrix([15,-49,-242,15,29,31,58,78,257,60,3,-10,61,115,41,2,-99,-56,114,-88,107])
assert X**4==I and X.T*G*X==G and X*h==h and K*Y==X*K
assert abs(B.det())==64 and H.det()==1 and H+H.T==-Q
assert A.rank()==10 and A*v==s.zeros(10,1) and (v.T*Q*v)[0]==-2
U=T.row_join(v);J=U.T*H*U
assert U.rank()==11 and J.det()==1
assert all(J[i,i]==1 for i in range(11))
assert all(J[i,j]==0 for i in range(11) for j in range(i))
assert U.T*Q*U==-J-J.T and list(map(int,J[:,10]))==[5,-14,10,-124,1808,-3265,-256,-67,-139,27,1]
r=K*B*v
assert list(map(int,r))==[-110,-204,-176,-242,15,29,31,58,78,257,113,22,-10,61,115,41,-37,-99,-56,114,-69,107]
assert (h.T*G*r)[0]==0 and (r.T*G*r)[0]==-2 and all(z.q==1 for z in r)
R=I+r*(r.T*G)
assert R**2==I and R.T*G*R==G and R*h==h
print('RQT-211 PASS: 11-root integral Wall flag; 21-root completion remains OPEN')
