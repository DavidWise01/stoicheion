#!/usr/bin/env python3
"""RQT-226 exact cone certificate and bound generator; requires SymPy."""
import ast,json,math
from pathlib import Path
import sympy as s
p=Path(__file__).resolve().parent
def load(n):
 t=(p/'source'/n).read_text().strip()
 return s.Matrix(ast.literal_eval(t[7:-1]))
G=load('gram-22x22.txt');X=load('X-22x22.txt');I=s.eye(22);h=s.Matrix([1]*4+[0]*18)
K=s.Matrix.hstack(*[I[:,j]-I[:,0] if j<20 else I[:,j] for j in range(1,22)])
B=s.Matrix(json.loads((p/'RQT-198-report.json').read_text())['basis_21x21'])
Z6=s.Matrix(json.loads((p/'RQT-216-reduced-basis.json').read_text()))
Z5=s.Matrix(json.loads((p/'RQT-225-reduced-basis.json').read_text()))
F=s.Matrix(json.loads((p/'RQT-225-reduced-gram.json').read_text()))
assert X.T*G*X==G and X*h==h
assert F==Z5.T*Z6.T*B.T*K.T*G*K*B*Z6*Z5
assert F.det()==614658467036485410516469524254677624
P=-F[1:5,1:5];b=F[1:5,0];V=P.inv();v=V*b
beta=F[0,0]+(b.T*v)[0]
assert all(P[:i,:i].det()>0 for i in range(1,5))
assert beta>0 and all(v[i]**2>(beta+2)*V[i,i] for i in range(4))
assert [s.sign(x) for x in v]==[-1,1,1,1]
count=0;rows=[]
for t in range(1,6001):
 row=[t];c=1
 for i in range(3):
  center=v[i]*t;rad2=(beta*t*t+2)*V[i,i]
  ceil_sqrt=math.isqrt((int(s.numer(rad2))+int(s.denom(rad2))-1)//int(s.denom(rad2)))+1
  lo=int(s.floor(center))-ceil_sqrt-1;hi=int(s.ceiling(center))+ceil_sqrt+1
  assert lo<center-s.sqrt(rad2) and hi>center+s.sqrt(rad2)
  row.extend([lo,hi]);c*=hi-lo+1
 rows.append(' '.join(map(str,row)));count+=c
assert count==588300144
assert (p/'bounds.txt').read_text()=='\n'.join(rows)+'\n'
assert (p/'roots.txt').read_text().strip()==''
assert (p/'search.log').read_text().strip()=='TOTAL 588300144 FOUND 0'
print('RQT-226 PASS: exact orthant theorem; finite exclusion |x[0]|<=6000')
