#!/usr/bin/env python3
"""RQT-189 exact non-monotone reflection bridge on original X,G."""
import ast
import sympy as s
from pathlib import Path
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ
p=Path(__file__).resolve().parent
read=lambda n:s.Matrix(ast.literal_eval((p/'source'/n).read_text().strip()[7:-1]))
X=read('X-22x22.txt');G=read('gram-22x22.txt');I=s.eye(22)
h=s.Matrix([1]*4+[0]*18)
K=s.Matrix.hstack(*[I[:,j]-I[:,0] if j<20 else I[:,j] for j in range(1,22)])
prev=[{19:1},{20:1},{8:1,16:-1,20:1},{5:1,16:-1,19:1,20:1},{14:1,17:-1,19:-1,20:-1},{7:1,8:1,10:-1,16:-1,20:1}]
extra=[{20:1},{5:1,14:-1},{2:1,17:-1},{0:1,5:-1},{0:1,1:-1},{0:1},{15:1},{13:1},{7:1},{4:1},{8:1},{9:1},{12:1}]
reflect=lambda r:I+r*(r.T*G)
F=X; refl=[]
for j,coeff in enumerate(prev+extra):
 c=s.zeros(21,1)
 for i,v in coeff.items():c[i]=v
 r=K*c if j<6 else (F-I)*K*c
 assert (r.T*G*r)[0]==-2 and (h.T*G*r)[0]==0
 R=reflect(r)
 assert R**2==I and R.T*G*R==G
 F=R*F;refl.append(R)
assert (F-I).rank()==2
B0=s.Matrix.hstack(*((F-I).columnspace()))
assert B0.T*G*B0==s.diag(0,-6)
u=((F-I)**2).columnspace()[0]/6
assert all(z.q==1 for z in u) and (u.T*G*u)[0]==0
r=I[:,20];rr=r+u
assert (r.T*G*r)[0]==(rr.T*G*rr)[0]==-2
assert (h.T*G*rr)[0]==0
R20=reflect(r);R21=reflect(rr)
F20=R20*F;F21=R21*F20
assert [(Z-I).rank() for Z in (F,F20,F21)]==[2,3,2]
B=s.Matrix.hstack(*((F21-I).columnspace()))
assert B.T*G*B==s.diag(0,-8)
SN=smith_normal_form(B,domain=ZZ)
assert [abs(int(SN[j,j])) for j in range(2)]==[1,1]
assert ((B[:,1]/2).T*G*(B[:,1]/2))[0]==-2
assert F21.T*G*F21==G
Y=F21
for R in [R21,R20]+list(reversed(refl)):Y=R*Y
assert Y==X
print('RQT-189 PASS: 21 root reflections, rank bridge 2->3->2; full factorization OPEN')
