#!/usr/bin/env python3
"""RQT-210: exact tenth-root verification against original RQT matrices."""
import ast,json
from pathlib import Path
import sympy as S
p=Path(__file__).resolve().parent
load=lambda n:S.Matrix(ast.literal_eval((p/'source'/n).read_text().strip()[7:-1]))
rep=lambda n:json.loads((p/f'RQT-{n}-report.json').read_text())
X=load('X-22x22.txt');G=load('gram-22x22.txt');I=S.eye(22)
h=S.Matrix([1]*4+[0]*18)
K=S.Matrix.hstack(*[I[:,j]-I[:,0] if j<20 else I[:,j] for j in range(1,22)])
B=S.Matrix(rep(198)['basis_21x21'])
GK=K.T*G*K;Y=(X*K)[1:22,:]
Q=B.T*GK*B;H=B.T*GK*(Y-S.eye(21)).inv()*B
T=S.Matrix.hstack(*[S.Matrix(z) for z in rep(201)['root_coefficients_in_index64_basis']])
for n,key in [(203,'fourth_root_coefficients'),(204,'fifth_root_lattice_coordinates'),(205,'root_lattice_coordinates'),(207,'root_lattice_coordinates'),(208,'root_lattice_coordinates'),(209,'root_lattice_coordinates')]:
 T=T.row_join(S.Matrix(rep(n)[key]))
A=T.T*H.T
v=S.Matrix([-5,18,87,-7,-10,-11,-22,-29,-95,-22,-1,3,-23,-41,-15,-2,38,21,-42,33,-41])
assert X**4==I and X.T*G*X==G and X*h==h
assert abs(B.det())==64 and H.det()==1 and H+H.T==-Q
assert A.rank()==9 and A*v==S.zeros(9,1) and (v.T*Q*v)[0]==-2
T10=T.row_join(v);W10=T10.T*H*T10
assert T10.rank()==10 and all(W10[i,i]==1 for i in range(10))
assert all(W10[i,j]==0 for i in range(10) for j in range(i))
assert list(map(int,W10[:,9]))==[-3,6,-1,46,-713,1154,98,24,46,1]
assert T10.T*Q*T10==-W10-W10.T
r=K*B*v
assert list(map(int,r))==[39,76,64,87,-7,-10,-11,-22,-29,-95,-41,-5,3,-23,-41,-15,13,38,21,-42,25,-41]
R=I+r*(r.T*G)
assert all(z.q==1 for z in r) and (h.T*G*r)[0]==0
assert R**2==I and R.T*G*R==G and R*h==h
print('RQT-210 PASS: tenth integral norm -2 Wall-compatible root')
