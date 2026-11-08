#!/usr/bin/env python3
"""RQT-222 exact full-support theorem against original RQT matrices."""
import ast,json
from pathlib import Path
import sympy as S
P=Path(__file__).resolve().parent
F=S.Matrix(json.loads((P/'RQT-216-reduced-gram.json').read_text()))
Z=S.Matrix(json.loads((P/'RQT-216-reduced-basis.json').read_text()))
B=S.Matrix(json.loads((P/'RQT-198-report.json').read_text())['basis_21x21'])
def read(n):
 t=(P/'source'/n).read_text().strip()
 return S.Matrix(ast.literal_eval(t[7:-1]))
G=read('gram-22x22.txt');X=read('X-22x22.txt');I=S.eye(22);h=S.Matrix([1]*4+[0]*18)
K=S.Matrix.hstack(*[I[:,j]-I[:,0] if j<20 else I[:,j] for j in range(1,22)])
assert X.T*G*X==G and X*h==h
assert F==Z.T*B.T*K.T*G*K*B*Z and F.det()==-313982794406122741723132503868
assert all(F[i,i]%2==0 for i in range(6))
for omitted in range(6):
 ids=[j for j in range(6) if j!=omitted]
 M=-F.extract(ids,ids)-10928*S.eye(5)
 assert all(M[:j,:j].det()>0 for j in range(1,6))
assert (F-13*S.eye(6)).det()==-15740534870424877855390570819
assert (F-14*S.eye(6)).det()==7207415819344600406943933164
print('RQT-222 PASS: full coordinate support required; signature (1,5); positive eigenvalue in (13,14). Integral root OPEN.')
