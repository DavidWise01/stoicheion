#!/usr/bin/env python3
"""RQT-237 independent reduced-lattice modular certificate, using only Python integers.
For original-source 22-dimensional reconstruction, see the self-contained evidence ZIP.
"""
import itertools
F=[
[-331935524,416833484,-277568716,-235874521,-324291858],
[416833484,-589727438,358299877,269088278,384175690],
[-277568716,358299877,-314957708,-195969801,-188480532],
[-235874521,269088278,-195969801,-236294736,-229213494],
[-324291858,384175690,-188480532,-229213494,-403213522]]
H=[
[165967762,-214299870,139276223,112260608,161356137],
[-202533614,294863719,-175293696,-123691944,-184920207],
[138292493,-183006181,157478854,93628129,93058888],
[123613913,-145396334,102341672,118147368,120338015],
[162935721,-199255483,95421644,108875479,201606761]]
V=[
[200,164,880,61,305],
[820,704,501,796,486],
[1004,366,1004,760,1023],
[1020,5,1021,1023,1020],
[1021,1017,1020,2,1]]
def pair(M,a,b):
 return sum(a[i]*M[i][j]*b[j] for i in range(5) for j in range(5))
def mv(M,x):return [sum(M[i][j]*x[j] for j in range(5)) for i in range(5)]
cols=list(zip(*V))
assert all(pair(F,c,c)%2048==2046 for c in cols)
assert all(pair(H,cols[j],cols[i])%1024==0 for j in range(1,5) for i in range(j))
assert all(pair(H,c,c)%1024==1 for c in cols)
from sympy import Matrix
assert int(Matrix(V).det())%1024==1
candidates=[r for r in itertools.product(range(4),repeat=5) if pair(F,r,r)%8==6]
assert len(candidates)==272
fail_norm16=[r for r in candidates if pair(F,r,r)%16!=14 and all(x%2==0 for x in mv(F,r))]
assert len(fail_norm16)==20
# Independent full-flag mod4 test via memoized successors.
R=candidates
adj=[sum(1<<j for j,s in enumerate(R) if pair(H,s,r)%4==0) for r in R]
from functools import lru_cache
@lru_cache(None)
def complete(bits,depth):
 if depth==0:return True
 while bits:
  bit=bits&-bits;bits-=bit;i=bit.bit_length()-1
  if complete(bits&adj[i],depth-1):return True
 return False
all_bits=(1<<len(R))-1
viable={r for i,r in enumerate(R) if complete(all_bits&adj[i],4)}
assert len(viable)==152
assert set(fail_norm16)<=viable
assert len(viable-set(fail_norm16))==132
print('PASS: 132 possible first-root classes; full five-root Wall flag mod1024.')
print('NOT AN INTEGRAL ROOT FACTORIZATION.')
