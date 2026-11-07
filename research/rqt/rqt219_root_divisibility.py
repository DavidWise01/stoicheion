#!/usr/bin/env python3
"""RQT-219 exact finite root-divisibility census; uses local RQT-216-reduced-gram.json."""
import itertools,json
from pathlib import Path
import sympy as S
p=Path(__file__).resolve().parent
F=S.Matrix(json.loads((p/'RQT-216-reduced-gram.json').read_text()))
assert F==F.T and F.det()==-313982794406122741723132503868
assert all(F[i,i]%2==0 for i in range(6))
A=[[int(F[i,j]) for j in range(6)] for i in range(6)]
for mod,expect in ((4,(1920,128)),(8,(61440,8192))):
 counts={1:0,2:0}
 for x in itertools.product(range(mod),repeat=6):
  y=[sum(A[i][j]*x[j] for j in range(6)) for i in range(6)]
  if (sum(x[i]*y[i] for i in range(6))+2)%mod==0:
   counts[2 if all(z%2==0 for z in y) else 1]+=1
 assert tuple(counts[d] for d in (1,2))==expect
 print(f'RQT-219 mod {mod}:',counts)
binary={1:[],2:[]}
for x in itertools.product(range(2),repeat=6):
 y=[sum(A[i][j]*x[j] for j in range(6)) for i in range(6)]
 if (sum(x[i]*y[i] for i in range(6))+2)%4==0:
  binary[2 if all(z%2==0 for z in y) else 1].append(x)
assert len(binary[1])==30 and binary[2]==[(0,0,1,1,0,1),(1,1,0,1,0,0)]
D=abs(int(F.det()));assert 2*D==627965588812245483446265007736
assert D//2==156991397203061370861566251934
print('RQT-219 PASS: primitive-root divisibilities {1,2}; root existence OPEN')
