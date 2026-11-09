#!/usr/bin/env python3
"""RQT-249 independent exact modular verifier; supply RQT-249-flag256.json alongside."""
import json
from pathlib import Path
import sympy as s
p=Path(__file__).resolve().parent
d=json.loads((p/'RQT-249-flag256.json').read_text())
F=s.Matrix([
[-4523390658618420908,2239380521691398176,-2422224054680331217,-3109472006028867029],
[2239380521691398176,-6703602364620082676,-1185189370853509030,4418426561730616356],
[-2422224054680331217,-1185189370853509030,-5270086080008383040,4649693842155823637],
[-3109472006028867029,4418426561730616356,4649693842155823637,-12373412455412906476]])
H=s.Matrix([
[2261695329309210454,-1051245631696015003,1175645097188971547,1627042015946053765],
[-1188134889995383173,3351801182310041338,491285385866907237,-2161158408172372287],
[1246578957491359670,693903984986601793,2635043040004191520,-2244501232348113591],
[1482429990082813264,-2257268153558244069,-2405192609807710046,6186706227706453238]])
V=s.Matrix.hstack(*(s.Matrix([int(x) for x in c]) for c in d['columns']))
m=1<<d['k']
assert d['k']==256 and H.det()==1 and H+H.T==-F
assert V.det()%2==1
assert all(((V[:,i].T*F*V[:,i])[0]+2)%(2*m)==0 for i in range(4))
W=V.T*H*V
assert all(W[j,i]%m==0 for j in range(1,4) for i in range(j))
assert all((W[i,i]-1)%m==0 for i in range(4))
d2=[i for i in range(4) if all(int(v)%2==0 for v in F*V[:,i])]
assert d2==[1,2]
assert {tuple(int(x)%2 for x in V[:,i]) for i in d2}=={(1,0,1,1),(1,1,1,1)}
print('RQT-249 PASS: full 4-column flag mod 2^256, norms mod 2^257')
print('Only a finite modular certificate; integral root18 still OPEN')
