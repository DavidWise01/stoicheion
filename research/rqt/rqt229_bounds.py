#!/usr/bin/env python3
"""RQT-229 exact rational cone bounds. Original-source evidence in downloadable ZIP."""
import json,math
from pathlib import Path
import sympy as s
p=Path(__file__).resolve().parent
F=s.Matrix(json.loads((p/'RQT-228-gram-4x4.json').read_text()))
idx=[0,1,3];P=-F.extract(idx,idx);Pi=P.inv();b=F.extract(idx,[2]);v=Pi*b;beta=F[2,2]+(b.T*v)[0]
assert all(P[:i,:i].det()>0 for i in range(1,4)) and beta>0
assert all(v[i]**2>(beta+2)*Pi[i,i] for i in range(3))
assert all(v[i]>0 for i in range(3))
count=0
with (p/'bounds.txt').open('w') as f:
 for t in range(1,25001):
  row=[t]
  for i in range(2):
   center=v[i]*t;rad2=(beta*t*t+2)*Pi[i,i]
   upper=math.isqrt(int(s.ceiling(rad2)))+1
   lo=int(s.floor(center))-upper-1
   hi=int(s.ceiling(center))+upper+1
   row.extend([lo,hi])
  count+=(row[2]-row[1]+1)*(row[4]-row[3]+1)
  f.write(' '.join(map(str,row))+'\n')
assert count==152127128
print('RQT-229 exact outward intervals PASS:',count)
