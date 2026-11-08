#!/usr/bin/env python3
"""RQT-243: exact reduced 4D modular lifting audit; full source replay in evidence ZIP."""
import json,itertools
from collections import Counter
from pathlib import Path
from sympy import Matrix
p=Path(__file__).resolve().parent
D=json.loads((p/"RQT-242-preliminary.json").read_text())
F=D["F4"];H=D["W4"]
def dot(M,x,y):return sum(x[i]*int(M[i][j])*y[j] for i in range(4) for j in range(4))
def unit(k):return tuple(int(i==k) for i in range(4))
def lift(V,m=4):
 eq=[]
 for i,r in enumerate(V):
  q=dot(F,r,r)+2;assert q%(2*m)==0
  mask=sum(1<<(4*i+k) for k in range(4) if dot(F,r,unit(k))%2)
  eq.append((mask,-(q//(2*m))%2))
 for j in range(1,4):
  for i in range(j):
   a,b=V[j],V[i];w=dot(H,a,b);assert w%m==0
   mask=0
   for k in range(4):
    if dot(H,unit(k),b)%2:mask|=1<<(4*j+k)
    if dot(H,a,unit(k))%2:mask|=1<<(4*i+k)
   eq.append((mask,-(w//m)%2))
 piv={}
 for mask,rhs in eq:
  while mask:
   pos=mask.bit_length()-1
   if pos not in piv:piv[pos]=(mask,rhs);break
   mm,rr=piv[pos];mask^=mm;rhs^=rr
  if not mask and rhs:return False
 return True
E=[x for x in itertools.product(range(4),repeat=4) if dot(F,x,x)%8==6]
assert len(E)==80
S=[[j for j,v in enumerate(E) if dot(H,v,u)%4==0] for u in E]
norm={x for x in E if any((dot(F,tuple(x[k]+4*((bits>>k)&1) for k in range(4)),tuple(x[k]+4*((bits>>k)&1) for k in range(4)))+2)%16==0 for bits in range(16))}
count=0;good=0;first=set()
for a in range(len(E)):
 for b in S[a]:
  for c in S[a]:
   if c not in S[b]:continue
   for d in S[a]:
    if d not in S[b] or d not in S[c]:continue
    count+=1
    if lift((E[a],E[b],E[c],E[d])):
     good+=1;first.add(E[a])
assert (len(norm),count,good,len(first))==(64,18432,5760,40)
V=Matrix.hstack(*[Matrix(v) for v in [(53,16,90,5),(73,6,119,57),(105,77,89,101),(21,81,119,22)]])
G=Matrix(F);W=Matrix(H)
assert V.det()%128==1
assert all(int((V[:,i].T*G*V[:,i])[0])%256==254 for i in range(4))
assert all(int((V[:,j].T*W*V[:,i])[0])%128==0 for j in range(1,4) for i in range(j))
print('RQT-243 PASS: 80, 64, 40 root classes; 18432, 5760 flags; witness mod128')
