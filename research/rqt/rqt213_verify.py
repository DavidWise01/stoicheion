#!/usr/bin/env python3
"""RQT-213 reproduction, exact integer matrix verification. Needs SymPy, NumPy."""
from pathlib import Path
import ast,json
import sympy as s
p=Path(__file__).resolve().parent
read=lambda n:s.Matrix(ast.literal_eval((p/'source'/n).read_text().strip()[7:-1]))
rep=lambda n:json.loads((p/f'RQT-{n}-report.json').read_text())
G=read('gram-22x22.txt');X=read('X-22x22.txt');I=s.eye(22)
h=s.Matrix([1]*4+[0]*18)
K=s.Matrix.hstack(*[I[:,j]-I[:,0] if j<20 else I[:,j] for j in range(1,22)])
B=s.Matrix(rep(198)['basis_21x21'])
GK=K.T*G*K;Y=(X*K)[1:22,:];Q=B.T*GK*B;H=B.T*GK*(Y-s.eye(21)).inv()*B
T=s.Matrix.hstack(*[s.Matrix(z) for z in rep(201)['root_coefficients_in_index64_basis']])
for n,key in [(203,'fourth_root_coefficients'),(204,'fifth_root_lattice_coordinates'),(205,'root_lattice_coordinates'),(207,'root_lattice_coordinates'),(208,'root_lattice_coordinates'),(209,'root_lattice_coordinates'),(210,'root_lattice_coordinates'),(211,'root_lattice_coordinates'),(212,'root_lattice_coordinates')]:
 T=T.row_join(s.Matrix(rep(n)[key]))
A=T.T*H.T
N12=s.Matrix(json.loads((p/'RQT-212-kernel-basis.json').read_text()))
N13=s.Matrix(json.loads((p/'RQT-213-kernel-basis.json').read_text()))
Z=s.Matrix(json.loads((p/'RQT-213-reduced-basis.json').read_text()))
assert X.T*G*X==G and X*h==h and K*Y==X*K
assert abs(B.det())==64 and H.det()==1 and H+H.T==-Q
assert A.rank()==12 and N12.rank()==10 and A[:11,:]*N12==s.zeros(11,10)
assert N13.rank()==9 and A*N13==s.zeros(12,9)
assert Z.T*Q*Z==s.Matrix(json.loads((p/'RQT-213-reduced-gram.json').read_text()))
assert (Z.T*Q*Z).det()==55925958066991376120
coeff=s.Matrix([39,-36,-2,-46,52,-23,-76,-48,-36])
v=Z*coeff
assert list(map(int,v))==[84,-238,-1156,94,130,170,306,358,1229,299,5,-44,269,534,176,2,-472,-250,532,-426,534]
assert A*v==s.zeros(12,1) and (v.T*Q*v)[0]==-2
U=T.row_join(v);J=U.T*H*U
assert U.rank()==13 and U.T*Q*U==-J-J.T
assert all(J[i,i]==1 for i in range(13)) and all(J[i,j]==0 for i in range(13) for j in range(i))
assert list(map(int,J[:,12]))==[0,-91,46,-532,8400,-16264,-1228,-277,-825,261,-439,183,1]
rr=K*B*v
assert list(map(int,rr))==[-494,-972,-823,-1156,94,130,170,306,358,1229,527,72,-44,269,534,176,-186,-472,-250,532,-318,534]
assert (rr.T*G*rr)[0]==-2 and (h.T*G*rr)[0]==0
R=I+rr*(rr.T*G)
assert R*R==I and R.T*G*R==G and R*h==h
print('RQT-213 PASS: 13 exact integral Wall roots; 21-root factorization OPEN')
