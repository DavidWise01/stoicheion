#!/usr/bin/env python3
"""RQT-203 original-source exact fourth root certificate. Requires SymPy."""
import ast,json
from pathlib import Path
import sympy as s
p=Path(__file__).resolve().parent
load=lambda n:s.Matrix(ast.literal_eval((p/'source'/n).read_text().strip()[7:-1]))
G=load('gram-22x22.txt');X=load('X-22x22.txt');I=s.eye(22);h=s.Matrix([1]*4+[0]*18)
K=s.Matrix.hstack(*[I[:,j]-I[:,0] if j<20 else I[:,j] for j in range(1,22)])
B=s.Matrix(json.loads((p/'RQT-198-report.json').read_text())['basis_21x21'])
prior=json.loads((p/'RQT-201-report.json').read_text())['root_coefficients_in_index64_basis']
T=s.Matrix.hstack(*[s.Matrix(v) for v in prior])
GK=K.T*G*K;Y=(X*K)[1:22,:];Q=B.T*GK*B
H=B.T*GK*(Y-s.eye(21)).inv()*B
A=T.T*H.T
assert X.T*G*X==G and X*h==h and A.rank()==3
assert T.T*Q*T==-2*s.eye(3) and T.T*H*T==s.eye(3)
piv=[3,9,20];free=[j for j in range(21) if j not in piv]
AP=A[:,piv];assert AP.det()==1
N=s.Matrix.hstack(*[s.eye(21)[:,j]-s.eye(21)[:,piv]*(AP.inv()*A[:,j]) for j in free])
assert N.shape==(21,18) and A*N==s.zeros(3,18)
RED,Ntrans=N.T.lll_transform();assert abs(Ntrans.det())==1
c=s.Matrix([3,-2,-4,1,4,-1,1,3,3,5,0,2,6,0,-2,-4,1,-3])
v=RED.T*c
expected=[3,1,3,-4,-4,-8,1,-1,1,-4,0,2,3,3,6,0,-2,-4,1,-3,-5]
assert [int(z) for z in v]==expected and A*v==s.zeros(3,1)
assert (v.T*Q*v)[0]==-2
T4=T.row_join(v)
assert T4.rank()==4
assert T4.T*H*T4==s.Matrix([[1,0,0,0],[0,1,0,3],[0,0,1,-1],[0,0,0,1]])
assert T4.T*Q*T4==s.Matrix([[-2,0,0,0],[0,-2,0,-3],[0,0,-2,1],[0,-3,1,-2]])
r=K*B*v;assert [int(z) for z in r]==[4,2,0,3,-4,-4,-8,1,-1,1,1,1,2,3,3,6,-5,-2,-4,1,-11,-5]
R=I+r*(r.T*G)
assert (h.T*G*r)[0]==0 and (r.T*G*r)[0]==-2
assert R*R==I and R.T*G*R==G and R*h==h
print('RQT-203 PASS: fourth exact integral Wall root; 21-root word remains OPEN')
