# RQT-207 — Seventh exact integral Wall root

**2026-11-07 | Original RQT-122 Gram and RQT-133 operator.**

The saturated rank-15 integer Wall kernel of RQT-206 contains a seventh integral square-(−2) root.

Coordinates in the index-64 RQT-198 basis:

`[4,-20,-102,3,8,0,28,32,112,19,-2,-3,36,53,21,1,-37,-34,51,-40,36]`

Original ambient 22-coordinate root:

`[-43,-91,-83,-102,3,8,0,28,32,112,55,12,-3,36,53,21,-18,-37,-34,51,-44,36]`

Using the original matrices, exact tests prove the root has square −2, is perpendicular to h, and lies in the integer kernel of all six prior one-sided Wall constraints. The seven root vectors are independent and their Wall pairing is upper-unitriangular:

```
[1,0,0,0,-7,115,10]
[0,1,0,3,-36,-11,-1]
[0,0,1,-1,21,-17,2]
[0,0,0,1,62,-457,-48]
[0,0,0,0,1,5116,658]
[0,0,0,0,0,1,-799]
[0,0,0,0,0,0,1]
```

The seventh root's reflection is an exact integral involution preserving G and fixing h. The witness came from a unimodular LLL change of basis on the saturated integer kernel using coefficients `[-59,14,-6,-6,33,21,-47,30,-39,45,42,-47,29,24,7]`.

**Exact audit PASS.** This certifies seven roots; it does not yet provide a complete 21-root factorization. The possible shortest root word lengths remain 21 or 23.

**Reproduction:** original source matrices, prior RQT-198/201/203/204/205/206 reports, executable `rqt207_verify.py`, and machine-readable root data are included in the standalone downloadable evidence archive.

**RQT-208:** Construct the saturated rank-14 integer kernel of the seven Wall constraints and seek an eighth exact integral square−2 root.
