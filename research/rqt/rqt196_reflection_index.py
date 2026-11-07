#!/usr/bin/env python3
"""RQT-196 original-source reflection-lattice index certificate."""
import ast,json,hashlib
from pathlib import Path
import sympy as s
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ
p=Path(__file__).resolve().parent
load=lambda n:s.Matrix(ast.literal_eval((p/'source'/n).read_text().strip()[7:-1]))
X=load('X-22x22.txt');G=load('gram-22x22.txt');I=s.eye(22)
h=s.Matrix([1]*4+[0]*18)
K=s.Matrix.hstack(*[I[:,j]-I[:,0] if j<20 else I[:,j] for j in range(1,22)])
GK=K.T*G*K;Y=(X*K)[1:22,:];D=s.eye(21)-Y
assert X**4==I and X.T*G*X==G and X*h==h
assert h.T*G*K==s.zeros(1,21) and K*Y==X*K
assert GK.det()==-4 and D.det()==2**14
sn_D=smith_normal_form(D,domain=ZZ)
snf_D=[abs(int(sn_D[j,j])) for j in range(21)]
assert snf_D==[1]*14+[4]*7
proof=json.loads((p/'RQT-195-hurwitz-proof.json').read_text())
roots=[s.Matrix(v) for v in proof['final_roots']]
assert len(roots)==23
R=lambda r:I+r*(r.T*G)
P=I
for r in roots:
 assert (r.T*G*r)[0]==-2 and (h.T*G*r)[0]==0
 assert all(v.q==1 for v in r)
 P=P*R(r)
assert P==X
B=s.Matrix.hstack(*[r[1:22,0] for r in roots])
assert K*B==s.Matrix.hstack(*roots)
sn_B=smith_normal_form(B,domain=ZZ)
snf_B=[abs(int(sn_B[j,j])) for j in range(21)]
assert snf_B==[1]*19+[4,4]
existing_index=int(s.prod(snf_B))
required_sq=int(D.det()//abs(GK.det()))
required_index=s.integer_nthroot(required_sq,2)
assert required_index==(64,True) and existing_index==16
out={'boundary':'RQT-196','status':'EXACT_NECESSARY_INDEX_INVARIANT',
'Gram_K_determinant':int(GK.det()),'det_I_minus_Y':int(D.det()),
'Smith_I_minus_Y':snf_D,'existing_23_root_word_length':23,
'existing_root_lattice_Smith':snf_B,'existing_root_lattice_index':16,
'hypothetical_21_root_lattice_index_required':64,
'possible_minimal_reflection_lengths':[21,23],'21_root_existence':'OPEN',
'X_sha256':hashlib.sha256((p/'source'/'X-22x22.txt').read_bytes()).hexdigest(),
'G_sha256':hashlib.sha256((p/'source'/'gram-22x22.txt').read_bytes()).hexdigest()}
(p/'RQT-196-report.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
