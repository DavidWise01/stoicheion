# RQT-245 — 3-adic Wall flags: exhaustive local-lifting theorem

**2026-11-08 | Exact original 22×22 replay PASS.**

Preserve the 17 integral norm−2 Wall roots of the RQT-241 Branch-2 prefix. In the saturated rank-four RQT-242 residual lattice, F4 is even integral and H4 is unimodular with H4+H4^T=−F4. This targets the odd prime **3** (which divides det F4 with valuation two).

**Mod-3 exhaustive census** (all 3^4=81 residues): 36 individual root residues obey r^T H4 r=1 (equiv r^T F4 r=−2 modulo3). Exactly 30 can start a complete ordered unimodular four-root Wall flag. Six cannot: (0,1,2,0), (0,2,1,0), (1,0,2,0), (1,2,1,0), (2,0,1,0), (2,1,2,0).

There are **3,888 complete ordered flags** modulo3. For each flag, the 10 equations (four diagonals r_i^T H4 r_i=1 and six lower Wall products r_j^T H4 r_i=0 for j>i) linearize under r_i→r_i+3^k e_i into a **10×16 GF(3) Jacobian of full rank 10**. The census confirms rank 10 for **all 3,888** flags. Because each Jacobian depends only on residues modulo 3, every such flag lifts inductively to a full ordered flag over Z_3, indefinitely. This is a general local theorem, not a global integral solution.

**Constructed exact local certificate:** One of the 3,888 flags is deterministically lifted through modulus 3^33 = 5559060566555523. The columns, shown as rows, are:

```
[4409335503088713, 297261264186375, 3136035136198522, 4401753864650904]
[4796289249477399, 3901172202755587, 2745616122359572, 2]
[4543534576420870, 5219082228223141, 1, 0]
[2276088881148973, 1, 2, 2]
```

Exact integer arithmetic checks each root norm −2 mod 3^33, all ten Wall-triangular congruences, and determinant 1 mod3. Its first lift, modulo9, is the four columns (0,6,4,3), (0,1,4,2), (4,7,1,0), (1,1,2,2).

**Reproducible 32-file evidence ZIP in conversation:** original Gram/operator, full RQT-241 original-source replay, RQT-242 Gram/Wall/kernel, exhaustive verifier and ternary Hensel solver `rqt245_3adic.py`, explicit `RQT-245-report.json`, and SHA256 sums.

**LIMITATION:** Odd-prime local solvability does not construct integral root18. The 40 compatible classes modulo4 from RQT-243, global sign cone from RQT-244, and exclusion |x0|≤10000 all persist. OPEN: actual integral roots18–21, exact 21-reflection identity, minimum length.

**Next RQT-246:** globally solve the rank-four integer norm−2 problem, e.g. using an exact lattice genus/spinor-genus obstruction or a constructive integer solver.