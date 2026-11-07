#!/usr/bin/env python3
"""RQT-190: reconstruct 25 ambient root reflections, verify product = original X."""
import ast, json
from pathlib import Path
import sympy as S
p=Path(__file__).resolve().parent
def load(n):
 t=(p/'source'/n).read_text().strip()
 return S.Matrix(ast.literal_eval(t[7:-1]))
X=load('X-22x22.txt');G=load('gram-22x22.txt')
I=S.eye(22);h=S.Matrix([1]*4+[0]*18)
K=S.Matrix.hstack(*[I[:,j]-I[:,0] if j<20 else I[:,j] for j in range(1,22)])
A=[{19:1},{20:1},{8:1,16:-1,20:1},{5:1,16:-1,19:1,20:1},
   {14:1,17:-1,19:-1,20:-1},{7:1,8:1,10:-1,16:-1,20:1}]
B=[{20:1},{5:1,14:-1},{2:1,17:-1},{0:1,5:-1},{0:1,1:-1},
   {0:1},{15:1},{13:1},{7:1},{4:1},{8:1},{9:1},{12:1}]
R=lambda r:I+r*(r.T*G)
def check(r,stabilizer):
 assert (r.T*G*r)[0]==-2
 assert R(r)**2==I and R(r).T*G*R(r)==G
 if stabilizer:assert (h.T*G*r)[0]==0
F=X;roots=[]
for j,c in enumerate(A+B):
 z=S.zeros(21,1)
 for i,v in c.items():z[i]=v
 r=K*z if j<6 else (F-I)*K*z
 check(r,True);roots.append(r);F=R(r)*F
assert (F-I).rank()==2
u0=((F-I)**2).columnspace()[0]/6
for r in [I[:,20],I[:,20]+u0]:
 check(r,True);roots.append(r);F=R(r)*F
assert (F-I).rank()==2
D=F-I;u=S.Matrix.hstack(*D.columnspace())[:,0]
a=D*I[:,7]
T=lambda z:I+z*(u.T*G)-u*(z.T*G)-S.Rational((z.T*G*z)[0],2)*u*(u.T*G)
assert (u.T*G*u)[0]==0 and (u.T*G*a)[0]==0 and (a.T*G*a)[0]==-8
assert (I[:,7].T*G*u)[0]==1 and T(a)==F
r=-I[:,0]-I[:,1]-I[:,2]-I[:,12]+I[:,20];s=a-r
assert (r.T*G*r)[0]==(s.T*G*s)[0]==-2
assert (r.T*G*u)[0]==(s.T*G*u)[0]==0
assert T(r)*T(s)==F
finish=[r+u,r,s+u,s]
for z in finish:check(z,False);roots.append(z)
assert [int((h.T*G*z)[0]) for z in finish]==[-4,-4,4,4]
assert T(r)==R(r+u)*R(r)
assert T(s)==R(s+u)*R(s)
P=I
for z in roots:P=P*R(z)
assert len(roots)==25 and P==X
Fcheck=X
for z in roots:Fcheck=R(z)*Fcheck
assert Fcheck==I
result={'RQT':190,'status':'AMBIENT_FULL_FACTORISATION_PASS',
'root_count':25,'initial_roots_fix_h':21,'final_h_pairings':[-4,-4,4,4],
'stabilizer_only_factorization':'OPEN','residual_rank':0,
'root_vectors':[[int(x) for x in z] for z in roots]}
(p/'RQT-190-report.json').write_text(json.dumps(result,indent=2)+'\n')
print('RQT-190 PASS: 25 ambient (-2) roots, exact product X, residual identity')
