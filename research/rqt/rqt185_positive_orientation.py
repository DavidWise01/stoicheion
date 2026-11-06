#!/usr/bin/env python3
"""RQT-185 exact positive-plane orientation on original matrices."""
import ast,json
from pathlib import Path
import sympy as s
p=Path(__file__).resolve().parent
load=lambda n:s.Matrix(ast.literal_eval((p/'source'/n).read_text().strip()[7:-1]))
X=load('X-22x22.txt');G=load('gram-22x22.txt')
I=s.eye(22);h=s.Matrix([1]*4+[0]*18);a=h.T*G;t=I[:,0]-h/4
v=s.Matrix([5,-1,-3,-1,-7,-5,-10,-1,-1,4,3,2,3,7,7,11,-7,-2,-8,4,-17,-9])
w=s.Matrix([5,14,14,18,4,2,3,-4,-4,-22,-9,-4,-4,-7,-13,-10,8,10,7,-8,14,-5])
U=s.Matrix.hstack(v,w)
assert X**4==I and X.T*G*X==G and a*U==s.zeros(1,2)
assert U.T*G*U==s.Matrix([[2,1],[1,2]])
def chi(F):
 z=(U.T*G*F*U).det()
 assert z!=0
 return int(s.sign(z))
def inK(z):return a*z==s.zeros(1,z.cols) and all(x.q==1 for x in z)
def disc(F):
 if inK(F*t-t):return 1
 if inK(F*t+t):return -1
 raise AssertionError('invalid discriminant action')
r=I[:,20];q=I[:,21]
assert (r.T*G*r)[0]==(q.T*G*q)[0]==-2
Rn=I+r*(r.T*G);Rq=I+q*(q.T*G)
Rp=I-v*(v.T*G)
J=h*a/2-I # minus identity on K, fixes h; not integral on full M
cases={'I':I,'X':X,'X2':X**2,'X3':X**3,'negative_root_20':Rn,'negative_root_21':Rq,'positive_root':Rp,'minus_I':-I,'minus_K':J,'positive_times_minus_K':Rp*J}
rows={}
for name,F in cases.items():
 assert F.T*G*F==G
 rows[name]={'chi':chi(F),'rho':disc(F),'integral':all(z.q==1 for z in F)}
assert chi(X)==chi(Rn)==chi(Rq)==chi(J)==1
assert chi(Rp)==-1 and disc(Rp)==1 and disc(J)==-1
assert Rp**2==J**2==I and Rp*J==J*Rp
assert all(chi(F*H)==chi(F)*chi(H) for F in cases.values() for H in cases.values())
out={'boundary':'RQT-185','result':'PASS','plane_gram':[[2,1],[1,2]],'characters_surjective':True,'negative_roots_generate_full_stabilizer':False,'full_kernel_generation':'OPEN','witnesses':rows}
(p/'RQT-185-report.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
