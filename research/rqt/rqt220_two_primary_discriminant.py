#!/usr/bin/env python3
"""RQT-220 exact two-primary discriminant form and modulo-eight audit."""
import itertools,ast,json
from pathlib import Path
import sympy as s
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ
p=Path(__file__).resolve().parent
F=s.Matrix(json.loads((p/'RQT-216-reduced-gram.json').read_text()))
Z=s.Matrix(json.loads((p/'RQT-216-reduced-basis.json').read_text()))
B=s.Matrix(json.loads((p/'RQT-198-report.json').read_text())['basis_21x21'])
def read(n):
 t=(p/'source'/n).read_text().strip();return s.Matrix(ast.literal_eval(t[7:-1]))
G=read('gram-22x22.txt');X=read('X-22x22.txt');I=s.eye(22);h=s.Matrix([1]*4+[0]*18)
K=s.Matrix.hstack(*[I[:,j]-I[:,0] if j<20 else I[:,j] for j in range(1,22)])
assert F==Z.T*B.T*K.T*G*K*B*Z and X.T*G*X==G and X*h==h
assert F.det()==-313982794406122741723132503868
S=smith_normal_form(F,domain=ZZ)
assert [abs(int(S[i,i])) for i in range(6)]==[1,1,1,1,2,156991397203061370861566251934]
rad=[s.Matrix(x) for x in itertools.product(range(2),repeat=6) if all(int(z)%2==0 for z in F*s.Matrix(x))]
assert len(rad)==4
q=[((x.T*F*x)[0]/4)%2 for x in rad]
b=[[((x.T*F*y)[0]/4)%1 for y in rad] for x in rad]
assert q==[0,s.Rational(3,2),s.Rational(3,2),1]
assert b==[[0,0,0,0],[0,s.Rational(1,2),0,s.Rational(1,2)],[0,0,s.Rational(1,2),s.Rational(1,2)],[0,s.Rational(1,2),s.Rational(1,2),0]]
counts={tuple(map(int,rad[i])):0 for i in (1,2)}
coeff=[[int(F[i,j]) for j in range(6)] for i in range(6)]
for x in itertools.product(range(8),repeat=6):
 y=[sum(coeff[i][j]*x[j] for j in range(6)) for i in range(6)]
 if (sum(x[i]*y[i] for i in range(6))+2)%8==0 and all(t%2==0 for t in y):
  k=tuple(t%2 for t in x);assert k in counts;counts[k]+=1
assert sorted(counts.values())==[4096,4096]
print('RQT-220 PASS; both d=2 root classes locally viable; integral root OPEN')
