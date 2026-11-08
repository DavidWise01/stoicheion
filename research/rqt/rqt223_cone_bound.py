#!/usr/bin/env python3
"""Regenerates rigorous integer enclosures for the RQT-223 hyperbolic cone.
Requires SymPy and archived RQT-216-reduced-gram.json; compile search223.cpp
and run it with bounds-t1-300.txt for exhaustive search.
"""
import json,math
from pathlib import Path
import sympy as S
p=Path(__file__).resolve().parent
F=S.Matrix(json.loads((p/'RQT-216-reduced-gram.json').read_text()))
idx=[0,1,2,4,5];P=-F.extract(idx,idx);b=F.extract(idx,[3])
assert all(P[:j,:j].det()>0 for j in range(1,6))
Pinv=P.inv();v=Pinv*b;beta=F[3,3]+(b.T*v)[0]
assert beta>0
assert all(v[i]**2>(beta+2)*Pinv[i,i] for i in range(5))
assert F.det()==-313982794406122741723132503868
rows=[];count=0
for t in range(1,301):
 intervals=[]
 for i in range(5):
  center=v[i]*t;rad2=(beta*t*t+2)*Pinv[i,i]
  mid=int(S.floor(center));radius=math.isqrt(int(S.ceiling(rad2)))+2
  left,right=mid-radius,mid+radius
  assert left<center-S.sqrt(rad2) and right>center+S.sqrt(rad2)
  intervals.extend([left,right])
 count+=math.prod(intervals[i*2+1]-intervals[i*2]+1 for i in range(5))
 rows.append([t]+intervals)
assert count==13521104
(p/'bounds-t1-300.txt').write_text('\n'.join(' '.join(map(str,row)) for row in rows)+'\n')
print('RQT-223 exact bounds PASS; candidate count',count)
