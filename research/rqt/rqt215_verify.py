#!/usr/bin/env python3
"""RQT-215 exact fifteenth-root audit. Run inside the RQT-215 evidence bundle."""
import ast,json
from pathlib import Path
import sympy as s
p=Path(__file__).resolve().parent
read=lambda n:s.Matrix(ast.literal_eval((p/'source'/n).read_text().strip()[7:-1]))
rep=lambda n:json.loads((p/f'RQT-{n}-report.json').read_text())
G=read('gram-22x22.txt');X=read('X-22x22.txt');I=s.eye(22)
h=s.Matrix([1]*4+[0]*18)
K=s.Matrix.hstack(*[I[:,j]-I[:,0] if j<20 else I[:,j] for j in range(1,22)])
B=s.Matrix(rep(198)['basis_21x21']);GK=K.T*G*K
Y=(X*K)[1:22,:];Q=B.T*GK*B;H=B.T*GK*(Y-s.eye(21)).inv()*B
T=s.Matrix.hstack(*[s.Matrix(z) for z in rep(201)['root_coefficients_in_index64_basis']])
for n,k in [(203,'fourth_root_coefficients'),(204,'fifth_root_lattice_coordinates'),(205,'root_lattice_coordinates'),(207,'root_lattice_coordinates'),(208,'root_lattice_coordinates'),(209,'root_lattice_coordinates'),(210,'root_lattice_coordinates'),(211,'root_lattice_coordinates'),(212,'root_lattice_coordinates'),(213,'root_lattice_coordinates'),(214,'root_lattice_coordinates')]:
 T=T.row_join(s.Matrix(rep(n)[k]))
A=T.T*H.T
N=s.Matrix(json.loads((p/'RQT-215-kernel-basis.json').read_text()))
Z=s.Matrix(json.loads((p/'RQT-215-reduced-basis.json').read_text()))
S=Z.T*Q*Z
v=Z*s.Matrix([-176,-74,51,-13,94,8,-71])
assert X.T*G*X==G and X*h==h and H.det()==1 and H+H.T==-Q
assert A.rank()==14 and N.rank()==7 and A*N==s.zeros(14,7)
assert S.det()==18369518910500574521749122
assert list(map(int,v))==[1455,-4653,-23402,2094,2636,3257,6296,7701,24421,5828,28,-905,5688,10595,3465,44,-9304,-5021,10574,-8456,10492]
assert A*v==s.zeros(14,1) and (v.T*Q*v)[0]==-2
U=T.row_join(v);J=U.T*H*U
assert U.rank()==15 and U.T*Q*U==-J-J.T
assert all(J[i,i]==1 for i in range(15))
assert all(J[i,j]==0 for i in range(15) for j in range(i))
assert list(map(int,J[:,14]))==[-3,-2013,740,-10916,163288,-328774,-26295,-6344,-17638,6255,-11093,9128,-14749,37553,1]
rr=K*B*v
assert list(map(int,rr))==[-10125,-19459,-16795,-23402,2094,2636,3257,6296,7701,24421,10600,1347,-905,5688,10595,3465,-3663,-9304,-5021,10574,-6420,10492]
R=I+rr*(rr.T*G)
assert (rr.T*G*rr)[0]==-2 and (h.T*G*rr)[0]==0
assert R**2==I and R.T*G*R==G and R*h==h
print('RQT-215 PASS: exact 15-root Wall flag; full factorization OPEN')
