#!/usr/bin/env python3
"""RQT-186 exact rational spinor parity checks on original RQT sources."""
import ast,json
from pathlib import Path
import sympy as s
p=Path(__file__).resolve().parent
src=p/'source'
read=lambda n:s.Matrix(ast.literal_eval((src/n).read_text().strip()[7:-1]))
X=read('X-22x22.txt');G=read('gram-22x22.txt');I=s.eye(22)
h=s.Matrix([1]*4+[0]*18); a=h.T*G;t=I[:,0]-h/4
assert X**4==I and X.T*G*X==G and X*h==h
def squareclass(q):
 q=s.Rational(q);assert q
 out=int(s.sign(q))
 for a in (abs(q.p),q.q):
  for prime,exp in s.factorint(a).items():
   if exp%2:out*=int(prime)
 return out
def negspace(F):
 vs=(F+I).nullspace()
 V=s.Matrix.hstack(*vs)
 return (V.cols,s.factor((V.T*G*V).det()))
d,m=negspace(X)
assert (d,m)==(7,-64)
theta_X=squareclass(m*s.Rational(1,2)**7)
d2,m2=negspace(X**2)
assert (d2,m2)==(14,16)
theta_X2=squareclass(m2)
assert theta_X==-2 and theta_X2==1 and X.det()==-1 and (X**2).det()==1
v=I[:,20];w=I[:,21]
assert (v.T*G*v)[0]==-2 and (w.T*G*w)[0]==-2
Rv=I+v*(v.T*G);Rw=I+w*(w.T*G)
assert Rv.T*G*Rv==G and Rw.T*G*Rw==G and (Rv*Rw)**3==I
u=s.Matrix([5,-1,-3,-1,-7,-5,-10,-1,-1,4,3,2,3,7,7,11,-7,-2,-8,4,-17,-9])
z=s.Matrix([5,14,14,18,4,2,3,-4,-4,-22,-9,-4,-4,-7,-13,-10,8,10,7,-8,14,-5])
U=s.Matrix.hstack(u,z)
assert a*U==s.zeros(1,2) and (U.T*G*U)==s.Matrix([[2,1],[1,2]])
assert (U.T*G*X*U).det()>0
assert a*(X*t-t)==s.zeros(1,1) and all(q.q==1 for q in X*t-t)
result={'RQT':'186','status':'PASS','X_spinor_squareclass':theta_X,
'X2_spinor_squareclass':theta_X2,'negative_X_eigenspace_Gram_det':str(m),
'negative_X2_eigenspace_Gram_det':str(m2),'root_factorization':'OPEN'}
(p/'RQT-186-report.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
