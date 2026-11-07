#!/usr/bin/env python3
"""RQT-199: Y-invariance and finite image quotient for an index-64 candidate."""
import ast,json,hashlib
from pathlib import Path
import sympy as s
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ
p=Path(__file__).resolve().parent
def load(n):return s.Matrix(ast.literal_eval((p/'source'/n).read_text().strip()[7:-1]))
X=load('X-22x22.txt');G=load('gram-22x22.txt');I=s.eye(22);h=s.Matrix([1]*4+[0]*18)
K=s.Matrix.hstack(*[I[:,j]-I[:,0] if j<20 else I[:,j] for j in range(1,22)])
GK=K.T*G*K;Y=(X*K)[1:22,:];D=Y-s.eye(21);W=GK*D.inv()
B=s.Matrix(json.loads((p/'RQT-198-report.json').read_text())['basis_21x21'])
assert X**4==I and X.T*G*X==G and X*h==h and K*Y==X*K
assert GK.det()==-4 and D.det()==-16384 and W.det()==s.Rational(1,4096)
assert abs(B.det())==64
H=B.T*W*B;Q=B.T*GK*B
assert all(z.q==1 for z in H) and H.det()==1 and H+H.T==-Q
YB=B.inv()*Y*B;J=B.inv()*D
assert all(z.q==1 for z in YB) and all(z.q==1 for z in J)
smith=lambda M:[abs(int(smith_normal_form(M,domain=ZZ)[i,i])) for i in range(21)]
sn_J=smith(J);sn_YB=smith(YB-s.eye(21))
assert sn_J==[1]*14+[2]*6+[4] and sn_YB==[1]*8+[2]*12+[4]
assert s.prod(sn_J)==256
from sympy.polys.matrices import DomainMatrix
R=DomainMatrix.from_Matrix((YB-s.eye(21)).applyfunc(lambda x:int(x)%2)).convert_to(s.GF(2)).rank()
assert R==8
out={'RQT':199,'status':'EXACT_CANDIDATE_ADMISSION_PASS','index':64,
 'Y_stable':True,'contains_image_Y_minus_I_K':True,'Wall_integral':True,'Wall_unimodular':True,
 'quotient_L_over_image':'(Z/2)^6 + Z/4','quotient_smith':sn_J,'quotient_order':256,
 'smith_Y_minus_I_on_L':sn_YB,'mod2_rank_Y_minus_I_on_L':8,
 '21_reflection_word':'OPEN','minimum_candidates':[21,23],
 'source_sha256':{n:hashlib.sha256((p/'source'/n).read_bytes()).hexdigest() for n in ['X-22x22.txt','gram-22x22.txt']}}
(p/'RQT-199-report.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
