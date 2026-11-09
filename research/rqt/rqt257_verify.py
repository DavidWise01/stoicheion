#!/usr/bin/env python3
"""RQT-257 exact automatic reflection-product audit.
Inputs alongside script: RQT-242-preliminary.json, flag256.json.
Both are in the self-contained evidence ZIP in the conversation.
"""
import itertools,json
from pathlib import Path
import sympy as s
p=Path(__file__).resolve().parent
d=json.loads((p/"RQT-242-preliminary.json").read_text())
F=s.Matrix(d["F4"]);H=s.Matrix(d["W4"]);D=s.Matrix(d["D4"]);I=s.eye(4)
assert H.det()==1 and H+H.T==-F and I+H.inv()*F==D
for n in range(1,5):
 par=s.symbols("a:"+str(n*(n-1)//2))
 A=s.eye(n);k=0
 for i in range(n):
  for j in range(i+1,n):A[i,j]=par[k];k+=1
 Q=-A-A.T;P=s.eye(n)
 for i in range(n):
  e=s.eye(n)[:,i];P=P*(s.eye(n)+e*(e.T*Q))
 assert all(s.expand(t)==0 for t in P+A.inv()*A.T)
print("PASS universal Coxeter-Seifert product, n=1..4")
f=[[int(F[i,j])%8 for j in range(4)] for i in range(4)]
h=[[int(H[i,j])%4 for j in range(4)] for i in range(4)]
ds=[[int(D[i,j])%4 for j in range(4)] for i in range(4)]
def pair(M,a,b,m):
 return sum(a[i]*M[i][j]*b[j] for i in range(4) for j in range(4))%m
E=[x for x in itertools.product(range(4),repeat=4) if pair(f,x,x,8)==6]
links=[[j for j,b in enumerate(E) if pair(h,b,a,4)==0] for a in E]
def mul(A,B):
 return [[sum(A[i][k]*B[k][j] for k in range(4))%4 for j in range(4)] for i in range(4)]
def refl(a):
 w=[sum(a[i]*f[i][j] for i in range(4))%4 for j in range(4)]
 return [[(int(i==j)+a[i]*w[j])%4 for j in range(4)] for i in range(4)]
R=[refl(a) for a in E]
c=0
for ia in range(len(E)):
 for ib in links[ia]:
  B=mul(R[ia],R[ib])
  for ic in links[ia]:
   if ic not in links[ib]:continue
   C=mul(B,R[ic])
   for id in links[ia]:
    if id not in links[ib] or id not in links[ic]:continue
    assert mul(C,R[id])==ds
    c+=1
assert c==18432
print("PASS 18,432/18,432 modular products agree with residual D modulo4")
flag=json.loads((p/"flag256.json").read_text())
V=s.Matrix.hstack(*(s.Matrix(v) for v in flag["columns"]))
m=1<<256
assert V.det()%2==1
assert all(((V[:,i].T*F*V[:,i])[0]+2)%(2*m)==0 for i in range(4))
assert all((V[:,j].T*H*V[:,i])[0]%m==0 for i in range(4) for j in range(i+1,4))
P=I
for i in range(4):
 r=V[:,i];P=P*(I+r*(r.T*F))
assert all(int(t)%m==0 for t in P-D)
print("PASS product of four modular reflections equals D modulo 2^256")
print("Integral root18 and full 21-reflection factorization remain OPEN")
