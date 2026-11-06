#!/usr/bin/env python3
"""Exact audit of the original RQT-133 matrix; run from this directory."""
from pathlib import Path
import ast, hashlib, json
import sympy as s
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

def rank2(A):
    piv={}
    for i in range(A.rows):
        x=sum((int(A[i,j])&1)<<j for j in range(A.cols))
        while x:
            j=x.bit_length()-1
            if j in piv: x^=piv[j]
            else: piv[j]=x; break
    return len(piv)

p=Path(__file__).resolve().parent
raw=(p/'source'/'X-22x22.txt').read_text().strip()
X=s.Matrix(ast.literal_eval(raw[7:-1]))
I=s.eye(22); D=X-I; N=I+X+X**2+X**3
e=I[:,0]; h=s.Matrix([1]*4+[0]*18)
assert X.shape==(22,22) and X**4==I and X.det()==-1
assert N.rank()==1 and N*e==h and X*h==h and D.rank()==21
b=(22-int(s.trace(X**2)))//4
ranks=[rank2(D**j) for j in range(5)]
g=ranks[1]-b-2
SN=smith_normal_form(D,domain=ZZ)
counts={str(v):sum(abs(int(SN[j,j]))==v for j in range(22)) for v in (0,1,2,4)}
B=s.Matrix.hstack(*[X**j*e for j in range(4)])
BS=smith_normal_form(B,domain=ZZ)
orbit=[abs(int(BS[j,j])) for j in range(4)]
assert (b,g)==(7,6) and ranks==[22,15,8,1,0]
assert counts=={'0':1,'1':15,'2':0,'4':6} and orbit==[1]*4
report={'source_sha256':hashlib.sha256(raw.encode()).hexdigest(),'b':b,'g':g,'mod2_ranks':ranks,'smith_counts':counts,'orbit_smith':orbit,'canonical_type':'C4 + 6 H blocks','conjugator_verified':False}
print(json.dumps(report,indent=2))
