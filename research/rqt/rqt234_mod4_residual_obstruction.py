#!/usr/bin/env python3
"""RQT-234 exact mod-four obstruction. Requires SymPy only.
The F4 and H4 below are exact certified RQT-233 matrices; independently
reconstruct both from original 22x22 sources using the attached evidence ZIP.
"""
import itertools
import sympy as s
F=s.Matrix([
[-17801313208674,-15761198498141,15135416925109,7424607432690],
[-15761198498141,-18808565513138,15151261558975,6742605417749],
[15135416925109,15151261558975,-13901548148824,-5277176639089],
[7424607432690,6742605417749,-5277176639089,-6096520821564]
])
H=s.Matrix([
[8900656604337,7817901014580,-7516765368317,-3763560697400],
[7943297483561,9404282756569,-7589636759966,-3436362525320],
[-7618651556792,-7561624799009,6950774074412,2700149229421],
[-3661046735290,-3306242892429,2577027409668,3048260410782]
])
assert H.det()==1 and H+H.T==-F
assert H.applyfunc(lambda x:x%4)==s.Matrix([[1,0,3,0],[1,1,2,0],[0,3,0,1],[2,3,0,2]])
f=[[int(F[i,j])%8 for j in range(4)] for i in range(4)]
w=[[int(H[i,j])%4 for j in range(4)] for i in range(4)]
q=lambda x:sum(x[i]*f[i][j]*x[j] for i in range(4) for j in range(4))%8
pair=lambda x,y:sum(x[i]*w[i][j]*y[j] for i in range(4) for j in range(4))%4
roots=[x for x in itertools.product(range(4),repeat=4) if q(x)==6]
assert len(roots)==64
assert all(pair(v,v)==1 for v in roots)
pairs=[(a,b) for a in roots for b in roots if pair(b,a)==0]
assert len(pairs)==768
triples=sum(pair(c,a)==0 and pair(c,b)==0 for a,b in pairs for c in roots)
assert triples==0
print('RQT-234 PASS: root residues 64; ordered pairs 768; triples 0')
print('Four integral reflections cannot complete this 17-root prefix.')
