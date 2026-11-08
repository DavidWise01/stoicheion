#!/usr/bin/env python3
"""RQT-241: self-contained reduced arithmetic verification (SymPy).
Full 22-dimensional replay and constructive LLL algorithm are in evidence ZIP.
"""
import sympy as s
J=s.Matrix([[-8319932,-3097057,2813438,-1794298,-149943],[-3097057,-15432094,-1413796,393685,5285590],[2813438,-1413796,-19053854,3128649,-2048137],[-1794298,393685,3128649,-10194696,4874825],[-149943,5285590,-2048137,4874825,10734700]])
B=s.Matrix([[-16,-2,-11,58,144],[-2,0,-1,7,17],[7,1,5,-25,-63],[1,0,1,-4,-9],[7,1,5,-26,-65]])
u=s.Matrix([240,45,-135,-545,786]);v=s.Matrix([12,-143,4,54,-9])
assert s.igcd(*u)==1 and (u.T*J*u)[0]==0 and (u.T*J*v)[0]==1
assert (v.T*J*v)[0]%2==0
w=v-((v.T*J*v)[0]//2)*u
r=u-w
assert (w.T*J*w)[0]==0 and (u.T*J*w)[0]==1 and (r.T*J*r)[0]==-2
assert list(r)==[-39770729434092,-7457011768747,22371035306666,90312698089836,-130249138896603]
assert B.det()==-1
assert list(B*r)==[-13112575205790704,-1524876051051881,5773881356966028,793591763582657,5944066936669398]
print("PASS explicit integral norm-minus-two root: reduced arithmetic")
