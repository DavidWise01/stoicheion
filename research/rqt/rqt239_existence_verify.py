#!/usr/bin/env python3
"""RQT-239 exact arithmetic premises; original matrices in self-contained evidence ZIP."""
import json,sympy as s
from pathlib import Path
p=Path(__file__).resolve().parent
F=s.Matrix(json.loads((p/'branch_2.json').read_text())['Gram_5x5'])
D=312669187727137013416789354039323478
assert F.det()==D and F==F.T and all(int(F[i,i])%2==0 for i in range(5))
assert s.factorint(D)=={2:1,139801:1,7915189:1,646956613:1,218377739361227:1}
P=-F[1:5,1:5]
assert all(P[:i,:i].det()>0 for i in range(1,5))
b=F[1:5,0];assert (F[0,0]+(b.T*P.inv()*b)[0])>0
B=s.Matrix([[-16,-2,-11,58,144],[-2,0,-1,7,17],[7,1,5,-25,-63],[1,0,1,-4,-9],[7,1,5,-26,-65]])
J=s.Matrix([[-8319932,-3097057,2813438,-1794298,-149943],[-3097057,-15432094,-1413796,393685,5285590],[2813438,-1413796,-19053854,3128649,-2048137],[-1794298,393685,3128649,-10194696,4874825],[-149943,5285590,-2048137,4874825,10734700]])
assert B.det()==-1 and B.T*F*B==J
assert (p/'search.log').read_text().strip()=='TESTED 43046721 positive 43046720 square 0 divisible 0 exact 0'
print('RQT-239 PASS: even indefinite rank-five Gram with squarefree determinant.')
print('Meyer + divisibility-one + Bezout imply global norm−2 root existence.')
print('The theorem is existential; explicit coordinates remain OPEN.')
