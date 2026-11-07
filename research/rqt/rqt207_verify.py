#!/usr/bin/env python3
"""RQT-207 exact seventh-root certificate against original RQT sources."""
import ast,json
from pathlib import Path
import sympy as s
p=Path(__file__).resolve().parent
load=lambda n:s.Matrix(ast.literal_eval((p/'source'/n).read_text().strip()[7:-1]))
G=load('gram-22x22.txt');X=load('X-22x22.txt');I=s.eye(22)
h=s.Matrix([1]*4+[0]*18)
K=s.Matrix.hstack(*[I[:,j]-I[:,0] if j<20 else I[:,j] for j in range(1,22)])
B=s.Matrix(json.loads((p/'RQT-198-report.json').read_text())['basis_21x21'])
GK=K.T*G*K;Y=(X*K)[1:22,:];Q=B.T*GK*B;H=B.T*GK*(Y-s.eye(21)).inv()*B
T=s.Matrix.hstack(*[s.Matrix(v) for v in json.loads((p/'RQT-201-report.json').read_text())['root_coefficients_in_index64_basis']])
for f,k in [('RQT-203-report.json','fourth_root_coefficients'),('RQT-204-report.json','fifth_root_lattice_coordinates'),('RQT-205-report.json','root_lattice_coordinates')]:
 T=T.row_join(s.Matrix(json.loads((p/f).read_text())[k]))
A=T.T*H.T;N=s.Matrix(json.loads((p/'RQT-206-report.json').read_text())['kernel_basis_21x15'])
assert X**4==I and X.T*G*X==G and X*h==h and K*Y==X*K
assert abs(B.det())==64 and H.det()==1 and H+H.T==-Q
assert A.rank()==6 and N.rank()==15 and A*N==s.zeros(6,15)
reduced,change=N.T.lll_transform()
assert abs(change.det())==1
coeff=s.Matrix([-59,14,-6,-6,33,21,-47,30,-39,45,42,-47,29,24,7])
v=reduced.T*coeff
expect=[4,-20,-102,3,8,0,28,32,112,19,-2,-3,36,53,21,1,-37,-34,51,-40,36]
assert list(map(int,v))==expect and A*v==s.zeros(6,1) and (v.T*Q*v)[0]==-2
T7=T.row_join(v);J=T7.T*H*T7
assert T7.rank()==7 and all(J[i,j]==0 for i in range(7) for j in range(i)) and all(J[i,i]==1 for i in range(7))
assert T7.T*Q*T7==-J-J.T
r=K*B*v
assert list(map(int,r))==[-43,-91,-83,-102,3,8,0,28,32,112,55,12,-3,36,53,21,-18,-37,-34,51,-44,36]
assert (r.T*G*r)[0]==-2 and (h.T*G*r)[0]==0
R=I+r*(r.T*G)
assert R**2==I and R.T*G*R==G and R*h==h
print('RQT-207 PASS: seventh integral root, exact 7x7 Wall triangularity')
