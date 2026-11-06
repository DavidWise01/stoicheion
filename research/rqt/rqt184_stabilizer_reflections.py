#!/usr/bin/env python3
"""RQT-184 exact stabilizer and root reflection audit (SymPy)."""
from pathlib import Path
import ast,json
import sympy as s
p=Path(__file__).resolve().parent
read=lambda f:s.Matrix(ast.literal_eval((p/'source'/f).read_text().strip()[7:-1]))
X=read('X-22x22.txt'); G=read('gram-22x22.txt')
I=s.eye(22); h=s.Matrix([1]*4+[0]*18); a=h.T*G
t=I[:,0]-h/4
assert X**4==I and X.T*G*X==G and a*h==s.Matrix([[4]])
def inK(v):
 return a*v==s.zeros(1,v.cols) and all(z.q==1 for z in v)
def discr_sign(F):
 if inK(F*t-t):return 1
 if inK(F*t+t):return -1
 raise ValueError('no discriminant sign')
v=I[:,20];w=I[:,21]
assert inK(v) and inK(w)
assert (v.T*G*v)[0]==-2 and (w.T*G*w)[0]==-2
assert (v.T*G*w)[0]==1
Rv=I+v*(v.T*G);Rw=I+w*(w.T*G)
assert Rv**2==Rw**2==I and (Rv*Rw)**3==I
J=h*a/2-I
cases=[
 ('identity',I,1,1,True),
 ('cyclic_X',X,1,1,True),
 ('root_e20',Rv,1,1,True),
 ('root_e21',Rw,1,1,True),
 ('root_product',Rv*Rw,1,1,True),
 ('negative_identity',-I,-1,-1,True),
 ('rational_mismatched_glue',J,1,-1,False),
]
results={}
for name,F,hs,ds,integral in cases:
 assert F.T*G*F==G and F*h==hs*h
 assert discr_sign(F)==ds
 assert all(z.q==1 for z in F)==integral
 assert (hs==ds)==integral
 results[name]={'h_sign':hs,'discriminant_sign':ds,'integral':integral}
assert J*X==X*J and J*Rv==Rv*J and J*Rw==Rw*J
out={'RQT':184,'status':'PASS','discriminant_image':['+1','-1'],
 'splitting':'O(K) = O(M)_h x C2 (central -I_K)',
 'root_pairing':[-2,-2,1],'root_product_order':3,
 'full_reflection_generation':'NOT PROVEN','tests':results}
(p/'RQT-184-report.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
