#!/usr/bin/env python3
"""RQT-230: exact 2-primary discriminant classes and Hensel lift."""
import itertools,json
from pathlib import Path
import sympy as s
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ
p=Path(__file__).resolve().parent
F=s.Matrix(json.loads((p/'RQT-228-gram-4x4.json').read_text()))
S=smith_normal_form(F,domain=ZZ)
assert [abs(int(S[i,i])) for i in range(4)]==[1,1,2,3577256884236693207232149214617967173770038110]
rad=[s.Matrix(t) for t in itertools.product(range(2),repeat=4) if all(int(z)%2==0 for z in F*s.Matrix(t))]
assert [list(r) for r in rad]==[[0,0,0,0],[0,1,1,1],[1,0,0,1],[1,1,1,0]]
assert [((r.T*F*r)[0]/4)%2 for r in rad]==[0,0,s.Rational(3,2),s.Rational(1,2)]
for m,expected in [(4,(96,32)),(8,(768,256)),(16,(6144,2048))]:
 c1=c2=0
 for z in itertools.product(range(m),repeat=4):
  x=s.Matrix(z);q=int((x.T*F*x)[0])
  if (q+2)%m:continue
  if all(int(u)%2==0 for u in F*x):
   assert tuple(u%2 for u in z)==(1,0,0,1)
   c2+=1
  else:c1+=1
 assert (c1,c2)==expected
a=s.Matrix([1,0,0,1]);e=s.eye(4)[:,3]
c=int(((a.T*F*a)[0]+2)/8);b=int((a.T*F*e)[0]/2);d=int(F[3,3]/2)
assert (c,b,d)==(-1131077395607,664043305563,-3048260410782)
t=0
for n in range(1,65):
 if (c+b*t+d*t*t)%(1<<n):t+=1<<(n-1)
 assert (c+b*t+d*t*t)%(1<<n)==0
assert t==18233304022598118383
assert (((a+2*t*e).T*F*(a+2*t*e))[0]+2)%(1<<67)==0
print('RQT-230 PASS; global integral root 18 remains OPEN')
