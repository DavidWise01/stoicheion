#!/usr/bin/env python3
"""RQT-244: exact arithmetic replay (requires RQT-242 and RQT-243 JSON supplied in ZIP)."""
import json,itertools
from pathlib import Path
import sympy as s
p=Path(__file__).resolve().parent
a=json.loads((p/'RQT-242-preliminary.json').read_text())
b=json.loads((p/'RQT-243-report.json').read_text())
F=s.Matrix(a['F4']);H=s.Matrix(a['W4']);V=s.Matrix(a['V'])
F5=s.Matrix(json.loads((p/'branch_2.json').read_text())['Gram_5x5'])
H5=s.Matrix(json.loads((p/'branch_2.json').read_text())['Wall_5x5'])
r17=s.Matrix(json.loads((p/'RQT-241-witness.json').read_text())['root_rank5'])
assert V.T*F5*V==F and V.T*H5*V==H and r17.T*H5.T*V==s.zeros(1,4)
idx=[1,2,3];P=-F.extract(idx,idx);J=P.inv();v=J*F.extract(idx,[0]);beta=F[0,0]+(v.T*P*v)[0]
assert all(P[:i,:i].det()>0 for i in range(1,4)) and beta>0
assert [s.sign(x) for x in v]==[1,-1,-1]
assert all(v[i]**2>(beta+2)*J[i,i] for i in range(3))
E=b['mod4_eligible_first_residues_for_full_mod8_flag']
d2=[x for x in E if all(int(y)%2==0 for y in F*s.Matrix(x))]
assert (len(E),len(d2))==(40,16)
z=s.Matrix(b['mod8_example_columns'][0]);assert list(z)==[0,1,1,5]
e=s.Matrix([0,0,1,0])
A=int(((z.T*F*z)[0]+2)/16);B=int((z.T*F*e)[0]);C=int(4*F[2,2])
assert (A,B,C)==(-14562385908299609109,16793193759917226115,-21080344320033532160)
t=0
for n in range(1,257):
 if (A+B*t+C*t*t)%(1<<n):t+=1<<(n-1)
assert t==93878330334900477488557551447004581630314366809978929771196499707722623893639
r=z+8*t*e
assert ((r.T*F*r)[0]+2)%(1<<260)==0
assert (r17.T*H5.T*V*r)[0]==0
assert (p/'search-1-10000.log').read_text().splitlines()[0]=='TOTAL 15240808 FOUND 0'
print('RQT-244 PASS: exact sign theorem, 24/16 split, 2-adic root mod 2^260, finite search log')
