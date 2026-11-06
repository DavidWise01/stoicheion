#!/usr/bin/env python3
"""RQT-181: reproducible exact form-transport audit (requires sympy).
Run RQT-180 script first (or let this script run it) to generate P.
"""
from pathlib import Path
import ast, json, runpy, hashlib
import sympy as s
root=Path(__file__).resolve().parent
read=lambda p:s.Matrix(ast.literal_eval(p.read_text().strip()[7:-1]))
x=read(root/'source'/'X-22x22.txt')
g=read(root/'source'/'gram-22x22.txt')
pfile=root/'P-22x22.txt'
if not pfile.exists():
    runpy.run_path(str(root/'rqt180_certificate.py'))
p=read(pfile)
cyc=s.zeros(4)
for j in range(4):cyc[(j+1)%4,j]=1
h=s.Matrix([[-1,0,0],[0,0,-1],[1,1,0]])
y=s.diag(cyc,*([h]*6))
t=p.T*g*p
def inertia(B):
    B=s.Matrix(B); pos=neg=0
    while B.rows:
        k=next((i for i in range(B.rows) if B[i,i]!=0),None)
        if k is None:
            i,j=next((i,j) for i in range(B.rows) for j in range(i+1,B.rows) if B[i,j]!=0)
            B[:,i]=B[:,i]+B[:,j]
            B[i,:]=B[i,:]+B[j,:]
            k=i
        if k:B.row_swap(0,k);B.col_swap(0,k)
        a=B[0,0]
        pos+=1 if a>0 else 0
        neg+=1 if a<0 else 0
        if B.rows==1:break
        v=B[1:,0]
        B=B[1:,1:]-v*v.T/a
    return [pos,neg]
assert x.shape==g.shape==p.shape==(22,22)
assert x**4==s.eye(22) and p.det(method='domain-ge')==1 and x*p==p*y
assert g==g.T and t==t.T
assert x.T*g*x==g and y.T*t*y==t
assert g.det(method='domain-ge')==t.det(method='domain-ge')==-1
assert all(g[i,i]%2==0 and t[i,i]%2==0 for i in range(22))
assert inertia(g)==inertia(t)==[3,19]
assert t[:4,:4]==s.Matrix([[-2,1,1,1],[1,-2,1,1],[1,1,-2,1],[1,1,1,-2]])
assert t[:4,:4].det()==-27
blocks=[(0,4)]+[(4+3*i,7+3*i) for i in range(6)]
zero=[];nonzero=[]
for i,(a,b) in enumerate(blocks):
    for j,(c,d) in enumerate(blocks):
        if j<=i:continue
        (zero if t[a:b,c:d]==s.zeros(b-a,d-c) else nonzero).append([i,j])
assert len(nonzero)==19 and len(zero)==2
(root/'G-canonical-22x22.txt').write_text(str(t))
report={'boundary':'RQT-181','status':'PASS','det':-1,'signature':[3,19],
        'even':True,'canonical_type':'C4 + H^6',
        'regular_sector_gram_det':-27,
        'nonzero_cross_block_pairs':len(nonzero),'zero_pairs':zero,
        'gram_sha256':hashlib.sha256((root/'source'/'gram-22x22.txt').read_bytes()).hexdigest()}
(root/'RQT-181-report.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
