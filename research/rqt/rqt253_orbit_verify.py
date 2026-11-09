#!/usr/bin/env python3
"""RQT-253 symbolic integral Eichler orbit proof. Requires SymPy."""
import sympy as s
a,b,k,m,n,p,q=s.symbols("a b k m n p q",integer=True)
G=s.Matrix([[0,1,0,0],[1,0,0,0],[0,0,-2*a,2*k],[0,0,2*k,-2*b]])
I=s.eye(4);u=I[:,0];w=I[:,1]
def bil(x,y):return (x.T*G*y)[0]
def trans(x,y):
 z=x*I[:,2]+y*I[:,3]
 return I+z*(u.T*G)-u*(z.T*G)-s.expand(bil(z,z)/2)*u*(u.T*G)
def root(x,y):
 z=x*I[:,2]+y*I[:,3]
 return u-w-z+s.expand(bil(z,z)/2)*u
T=trans(m,n);r=root(m,n)
assert bil(r,r)==-2 and bil(r,u)==-1
assert all(s.expand(x)==0 for x in T.T*G*T-G)
assert s.expand(T.det()-1)==0
assert all(s.expand(x)==0 for x in trans(m,n)*trans(p,q)-trans(m+p,n+q))
assert T*root(0,0)==r
assert (r[2],r[3])==(-m,-n)
print("PASS RQT-253: infinite Z² orbit of primitive norm−2 integral roots")
print("LIMIT: an explicit U-splitting in original F4 coordinates is not yet known")
