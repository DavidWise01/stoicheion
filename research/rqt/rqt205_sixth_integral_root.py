#!/usr/bin/env python3
"""Exact original-source RQT-205 sixth integral root certificate (SymPy)."""
from pathlib import Path
import ast,json
import sympy as S
p=Path(__file__).resolve().parent
load=lambda n:S.Matrix(ast.literal_eval((p/'source'/n).read_text().strip()[7:-1]))
X=load('X-22x22.txt');G=load('gram-22x22.txt');I=S.eye(22);h=S.Matrix([1]*4+[0]*18)
K=S.Matrix.hstack(*[I[:,j]-I[:,0] if j<20 else I[:,j] for j in range(1,22)])
B=S.Matrix(json.loads((p/'RQT-198-report.json').read_text())['basis_21x21'])
T=S.Matrix.hstack(*[S.Matrix(v) for v in json.loads((p/'RQT-201-report.json').read_text())['root_coefficients_in_index64_basis']])
T=T.row_join(S.Matrix(json.loads((p/'RQT-203-report.json').read_text())['fourth_root_coefficients']))
T=T.row_join(S.Matrix(json.loads((p/'RQT-204-report.json').read_text())['fifth_root_lattice_coordinates']))
GK=K.T*G*K;Y=(X*K)[1:22,:];Q=B.T*GK*B;H=B.T*GK*(Y-S.eye(21)).inv()*B
A=T.T*H.T
assert X**4==I and X.T*G*X==G and X*h==h and K*Y==X*K
assert abs(B.det())==64 and H.det()==1 and H+H.T==-Q
piv=[0,1,5,9,20]
assert A.rank()==5 and A[:,piv].det()==-1
free=[j for j in range(21) if j not in piv]
N=S.Matrix.hstack(*[I[:21,j]-I[:21,piv]*(A[:,piv].inv()*A[:,j]) for j in free])
assert N.shape==(21,16) and A*N==S.zeros(5,16)
v=S.Matrix([-60,-207,-819,-7,83,-28,220,288,811,50,-60,-24,369,425,202,-14,-202,-245,380,-286,207])
assert A*v==S.zeros(5,1) and (v.T*Q*v)[0]==-2
U=T.row_join(v)
J=U.T*H*U
expected=S.Matrix([[1,0,0,0,-7,115],[0,1,0,3,-36,-11],[0,0,1,-1,21,-17],[0,0,0,1,62,-457],[0,0,0,0,1,5116],[0,0,0,0,0,1]])
assert U.rank()==6 and J==expected and U.T*Q*U==-J-J.T
r=K*B*v
assert [int(x) for x in r]==[-417,-770,-719,-819,-7,83,-28,220,288,811,445,103,-24,369,425,202,-95,-202,-245,380,-365,207]
assert (r.T*G*r)[0]==-2 and (h.T*G*r)[0]==0
R=I+r*(r.T*G)
assert all(x.q==1 for x in r) and R**2==I and R.T*G*R==G and R*h==h
print('RQT-205 PASS: exact six-root Wall flag; 21-root completion OPEN')
