#!/usr/bin/env python3
"""RQT-188 exact extended root-reflection descent and rank-2 obstruction."""
import ast,hashlib,json
from pathlib import Path
import sympy as s
ROOT=Path(__file__).resolve().parent
SRC=ROOT/'source'
load=lambda fn:s.Matrix(ast.literal_eval((SRC/fn).read_text().strip()[7:-1]))
X=load('X-22x22.txt');G=load('gram-22x22.txt')
I=s.eye(22); h=s.Matrix([1]*4+[0]*18); a=h.T*G
assert X**4==I and X.T*G*X==G and X*h==h
K=s.Matrix.hstack(*[I[:,j]-I[:,0] if j<20 else I[:,j] for j in range(1,22)])
assert a*K==s.zeros(1,21)
prior=[{19:1},{20:1},{8:1,16:-1,20:1},{5:1,16:-1,19:1,20:1},{14:1,17:-1,19:-1,20:-1},{7:1,8:1,10:-1,16:-1,20:1}]
additions=[{20:1},{5:1,14:-1},{2:1,17:-1},{0:1,5:-1},{0:1,1:-1},{0:1},{15:1},{13:1},{7:1},{4:1},{8:1},{9:1},{12:1}]
F=X;reflections=[];ranks=[(F-I).rank()];records=[]
for j,coef in enumerate(prior+additions,1):
 c=s.zeros(21,1)
 for i,v in coef.items(): c[i]=v
 r=K*c if j<=6 else (F-I)*K*c
 assert a*r==s.zeros(1,1) and (r.T*G*r)[0]==-2
 R=I+r*(r.T*G)
 assert R**2==I and R.T*G*R==G and R*h==h and R.det()==-1
 F=R*F;reflections.append(R)
 ranks.append((F-I).rank())
 assert ranks[-1]==ranks[-2]-1
 records.append({'step':j,'type':'K*c' if j<=6 else '(Fprev-I)*K*c','c':{str(i):v for i,v in coef.items()},'rank':ranks[-1]})
Y=F
for R in reversed(reflections):Y=R*Y
assert Y==X and (F-I).rank()==2 and F.T*G*F==G
D=F-I;B=s.Matrix.hstack(*D.columnspace())
Q=B.T*G*B
assert Q==s.Matrix([[0,0],[0,-6]])
# Rational norm -2 requires a square root of 1/3, impossible in Q.
assert not s.sqrt(s.Rational(1,3)).is_rational
report={'boundary':'RQT-188','status':'MONOTONE_DESCENT_OBSTRUCTION_PROVEN',
'reflections':19,'added':13,'rank_sequence':ranks,'residual_rank':2,
'residual_det':int(F.det()),'image_gram':Q.tolist(),
'monotone_obstruction':'No rational square -2 vector in im(F-I)',
'full_factorization':'OPEN','roots':records,
'source_X_sha256':hashlib.sha256((SRC/'X-22x22.txt').read_bytes()).hexdigest(),
'source_G_sha256':hashlib.sha256((SRC/'gram-22x22.txt').read_bytes()).hexdigest()}
(ROOT/'RQT-188-report.json').write_text(json.dumps(report,indent=2)+'\n')
(ROOT/'RQT-188-residual-22x22.txt').write_text(str(F))
print(json.dumps({k:v for k,v in report.items() if k!='roots'},indent=2))
