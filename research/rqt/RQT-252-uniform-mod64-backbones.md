# RQT-252 — All 36 binary Wall backbones admit four-column lifts modulo 64

**2026-11-08 | Exact original-source replay + independent arithmetic audit PASS.**

The RQT-241 Branch 2 prefix contains 17 certified *integral* norm−2 Wall roots. The RQT-242 rank-four residual lattice has an even Gram F4, a unimodular Wall H4 satisfying H4+H4.T=−F4, and an **index-two residual image** inside the saturated rank-four Wall kernel.

**Constructive modular theorem.** Every one of the 36 ordered four-root flags modulo 2 (RQT-250) has an **explicit four-column lift modulo 64**. For each 4×4 integer witness V:
- each column has norm **−2 mod 128**, i.e. (V.T F4 V)[i,i]≡−2 (mod128);
- all six lower Wall pairings (V.T H4 V)[j,i]≡0 (mod64) for j>i;
- all four diagonal Wall pairings ≡1 (mod64);
- det(V) is odd;
- reduction modulo2 exactly equals its claimed binary backbone.

An exact independent verifier reconstructed the set of all 36 binary flags and checked the complete family of 36 witnesses; all passed. **This is a constructive coverage theorem, NOT an exhaustive enumeration of every possible mod64 flag.**

A displayed example, with roots as *columns*:
```
[40 25 11  9]
[43 22  6 11]
[ 5  8 57 35]
[37 57 19 45]
```
This particular witness represents the backbone with columns (0,1,1,1), (1,0,0,1), (1,0,1,1), (1,1,1,1).

The seeded constructive search used seed 252032 and **18,789** sampled lift paths in total; the most difficult backbone took **1,874** trials. Per-flag congruences were verified exactly, not probabilistically.

**Partial higher exploration:** 35 of 36 backbones had a modulus-128 witness found before the execution budget expired. The last backbone is *undetermined*, not obstructed. The fully certified uniform result stops at modulus64.

A standalone evidence ZIP in this conversation, `RQT-252-all-36-binary-backbones-mod64-evidence.zip`, contains all 36 exact matrices in `RQT-252-mod64-report.json`, deterministic construction `rqt252_construct_mod64.py`, independent verifier `rqt252_verify_mod64.py`, original 22D replay `rqt242_verify.py`, previous root data, exact Gram/Wall matrices, replay logs, SHA256 manifest.

**OPEN:** actual integral root18, roots19–21, complete 21-reflection equality, and minimal reflection length. Finite 2-adic compatibility must never be conflated with an ordinary integer root.

**Next RQT-253:** explicitly construct an integral isotropic vector in the rank-four lattice and its norm−2 root, then test the successor's rank-three residual and modular continuation.
