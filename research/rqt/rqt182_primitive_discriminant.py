#!/usr/bin/env python3
"""Exact RQT-182 primitive orthogonal/discriminant audit."""
from pathlib import Path
import ast, json, hashlib
import sympy as s
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ
root=Path(__file__).resolve().parent
parse=lambda p:s.Matrix(ast.literal_eval(p.read_text().strip()[7:-1]))
X=parse(root/'source'/'X-22x22.txt')
G=parse(root/'source'/'gram-22x22.txt')
I=s.eye(22); h=s.Matrix([1]*4+[0]*18); a=h.T*G
assert X**4==I and X.T*G*X==G and G.det()==-1
assert a[0]==1 and a*h==s.Matrix([[4]]) and X*h==h
K=s.Matrix.hstack(*[I[:,j]-a[j]*I[:,0] for j in range(1,22)])
A=s.Matrix.hstack(h,K); GK=K.T*G*K
assert a*K==s.zeros(1,21) and abs(A.det())==4
assert GK.det()==-4
SN=smith_normal_form(GK,domain=ZZ)
assert [abs(int(SN[j,j])) for j in range(21)]==[1]*20+[4]
t=I[:,0]-h/4
assert (h.T*G*t)[0]==0 and all(q.q==1 for q in K.T*G*t)
assert (t.T*G*t)[0]==s.Rational(-9,4)
Z=A.inv()
def inK(v):
    z=Z*v
    return z[0]==0 and all(q.q==1 for q in z[1:,0])
assert inK(4*t) and not inK(2*t) and inK(X*t-t)
report={'RQT':182,'status':'PASS','h2':4,'K_rank':21,
'K_det':-4,'K_signature':[2,19],'discriminant':'Z/4',
'quadratic_generator':'-1/4 (mod 2Z)','glue_index':4,
'X_on_discriminant':'identity',
'X_sha256':hashlib.sha256((root/'source'/'X-22x22.txt').read_bytes()).hexdigest(),
'G_sha256':hashlib.sha256((root/'source'/'gram-22x22.txt').read_bytes()).hexdigest()}
(root/'RQT-182-report.json').write_text(json.dumps(report,indent=2)+'\n')
(root/'RQT-182-K-gram.txt').write_text(str(GK))
print(json.dumps(report,indent=2))
