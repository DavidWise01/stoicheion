#!/usr/bin/env python3
"""RQT-236 exact first-root modular gate. Requires branch_2.json from evidence ZIP."""
import itertools,json
from pathlib import Path
from functools import lru_cache
p=Path(__file__).resolve().parent
d=json.loads((p/'branch_2.json').read_text())
F=d['Gram_5x5'];H=d['Wall_5x5']
E=[v for v in itertools.product(range(4),repeat=5) if sum(v[i]*F[i][j]*v[j] for i in range(5) for j in range(5))%8==6]
def pairing(a,b):
 return sum(a[i]*H[i][j]*b[j] for i in range(5) for j in range(5))%4
successors=[sum(1<<j for j,v in enumerate(E) if pairing(v,u)==0) for u in E]
@lru_cache(None)
def extension(allowed,depth):
 if depth==0:return ()
 if not allowed:return None
 bits=allowed
 while bits:
  bit=bits&-bits;bits-=bit;j=bit.bit_length()-1
  tail=extension(allowed&successors[j],depth-1)
  if tail is not None:return (j,)+tail
 return None
all_bits=(1<<len(E))-1
viable=[E[i] for i in range(len(E)) if extension(all_bits&successors[i],4) is not None]
blocked=[E[i] for i in range(len(E)) if extension(all_bits&successors[i],4) is None]
assert (len(E),len(viable),len(blocked))==(272,152,120)
print('RQT-236 PASS: eligible 272; viable first roots 152; blocked 120')
