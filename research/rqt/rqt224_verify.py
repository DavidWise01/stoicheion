#!/usr/bin/env python3
"""RQT-224 exact sixteenth-root check, requires original matrices and prior root JSONs."""
import ast,json
from pathlib import Path
import sympy as s
p=Path(__file__).resolve().parent
load=lambda n:s.Matrix(ast.literal_eval((p/'source'/n).read_text().strip()[7:-1]))
rep=lambda n:json.loads((p/f'RQT-{n}-report.json').read_text())
G=load('gram-22x22.txt');X=load('X-22x22.txt');I=s.eye(22);h=s.Matrix([1]*4+[0]*18)
K=s.Matrix.hstack(*[I[:,j]-I[:,0] if j<20 else I[:,j] for j in range(1,22)])
B=s.Matrix(rep(198)['basis_21x21']);Z=s.Matrix(json.loads((p/'RQT-216-reduced-basis.json').read_text()))
GK=K.T*G*K;Y=(X*K)[1:22,:];Q=B.T*GK*B;H=B.T*GK*(Y-s.eye(21)).inv()*B
F=Z.T*Q*Z
assert F==s.Matrix(json.loads((p/'RQT-216-reduced-gram.json').read_text()))
T=s.Matrix.hstack(*[s.Matrix(z) for z in rep(201)['root_coefficients_in_index64_basis']])
for n,key in [(203,'fourth_root_coefficients'),(204,'fifth_root_lattice_coordinates'),(205,'root_lattice_coordinates'),(207,'root_lattice_coordinates'),(208,'root_lattice_coordinates'),(209,'root_lattice_coordinates'),(210,'root_lattice_coordinates'),(211,'root_lattice_coordinates'),(212,'root_lattice_coordinates'),(213,'root_lattice_coordinates'),(214,'root_lattice_coordinates'),(215,'root_lattice_coordinates')]:
 T=T.row_join(s.Matrix(rep(n)[key]))
A=T.T*H.T
z=s.Matrix([-183,-198,174,572,-368,-188]);b16=Z*z;r=K*B*b16
assert X.T*G*X==G and X*h==h and T.rank()==A.rank()==15
assert A*Z==s.zeros(15,6) and H+H.T==-Q and (z.T*F*z)[0]==-2
assert list(map(int,r))==[199942,383386,329827,461310,-41442,-52679,-65082,-125589,-153660,-481817,-207896,-25459,18678,-110547,-206072,-66620,69930,182115,99059,-207384,126089,-206587]
assert A*b16==s.zeros(15,1) and (r.T*G*r)[0]==-2 and (r.T*G*h)[0]==0
U=T.row_join(b16);J=U.T*H*U
assert U.rank()==16 and all(J[i,j]==0 for i in range(16) for j in range(i))
assert all(J[i,i]==1 for i in range(16)) and U.T*Q*U==-J-J.T
R=I+r*(r.T*G)
assert R*R==I and R.T*G*R==G and R*h==h
print('RQT-224 PASS: 16 exact integral Wall roots; full 21-word still OPEN')
