#!/usr/bin/env python3
"""RQT-195: deterministic Hurwitz shortening, exact original-matrix certificate."""
import ast, json, random
from pathlib import Path
import numpy as np
import sympy as S
p=Path(__file__).resolve().parent
read=lambda f:S.Matrix(ast.literal_eval((p/'source'/f).read_text().strip()[7:-1]))
X=read('X-22x22.txt');G=read('gram-22x22.txt')
I=S.eye(22);h=S.Matrix([1]*4+[0]*18)
starting=json.loads((p/'RQT-193-report.json').read_text())['all_25_roots_ambient']
A=[np.array(v,dtype=np.int64) for v in starting];GN=np.array(G.tolist(),dtype=np.int64)
rng=random.Random(194)
def norm(v):return int(max(abs(x) for x in v))
def canonical(v):
 t=tuple(int(x) for x in v)
 return min(t,tuple(-x for x in t))
def search(A,maxrestart,steps,cap=1000):
 tot=0
 for restart in range(maxrestart):
  arr=[v.copy() for v in A];prev=-1;moves=[]
  for step in range(steps):
   i=rng.randrange(len(arr)-1)
   if i==prev and rng.random()<.7:continue
   a,b=arr[i],arr[i+1];pairing=int(a@GN@b)
   if abs(pairing)>16:continue
   forward=rng.randrange(2)
   c=(a+pairing*b) if forward else (b+pairing*a)
   if norm(c)>cap:continue
   arr[i],arr[i+1]=(b.copy(),c) if forward else (c,a.copy())
   prev=i;tot+=1;moves.append([i,forward])
   if canonical(arr[i])==canonical(arr[i+1]):
    arr=arr[:i]+arr[i+2:]
    return arr,{'restart':restart,'step':step,'accepted_moves':len(moves),'moves':moves,'cancellation_position':i,'total_moves_across_restarts':tot}
 return None,{'tested_moves':tot,'restarts':maxrestart,'steps_per_restart':steps}
short,stage=search(A,100,500)
assert short is not None and len(short)==23 and len(stage['moves'])==308
nextword,stage2=search(short,800,900)
assert nextword is None and stage2['tested_moves']==493356
reflect=lambda r:I+r*(r.T*G)
prod=I
for v in short:
 r=S.Matrix([int(x) for x in v])
 assert (r.T*G*r)[0]==-2 and (h.T*G*r)[0]==0
 prod=prod*reflect(r)
assert prod==X and (X-I).rank()==21 and X.det()==-1
proof={'initial_roots':starting,'final_roots':[v.tolist() for v in short],'stages':[stage,stage2]}
(p/'RQT-195-hurwitz-proof.json').write_text(json.dumps(proof,indent=1)+'\n')
(p/'RQT-195-report.json').write_text(json.dumps({'boundary':'RQT-195','status':'EXACT_23_ROOT_CERTIFICATE','shorter_word':23,'lower_bound':21,'possible_minimum':[21,23],'moves':308,'product_equals_original_X':True,'global_minimum_proven':False},indent=2)+'\n')
print('PASS: 23 stabilizer-preserving roots exactly multiply to original X; length minimum OPEN')
