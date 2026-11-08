# RQT-227 — Seventeenth integral Wall root (exact PASS)

**2026-11-07.** The frozen rank-five kernel of RQT-225 / RQT-226 has an integral norm−2 vector:

`x=(6102,-2356,261,1246,1580)`.

This satisfies the exact Gram equation **xᵀ F x = −2**. The original 22-coordinate vector is

```
[-25512867,-48988892,-41954842,-58838674,5239641,6565898,7964970,16198497,19538668,61571431,26470277,3252567,-2254848,14308122,26296581,8441205,-9085188,-23136184,-12607950,26531588,-16333007,26242375]
```

Against the original source Gram G and operator X, all 16 prior Wall constraints vanish with **correct orientation** `T16.T * H.T * b17=0`; the ambient vector is orthogonal to h and of norm−2; the associated integral reflection preserves G and fixes h. The expanded 17-root flag has rank17 and upper-unitriangular Wall form. Its final Wall column is

```
[-142631,-5061699,1970240,-27317715,408648674,-820965243,-66934190,-16194548,-44766648,15855993,-28218149,24392874,-42189644,116935428,-96366963,1113536640,1]
```

A cone-guided exact quadratic-discriminant search encountered the root at pivot **6102**, just beyond RQT-226's certified exclusion through 6000. The 6001–8000 scan was **interrupted after discovery**; do not treat the rest of that range as exhaustively checked, or 6102 as the global minimal pivot.

**PASS:** 17 integral square−2 Wall-compatible roots and original-matrix reflection certificate. **OPEN:** roots 18–21, 21-product equality, and minimal reflection length 21 versus 23.

Complete original-source verification, all prior root reports and the complete 17×17 Wall matrix are included in the RQT-227 evidence bundle linked in the conversation.

**Next: RQT-228** — saturate the rank-four kernel of the 17 Wall constraints and seek the eighteenth root.