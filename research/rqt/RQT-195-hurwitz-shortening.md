# RQT-195 — Exact 25-to-23 root-reflection word shortening

**2026-11-06 | Exact original RQT-122/133 sources.**

A deterministic Hurwitz search found a pair of adjacent equal-root reflections in the certified 25-root word of RQT-193. The successful trial accepted **308 Hurwitz moves**; cancellation removed the adjacent pair and yielded an integral square-(−2) reflection word of **length 23**. All roots still lie in K=h^⊥.

The exact full 22×22 matrix product of the resulting 23 reflections equals the original X (484 entries). Each of the 23 roots was checked to be integral, square −2, and orthogonal to h.

## Invariant length bound

rank(X−I)=21 and det(X)=−1, so any root-reflection word must have odd length ≥21. The new 23-word leaves only **21 or 23** as possible minimal lengths.

## Search limits

The successful cancellation occurred at restart 28, step 344 of a fixed-seed bounded random Hurwitz walk, with 308 accepted moves in that successful run. A subsequent bounded search from the 23-word accepted 493,356 Hurwitz moves without another cancellation. This is **not** a proof that length 21 is unattainable. No global minimality claim is made.

## Reproduction

The companion script `rqt195_hurwitz_shortening.py` regenerates the 25-root baseline from RQT-193's published vector certificate, executes the fixed-seed Hurwitz search, cancels the adjacent duplicate, checks root norms and h-orthogonality, then multiplies the 23-root word exactly to verify equality with the original X. It outputs the full root and move trace.

The complete independently replayed evidence bundle, including all 308 successful moves and the final 23 integral root vectors, is supplied as a downloadable archive with this research turn.

## RQT-196

Find a 21-root certificate, or derive an arithmetic obstruction implying the root-reflection length is 23. A failed bounded search is not an impossibility proof.
