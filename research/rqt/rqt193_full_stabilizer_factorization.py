#!/usr/bin/env python3
"""RQT-193 exact 25-reflection factorization inside K=h-perp of original X."""
import ast,json,hashlib
from pathlib import Path
import sympy as S
p=Path(__file__).resolve().parent;src=p/'source'
load=lambda n:S.Matrix(ast.literal_eval((src/n).read_text().strip()[7:-1]))
X=load('X-22x22.txt');G=load('gram-22x22.txt')
I=S.eye(22);h=S.Matrix([1]*4+[0]*18)
K=S.Matrix.hstack(*[I[:,j]-I[:,0] if j<20 else I[:,j] for j in range(1,22)])
assert X**4==I and X.T*G*X==G and X*h==h and h.T*G*K==S.zeros(1,21)
A=[{19:1},{20:1},{8:1,16:-1,20:1},{5:1,16:-1,19:1,20:1},{14:1,17:-1,19:-1,20:-1},{7:1,8:1,10:-1,16:-1,20:1}]
B=[{20:1},{5:1,14:-1},{2:1,17:-1},{0:1,5:-1},{0:1,1:-1},{0:1},{15:1},{13:1},{7:1},{4:1},{8:1},{9:1},{12:1}]
R=lambda v:I+v*(v.T*G)
def verify(v):
 assert (v.T*G*v)[0]==-2 and (h.T*G*v)[0]==0
 assert R(v)**2==I and R(v).T*G*R(v)==G and R(v)*h==h
 assert all(x.q==1 for x in v)
F=X;roots=[];ranks=[(F-I).rank()]
for j,terms in enumerate(A+B):
 c=S.zeros(21,1)
 for i,n in terms.items():c[i]=n
 v=K*c if j<6 else (F-I)*K*c
 verify(v);roots.append(v);F=R(v)*F;ranks.append((F-I).rank())
 assert ranks[-1]==ranks[-2]-1
assert len(roots)==19 and (F-I).rank()==2
u0=((F-I)**2).columnspace()[0]/6
for v in (I[:,20],I[:,20]+u0):
 verify(v);roots.append(v);F=R(v)*F;ranks.append((F-I).rank())
assert ranks[-3:]==[2,3,2]
D=F-I;u=S.Matrix.hstack(*D.columnspace())[:,0];a=D*I[:,7]
dot=lambda x,y:(x.T*G*y)[0]
assert dot(u,u)==dot(u,a)==0 and dot(a,a)==-8 and dot(I[:,7],u)==1
T=lambda z:I+z*(u.T*G)-u*(z.T*G)-S.Rational(dot(z,z),2)*u*(u.T*G)
assert F==T(a)
coeff=S.Matrix([0,0,-1,2,1,3,0,0,0,0,0,-1,-2,-1,-2,1,-1,2,-1,4,3])
r=K*coeff;s=a-r;z=2*r-a
assert dot(r,r)==dot(s,s)==-2 and dot(u,r)==dot(u,s)==0
assert dot(h,r)==dot(h,s)==0 and dot(a,r)==dot(a,s)==-4
assert dot(z,z)==dot(z,u)==dot(z,a)==0
assert all(v.q==1 for v in K.gauss_jordan_solve(z-a)[0])
assert T(r)*T(s)==F and T(r)==R(r+u)*R(r) and T(s)==R(s+u)*R(s)
for v in (r+u,r,s+u,s):verify(v);roots.append(v)
P=I
for v in roots:P=P*R(v)
assert len(roots)==25 and P==X
Z=X
for v in roots:Z=R(v)*Z
assert Z==I
out={'boundary':'RQT-193','status':'FULL_STABILIZER_FACTORIZATION_PASS',
'roots':25,'all_roots_square_minus_two':True,'all_roots_fix_h':True,'product_equals_original_X':True,
'residual_identity':True,'K_witness_coefficients':list(map(int,coeff)),
'all_25_original_coordinate_roots':[list(map(int,v)) for v in roots],
'X_sha256':hashlib.sha256((src/'X-22x22.txt').read_bytes()).hexdigest(),
'G_sha256':hashlib.sha256((src/'gram-22x22.txt').read_bytes()).hexdigest(),
'minimal_word_length':'OPEN','full_stabilizer_generation':'OPEN'}
(p/'RQT-193-report.json').write_text(json.dumps(out,indent=2)+'\n')
print('RQT-193 PASS: 25 original-lattice (-2) root reflections, all fix h, product X')
