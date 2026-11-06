#!/usr/bin/env python3
"""RQT-180: exact integral conjugator for original RQT-133 matrix."""
import ast, hashlib, json
from pathlib import Path
import sympy as s
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

root=Path(__file__).resolve().parent
raw=(root/'source'/'X-22x22.txt').read_text().strip()
X=s.Matrix(ast.literal_eval(raw[7:-1]))
I=s.eye(22); e=I[:,0]
assert X.shape==(22,22) and X**4==I
B=s.Matrix.hstack(*[X**j*e for j in range(4)])
rows=[0,1,4,7]
Z=B[rows,:].inv()
F=s.zeros(4,22)
for j,i in enumerate(rows): F[:,i]=Z[:,j]
assert F*B==s.eye(4)
C4=s.zeros(4)
for j in range(4): C4[(j+1)%4,j]=1
Pco=s.Matrix.vstack(*[F[0,:]*X**(-j) for j in range(4)])
assert Pco*B==s.eye(4) and Pco*X==C4*Pco
piv=[0,1,3,5]; other=[j for j in range(22) if j not in piv]
assert abs(Pco[:,piv].det())==1
W=s.Matrix.hstack(*[I[:,j]-I[:,piv]*Pco[:,piv].inv()*Pco[:,j] for j in other])
F0=B.row_join(W)
assert F0.det(method='domain-ge')==1
Xw=(F0.inv()*X*F0)[4:,4:]
E=s.eye(18)
assert E+Xw+Xw**2+Xw**3==s.zeros(18)
H=s.Matrix([[-1,0,0],[0,0,-1],[1,1,0]])
seeds=[5,10,17,2,8,13]
blocks=[]
for idx in seeds:
    v=E[:,idx]; t=(Xw+E)*v; r=-Xw*t
    Q=s.Matrix.hstack(v,r,t)
    assert Xw*Q==Q*H
    blocks.append(Q)
V=s.Matrix.hstack(*blocks)
assert V.det(method='domain-ge')==1
P=B.row_join(W*V)
Y=s.diag(C4,*([H]*6))
assert P.det(method='domain-ge')==1
assert X*P==P*Y and P.inv()*X*P==Y
N=I+X+X**2+X**3; NY=I+Y+Y**2+Y**3
assert N*P==P*NY
assert N.rank()==1 and N*e==s.Matrix([1]*4+[0]*18)
SN=smith_normal_form(X-I,domain=ZZ)
assert [abs(int(SN[i,i])) for i in range(22)]==[1]*15+[4]*6+[0]
(root/'P-22x22.txt').write_text(str(P))
report={'RQT':180,'status':'PASS','det_P':1,'normal_form':'C4 + H^6','seeds':seeds,'source_sha256':hashlib.sha256(raw.encode()).hexdigest(),'P_sha256':hashlib.sha256(str(P).encode()).hexdigest()}
(root/'RQT-180-report.json').write_text(json.dumps(report,indent=2))
print(json.dumps(report,indent=2))
