#!/usr/bin/env python3
"""RQT-183: discriminant extension tests against actual RQT-122/133 files."""
from pathlib import Path
import ast,json
import sympy as s
root=Path(__file__).resolve().parent
load=lambda p:s.Matrix(ast.literal_eval(p.read_text().strip()[7:-1]))
X=load(root/'source'/'X-22x22.txt')
G=load(root/'source'/'gram-22x22.txt')
I=s.eye(22);h=s.Matrix([1]*4+[0]*18);a=h.T*G
assert X**4==I and X.T*G*X==G and G.det()==-1 and (a*h)[0]==4
t=I[:,0]-h/4
K=s.Matrix.hstack(*[I[:,j]-a[j]*I[:,0] for j in range(1,22)])
assert abs(s.Matrix.hstack(h,K).det())==4
def in_K(v):return a*v==s.zeros(1,v.cols) and all(x.q==1 for x in v)
assert in_K(4*t) and not in_K(2*t)
def check(F,hsign,disc_sign,integral):
 assert F*h==hsign*h and F.T*G*F==G
 assert in_K(F*t-disc_sign*t)
 assert all(x.q==1 for x in F)==integral
 assert in_K(F*t-hsign*t)==integral
v=K[:,19];assert (v.T*G*v)[0]==-2
reflection=I+v*(v.T*G)
bad=h*a/2-I
for F,h_sign,d_sign,yes in [(I,1,1,True),(X,1,1,True),(reflection,1,1,True),(bad,1,-1,False),(-I,-1,-1,True)]:
 check(F,h_sign,d_sign,yes)
print("RQT-183 PASS: five exact extension/obstruction cases")
