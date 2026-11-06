#!/usr/bin/env python3
"""RQT-187: Six integral -2-root reflections on the original 22D action."""
import ast,json
from pathlib import Path
import sympy as sp
ROOT=Path(__file__).resolve().parent
SRC=ROOT/'source'
read=lambda name:sp.Matrix(ast.literal_eval((SRC/name).read_text().strip()[7:-1]))
X=read('X-22x22.txt');G=read('gram-22x22.txt')
I=sp.eye(22);h=sp.Matrix([1]*4+[0]*18);a=h.T*G
assert X**4==I and X.T*G*X==G and X*h==h
K=sp.Matrix.hstack(*[I[:,j]-I[:,0] if j<20 else I[:,j] for j in range(1,22)])
assert a*K==sp.zeros(1,21)
seeds=[{19:1},{20:1},{8:1,16:-1,20:1},{5:1,16:-1,19:1,20:1},{14:1,17:-1,19:-1,20:-1},{7:1,8:1,10:-1,16:-1,20:1}]
F=X;reflections=[];ranks=[(X-I).rank()]
for seed in seeds:
 c=sp.zeros(21,1)
 for i,v in seed.items():c[i]=v
 r=K*c
 assert (r.T*G*r)[0]==-2 and a*r==sp.zeros(1,1)
 R=I+r*(r.T*G)
 assert R**2==I and R.T*G*R==G and R*h==h and R.det()==-1
 F=R*F;reflections.append(R)
 ranks.append((F-I).rank())
 assert ranks[-1]==ranks[-2]-1
Z=F
for R in reversed(reflections):Z=R*Z
assert Z==X and F.T*G*F==G
report={'boundary':'RQT-187','status':'PARTIAL_CERTIFICATE_PASS','rank_sequence':ranks,'root_count':6,'complete_factorization':False,'roots_sparse':seeds}
(ROOT/'RQT-187-report.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
