# RQT-236 — Branch 2 first-root modular gate and exact cone exclusion

**2026-11-08 — Original-matrix exact replay PASS**

Continue fifteen certified roots plus the alternative RQT-224 sixteenth root (Branch 2):
`(-232,-246,223,729,-473,-242)` in the RQT-216 saturated rank-six coordinates. Branch 2's saturated remaining Wall lattice has rank five, with exact Gram `F5` and Wall form `H5`, frozen in the self-contained evidence bundle.

## Exhaustive first-root modular gate

Enumerate all `4^5=1024` reduced vectors modulo four. Exactly **272** have squared norm `−2 (mod 8)`. For each first-root residue `a`, use a memoized bitset dynamic program to test whether it can head a full length-five sequence where every vector has norm `−2 (mod 8)` and `b_j^T H5 b_i ≡0 (mod 4)` whenever `j>i`.

Results:
- **152** first-root classes can begin a complete length-five flag modulo four.
- **120** are obstructed from beginning such a flag modulo four.
- The complete 152-class whitelist and 120-class blacklist are archived in `first_root_screen.json`.

These conditions are **necessary only**, not actual integral reflections.

## Exact global sign invariant

Let `t=x[0]`, `z=x[1:5]`, `P=−F5[1:5,1:5]`, `v=P^−1 F5[1:5,0]`, and `beta=F5[0,0]+F5[0,1:5]v`. Exact Schur identity:

`x^T F5 x=beta*t²−(z−vt)^T P (z−vt)`.

`P` is positive definite, `beta>0`, and exact rational inequalities establish `v[i]^2>(beta+2)*(P^−1)[i,i]` for all four transverse coordinates. `v≈(0.1184355594,−0.4373922970,−0.0629250436,−0.4511966574)`. Every integral norm−2 root must therefore have sign pattern **(+,+,−,−,−)** or its simultaneous negative. `t=0` cannot represent −2.

## Exact bounded search

For **every integer t from 1 through 10000**, exact rational cone inequalities give outward-rounded integer ranges of `x[1],x[2],x[3]`. Enumerate every triple and solve for final `x[4]` with an **unbounded exact signed-128-bit quadratic discriminant and divisibility test**.

Completed search log:
```
TOTAL 764141080 FOUND 0
```
Negative t is covered by sign reversal. Hence any future integral root in this frozen basis must have **|x[0]|≥10001**. This is a finite exclusion, NOT a global nonrepresentation theorem.

Original 22×22 Gram/operator, earlier certificates, exact modular whitelist, bound generator, complete bounds, C++ search source and result log, and exact original-source verifier are all inside the downloadable RQT-236 evidence ZIP.

**STATUS:** PASS; Branch 2 roots 1–16 certified. Root 17 OPEN. Roots 18–21 OPEN. Complete 21-reflection identity OPEN.

**NEXT RQT-237:** search the 152 viable first-root classes using arithmetic/cone methods instead of expanding the raw coefficient cube.
