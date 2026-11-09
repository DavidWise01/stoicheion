# RQT-249 — Full four-column binary lift to 2^256

**2026-11-08 | Exact independent finite-modulus certificate PASS.**

Preserve seventeen integral roots of the RQT-241 Branch-2 prefix. In the RQT-242 saturated rank-four kernel, Gram F4 and unimodular one-sided Wall H4 are fixed exact integer matrices with `H4+H4.T=-F4`. The image of the post-root residual is index two in this kernel; never conflate the image with its saturation.

## New actual construction

A particular RQT-243 modular flag did not lift beyond its prior precision. That **does not imply** an obstruction for other lifts. Starting from the same four columns **modulo eight**, we implemented deterministic randomized affine GF(2) choices with backtracking on failed subsequent lifts. The seeded program reached **modulus 2^256** with **1969 trial choices**. A second deterministic replay reproduced the identical 4×4 large-integer certificate.

The complete four-column matrix is in the attached evidence bundle as `flag256.json`. Independent exact arithmetic establishes:

- `det(V)` is **odd**.
- `diag(V.T F4 V) ≡ (-2,-2,-2,-2) (mod 2^257)`.
- `(V.T H4 V)[j,i] ≡ 0 (mod 2^256)` for all `j>i`.
- `(V.T H4 V)[i,i] ≡ 1 (mod 2^256)`.
- The two d=2 columns are positions **2 and 3** (one based), with distinct parities **(1,0,1,1)** and **(1,1,1,1)**, exactly as required by RQT-248. Remaining columns are d=1.

The 16 binary lift variables per step are constrained by four norm and six lower Wall equations. Gradients of d=2 roots vanish modulo 2, so a fixed lift choice need not continue. Backtracking explores alternative solutions and is essential. This is a high-precision **finite** 2-adic certificate; no claim of an infinite 2-adic lift is made.

The downloadable evidence ZIP includes the exact `lift.py` generator, `verify.py`, full `flag256.json` witness, frozen RQT-242 form, RQT-241 witness, source matrix files, prior source audit, both replay logs, report JSON and SHA256 file manifest.

**PASS:** full four-column Wall flag mod2^256; all four norms mod2^257; determinant unit; forced d2 parity composition; reproducibility.
**OPEN:** exact integral root18, roots19–21, full exact 21-reflection product, and minimality.

**Next RQT-250:** turn the local rank-four flag into an integral norm−2 root by constructive rational-isotropic arithmetic, or prove a stable 2-adic lifting mechanism beyond the finite certificate.
