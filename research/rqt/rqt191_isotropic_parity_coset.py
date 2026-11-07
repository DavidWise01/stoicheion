#!/usr/bin/env python3
"""RQT-191: exact isotropic parity-coset criterion and finite search."""
import ast,itertools,json
from pathlib import Path
import sympy as s
p=Path(__file__).resolve().parent
read=lambda f:s.Matrix(ast.literal_eval((p/'source'/f).read_text().strip()[7:-1]))
G=read('gram-22x22.txt');X=read('X-22x22.txt');I=s.eye(22)
h=s.Matrix([1]*4+[0]*18)
K=s.Matrix.hstack(*[I[:,j]-I[:,0] if j<20 else I[:,j] for j in range(1,22)])
u=s.Matrix([-4,-5,-5,-7,0,1,2,0,1,6,3,2,1,1,4,2,-1,-3,0,2,-1,4])
a=s.Matrix([-17,-22,-24,-29,0,5,5,0,6,24,13,8,1,9,18,10,-4,-10,-3,10,-8,11])
dot=lambda x,y:(x.T*G*y)[0]
assert X**4==I and X.T*G*X==G
assert dot(u,u)==dot(h,u)==dot(h,a)==dot(a,u)==0 and dot(a,a)==-8
r0=-I[:,0]-I[:,1]-I[:,2]-I[:,12]+I[:,20]
s0=a-r0;z0=2*r0-a
assert dot(r0,r0)==dot(s0,s0)==-2
assert [dot(h,r0),dot(h,s0)]==[-4,4]
assert [dot(z0,z0),dot(z0,u),dot(z0,a),dot(z0,h)]==[0,0,0,-8]
B=K.T*G*K
av=[int(x) for x in (a.T*G*K)]
uv=[int(x) for x in (u.T*G*K)]
eligible=[j for j in range(21) if uv[j]==0]
assert len(eligible)==20
checked=linear_hits=success=0
for n in range(1,5):
 for ids in itertools.combinations(eligible,n):
  for signs in itertools.product((-1,1),repeat=n):
   checked+=1
   if sum(signs[j]*av[i] for j,i in enumerate(ids))!=-4: continue
   linear_hits+=1
   q=sum(signs[j]*signs[k]*int(B[i,l]) for j,i in enumerate(ids) for k,l in enumerate(ids))
   if q==-2: success+=1
assert (checked,linear_hits,success)==(87440,1084,0)
report={'RQT':191,'status':'EXACT_COSET_CRITERION_BOUNDED_EXCLUSION',
 'candidate_count':checked,'linear_hits':linear_hits,'root_pairs_found':success,
 'ambient_isotropic_h_pairing':-8,'full_stabilizer_factorization':'OPEN'}
(p/'RQT-191-report.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
