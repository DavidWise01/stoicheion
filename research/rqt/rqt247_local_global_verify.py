#!/usr/bin/env python3
"""RQT-247: independent exact prerequisites for global root18 existence.
Uses Hasse--Minkowski and weak approximation in the accompanying proof.
Does NOT claim to output explicit root coordinates.
"""
import sympy as s
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
assert H+H.T==-F and H.det()==1
D=s.eye(4)+H.inv()*F
assert D.det()==1 and D.T*F*D==F and (D-s.eye(4)).rank()==4
n=abs(int(F.det()))
factor=s.factorint(n)
assert factor=={2:2,3:2,4966811:1,140001169580740529:1,330823854880640721967014002817981344723960683:1}
assert all(s.isprime(prime) for prime in factor)
def matrix_rank_mod(A,p):
 rows=[[int(A[i,j])%p for j in range(A.cols)] for i in range(A.rows)]
 rank=0
 for j in range(A.cols):
  pivot=next((k for k in range(rank,A.rows) if rows[k][j]),None)
  if pivot is None:continue
  rows[rank],rows[pivot]=rows[pivot],rows[rank]
  inv=pow(rows[rank][j],-1,p)
  rows[rank]=[(x*inv)%p for x in rows[rank]]
  for k in range(rank+1,A.rows):
   t=rows[k][j]
   rows[k]=[(rows[k][i]-t*rows[rank][i])%p for i in range(A.cols)]
  rank+=1
 return rank
for p in factor:
 assert matrix_rank_mod(F,p)==(2 if p==2 else 3)
for p,coordinates in [(2,[0,0,0,1]),(3,[0,1,0,1])]:
 x=s.Matrix(coordinates)
 q=(x.T*F*x)[0]//2
 grad=F*x
 assert q%p==0 and any(int(c)%p for c in grad)
P=-F[1:4,1:4]
assert all(P[:i,:i].det()>0 for i in range(1,4))
b=F[1:4,0]
assert F[0,0]+(b.T*P.inv()*b)[0]>0
print("PASS RQT-247 local-global theorem hypotheses")
print("Integral root18 existence follows from Hasse--Minkowski, weak approximation and Bezout.")
print("Explicit integral coordinates NOT constructed.")
