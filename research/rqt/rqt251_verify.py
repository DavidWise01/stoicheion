#!/usr/bin/env python3
"""RQT-251 exhaustive exact 36-backbone mod8 lift audit.
Requires RQT-242-preliminary.json from the conversation evidence ZIP.
"""
import itertools,json,collections,pathlib
j=json.loads((pathlib.Path(__file__).parent/'RQT-242-preliminary.json').read_text())
F=[[int(t) for t in r] for r in j['F4']]
H=[[int(t) for t in r] for r in j['W4']]
def bil(M,a,b):return sum(a[i]*M[i][k]*b[k] for i in range(4) for k in range(4))
E=[x for x in itertools.product(range(4),repeat=4) if bil(F,x,x)%8==6]
S=[[k for k,b in enumerate(E) if bil(H,b,a)%4==0] for a in E]
def lift(A):
 eq=[]
 for i,a in enumerate(A):
  q=bil(F,a,a)+2;assert q%8==0
  mask=sum(1<<(4*i+k) for k in range(4) if sum(F[k][j]*a[j] for j in range(4))&1)
  eq.append((mask,-(q//8)&1))
 for j in range(1,4):
  for i in range(j):
   a,b=A[j],A[i];w=bil(H,a,b);assert w%4==0
   mask=0
   for k in range(4):
    if sum(H[k][l]*b[l] for l in range(4))&1:mask|=1<<(4*j+k)
    if sum(a[l]*H[l][k] for l in range(4))&1:mask|=1<<(4*i+k)
   eq.append((mask,-(w//4)&1))
 piv={}
 for mask,rhs in eq:
  while mask:
   t=mask.bit_length()-1
   if t not in piv:piv[t]=(mask,rhs);break
   m,r=piv[t];mask^=m;rhs^=r
  if not mask and rhs:return False,len(piv)
 return True,len(piv)
seen=collections.Counter();good=collections.Counter();pos=collections.Counter();first=set()
for ia in range(len(E)):
 for ib in S[ia]:
  for ic in S[ia]:
   if ic not in S[ib]:continue
   for id in S[ia]:
    if id not in S[ib] or id not in S[ic]:continue
    A=(E[ia],E[ib],E[ic],E[id])
    key=tuple(tuple(x%2 for x in a) for a in A)
    seen[key]+=1
    ok,rank=lift(A)
    if ok:
     assert rank==7
     good[key]+=1;first.add(A[0])
     pat=tuple(i for i,a in enumerate(A) if all(sum(F[k][j]*a[j] for j in range(4))%2==0 for k in range(4)))
     pos[pat]+=1
assert len(E)==80 and len(seen)==len(good)==36
assert set(seen.values())=={512} and set(good.values())=={160}
assert sum(good.values())==5760 and len(first)==40
assert len(pos)==6 and set(pos.values())=={960}
assert 5760*(1<<(16-7))==2949120
v=[(4,5,5,1),(1,4,6,1),(5,0,3,3),(1,1,1,3)]
assert all((bil(F,a,a)+2)%16==0 for a in v)
assert all(bil(H,v[j],v[i])%8==0 for j in range(1,4) for i in range(j))
print('PASS: 36 backbones * 160 mod4 flags * 512 mod8 lifts = 2949120')
print('Integral norm-minus-two root18 remains OPEN')
