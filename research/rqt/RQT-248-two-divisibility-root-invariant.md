# RQT-248 — Two-divisibility invariant for every four-root completion

**2026-11-08 | Exact full mod-four census: PASS.**

The existing 17 explicit integral norm−2 Wall roots of the RQT-241 Branch 2 prefix remain frozen. In the saturated rank-four residual Wall lattice of RQT-242, let F4 be the even integral Gram matrix and H4 the unimodular integral Wall matrix satisfying H4+H4.T=−F4.

### Theorem (prefix-specific necessary condition)

**Every possible completion by four integral norm−2 reflections must have exactly two roots of pairing divisibility 1 and exactly two roots of pairing divisibility 2.** The two divisibility-two roots must have **distinct binary parities (1,0,1,1) and (1,1,1,1)** in the frozen RQT-242 basis. Their order may vary.

For any primitive norm−2 vector x, pairing divisibility d=gcd(F4*x) divides 2. Therefore d=2 iff F4*x=0 mod2. Exhaustively enumerate all 4^4=256 residues x mod4, retain the 80 with q(x)=−2 mod8. Of these, 32 have d=2: 16 with parity (1,0,1,1), 16 with (1,1,1,1).

Enumerate all ordered four-root flags satisfying lower one-sided Wall orthogonality x_j.T H4 x_i=0 mod4 for each j>i. There are **18,432** flags. Every one has **exactly two d=2 columns, precisely one of each parity**. Each of the six possible pairs of d2 positions occurs **3,072 times**. Since an actual integral flag would reduce to one of these modular flags, this is a global necessary condition for this 17-root prefix.

**This does not prove existence of a four-root integral completion.** Exact integral root18, roots19–21, complete original 21-reflection equality and minimal word length remain OPEN.

**Reproducible certificate:** The self-contained `RQT-248-two-divisibility-invariant-evidence.zip` attached to the conversation contains `rqt248_verify.py`, exact `RQT-242-preliminary.json` Gram/Wall data, original 22×22 source Gram/operator, previously certified root17 witness and original-source replay log, precise result JSON and checksums. The executable exact enumeration independently verified all counts.

**Next RQT-249:** use the forced two-d1/two-d2 completion composition and the RQT-243 40-class sieve to choose and construct an actual integral eighteenth root.
