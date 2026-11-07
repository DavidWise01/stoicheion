# RQT-221 — Two complete 2-adic divisibility-two root branches

**2026-11-07. Exact original-source verification: PASS (local only).**

The saturated rank-six Wall kernel of the fifteen-root RQT-215 flag has exact even integral Gram F. RQT-220 identified exactly two discriminant order-two classes eligible for an integral square−2 root with pairing divisibility two. Here **both classes admit actual norm−2 vectors over the 2-adic integers Z₂**.

For a binary representative a, use r(t)=a+2t e_j. Then q(r(t))+2=8(c+b t+d t²), where q(r)=rᵀFr.

**Branch A:** a=(0,0,1,1,0,1); j=3 (zero-based); (c,b,d)=(-337450,53779,-142338). The exact solution has t≡6499668843087076870 (mod 2^64).

**Branch B:** a=(1,1,0,1,0,0); j=1; (c,b,d)=(-102145,-90741,-111758). The exact solution has t≡3886618388119862109 (mod 2^64).

In both branches b is odd and d even, so derivative b+2dt is odd and Hensel's lemma yields a **unique compatible infinite 2-adic lift**. The exact 64-bit witnesses satisfy q(r)+2≡0 mod 2^67. Both remain in their distinct eligible binary classes. All pairings Fr are even, with at least one exactly 2 mod4; hence local pairing divisibility is 2. The same original ambient Gram congruences hold under the exact basis map K B Z, and h-orthogonality is exact.

**PROVED:** both admissible d=2 classes are truly 2-adically representable, beyond mere finite low-modulus compatibility. **OPEN:** existence of an ordinary integral norm−2 vector in the rank-six kernel; sixteenth integral Wall root; full 21-reflection product and minimum word length. These local roots are not global integral root certificates.

Reproduce with `rqt221_two_adic_branch_lift.py` in the independent evidence ZIP, containing original X/G, RQT-198 index-64 basis and RQT-216 reduced basis/Gram.

**RQT-222 target:** a genuinely global integer norm−2 representation, or a rigorous arithmetic obstruction.
