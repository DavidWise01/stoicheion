#!/usr/bin/env python3
"""RQT-192: exact 2-adic lifting, original RQT-122/133 sources."""
import ast,json
from pathlib import Path
import sympy as S
p=Path(__file__).resolve().parent
read=lambda n:S.Matrix(ast.literal_eval((p/'source'/n).read_text().strip()[7:-1]))
G=read('gram-22x22.txt');X=read('X-22x22.txt');I=S.eye(22)
h=S.Matrix([1]*4+[0]*18)
K=S.Matrix.hstack(*[I[:,j]-I[:,0] if j<20 else I[:,j] for j in range(1,22)])
u=S.Matrix([-4,-5,-5,-7,0,1,2,0,1,6,3,2,1,1,4,2,-1,-3,0,2,-1,4])
a=S.Matrix([-17,-22,-24,-29,0,5,5,0,6,24,13,8,1,9,18,10,-4,-10,-3,10,-8,11])
dot=lambda x,y:int((x.T*G*y)[0])
assert X**4==I and X.T*G*X==G and dot(h,h)==4
assert dot(h,u)==dot(h,a)==dot(u,u)==dot(u,a)==0 and dot(a,a)==-8
c=S.Matrix([1,1,0,1,1,1,0,1,1,1,1,0,1,0,0,1,0,0,1,1,0])
d=I[:21,0]
assert dot(K*c,K*c)==-382 and dot(K*c,K*d)%2==1
assert dot(K*d,K*d)%2==0 and dot(a,K*d)==dot(u,K*d)==0
trace=[]
for k in range(2,21):
 r=K*c
 assert dot(a,r)==-4 and dot(u,r)==0
 assert (dot(r,r)+2)%(2**k)==0
 if (dot(r,r)+2)%(2**(k+1)):
  c+=2**(k-1)*d
 r=K*c
 assert (dot(r,r)+2)%(2**(k+1))==0 and dot(r,K*d)%2==1
 trace.append({'power':k+1,'norm':dot(r,r)})
r=K*c;z=2*r-a
assert dot(z,z)%(2**23)==0
assert dot(z,a)==dot(z,u)==dot(z,h)==0
assert all((z-a)[i]%2==0 for i in range(22))
out={'RQT':192,'status':'2ADIC_SOLUBILITY_PASS','seed_norm':-382,
'precision':21,'z_precision':23,'coefficients':[int(x) for x in c],
'global_integral_solution':'OPEN','trace':trace}
(p/'RQT-192-report.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
