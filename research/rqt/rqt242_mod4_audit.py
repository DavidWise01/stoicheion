#!/usr/bin/env python3
"""RQT-242 exact reduced modular census. Original 22D replay in evidence ZIP."""
from itertools import product
import sympy as s
F=s.Matrix([["-4523390658618420908","2239380521691398176","-2422224054680331217","-3109472006028867029"],["2239380521691398176","-6703602364620082676","-1185189370853509030","4418426561730616356"],["-2422224054680331217","-1185189370853509030","-5270086080008383040","4649693842155823637"],["-3109472006028867029","4418426561730616356","4649693842155823637","-12373412455412906476"]])
H=s.Matrix([["2261695329309210454","-1051245631696015003","1175645097188971547","1627042015946053765"],["-1188134889995383173","3351801182310041338","491285385866907237","-2161158408172372287"],["1246578957491359670","693903984986601793","2635043040004191520","-2244501232348113591"],["1482429990082813264","-2257268153558244069","-2405192609807710046","6186706227706453238"]])
assert F.det()==-8281492574115056973770683990411769007319047636247715225543944839911172
assert H.det()==1 and H+H.T==-F
def pair(M,x,y):
 return sum(x[i]*int(M[i,j])*y[j] for i in range(4) for j in range(4))
E=[x for x in product(range(4),repeat=4) if pair(F,x,x)%8==6]
pairs=[(x,y) for x in E for y in E if pair(H,y,x)%4==0]
triples=0;quadruples=0;odd=0
for x,y in pairs:
 for z in E:
  if pair(H,z,x)%4 or pair(H,z,y)%4:continue
  triples+=1
  for w in E:
   if any(pair(H,w,u)%4 for u in (x,y,z)):continue
   quadruples+=1
   odd+=int(s.Matrix.hstack(*map(s.Matrix,(x,y,z,w))).det()%2!=0)
assert (len(E),len(pairs),triples,quadruples,odd)==(80,1504,9216,18432,18432)
print("RQT-242 PASS: 80 residues, 1504 pairs, 9216 triples, 18432 unimodular flags")
