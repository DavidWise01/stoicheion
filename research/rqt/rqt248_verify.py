#!/usr/bin/env python3
"""RQT-248 exact modular census. Supply RQT-242-preliminary.json alongside this script."""
import json,itertools
from collections import Counter
from pathlib import Path
d=json.loads((Path(__file__).resolve().parent/'RQT-242-preliminary.json').read_text())
F=[[int(v) for v in r] for r in d['F4']]
H=[[int(v) for v in r] for r in d['W4']]
def dot(M,x,y):return sum(x[i]*M[i][j]*y[j] for i in range(4) for j in range(4))
def is_d2(x):return all(sum(F[i][j]*x[j] for j in range(4))%2==0 for i in range(4))
E=[v for v in itertools.product(range(4),repeat=4) if dot(F,v,v)%8==6]
S=[[j for j,y in enumerate(E) if dot(H,y,x)%4==0] for x in E]
assert len(E)==80 and sum(map(is_d2,E))==32
cnt=Counter();pat=Counter();typecnt=Counter()
for a in range(len(E)):
 for b in S[a]:
  for c in S[a]:
   if c not in S[b]:continue
   for e in S[a]:
    if e not in S[b] or e not in S[c]:continue
    V=[E[i] for i in (a,b,c,e)]
    d2=[is_d2(x) for x in V]
    cnt[sum(d2)]+=1
    pat[tuple(i+1 for i in range(4) if d2[i])]+=1
    typecnt[tuple(sorted(tuple(z%2 for z in x) for x in V if is_d2(x)))]+=1
assert cnt=={2:18432}
assert set(pat.values())=={3072} and len(pat)==6
assert typecnt=={((1,0,1,1),(1,1,1,1)):18432}
print("RQT-248 PASS: all 18432 flags require two d2 roots of distinct fixed parities.")
