#!/usr/bin/env python3
"""RQT-194 exact 25-root word audit; run RQT-193 script first for root JSON."""
import ast,json,hashlib
from pathlib import Path
import sympy as s
p=Path(__file__).resolve().parent
load=lambda n:s.Matrix(ast.literal_eval((p/'source'/n).read_text().strip()[7:-1]))
X=load('X-22x22.txt');G=load('gram-22x22.txt');I=s.eye(22)
h=s.Matrix([1]*4+[0]*18)
c=json.loads((p/'RQT-193-report.json').read_text())
roots=[s.Matrix(v) for v in c['all_25_roots_ambient']]
assert len(roots)==25
dot=lambda a,b:int((a.T*G*b)[0])
R=lambda v:I+v*(v.T*G)
for v in roots:
 assert dot(v,v)==-2 and dot(h,v)==0 and all(z.q==1 for z in v)
 assert R(v)**2==I and R(v).T*G*R(v)==G
def product(rs):
 P=I
 for v in rs:P=P*R(v)
 return P
assert product(roots)==X
rank=(X-I).rank()
assert rank==21 and X.det()==-1
repeats=[(i+1,j+1) for i in range(25) for j in range(i+1,25) if roots[i]==roots[j] or roots[i]==-roots[j]]
assert repeats==[(1,20)]
assert dot(roots[0],roots[1])==1
assert all(dot(roots[0],roots[j])==0 for j in range(2,19))
commuted=roots[:2]+[roots[19]]+roots[2:19]+roots[20:]
assert product(commuted)==X and commuted[0]==commuted[2]
a,b=commuted[0],commuted[1]
assert R(a)*R(b)*R(a)==R(b)*R(a)*R(b)
braided=[b,a,b]+commuted[3:]
assert product(braided)==X
for rs in (roots,commuted,braided):
 assert not any(rs[j]==rs[j+1] or rs[j]==-rs[j+1] for j in range(24))
possible=[n for n in range(rank,26) if n%2==1]
assert possible==[21,23,25]
report={'boundary':'RQT-194','status':'EXACT_WORD_NORMALIZATION_PASS',
'rank_X_minus_I':rank,'det_X':-1,'root_count':25,
'possible_minimal_lengths':possible,'repeated_root_positions':repeats,
'commuted_and_braided_products_equal_X':True,'adjacent_cancellations':0,
'shorter_factorization':'OPEN',
'X_sha256':hashlib.sha256((p/'source'/'X-22x22.txt').read_bytes()).hexdigest(),
'G_sha256':hashlib.sha256((p/'source'/'gram-22x22.txt').read_bytes()).hexdigest()}
(p/'RQT-194-report.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
