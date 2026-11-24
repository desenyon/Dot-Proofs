# Stage 2: Collatz parity classes and Erdős–Straus prime reduction

## 1. Collatz: exact parity-prefix classes

Use the shortcut T(x)=x/2 for even x and (3x+1)/2 for odd x; the odd branch is two ordinary steps and the even branch one. Forward reaching 1 under T implies reaching 1 under the original map. Conversely a skipped original intermediate is 3x+1≥4, so it cannot be the first 1. The boundary starting value 1 is immediate.

For every length-k parity word there is exactly one residue modulo 2^k realizing it. For k=0 the claim is immediate. Inductively, along a fixed prefix with s odd steps, let T^k(x)=(3^s x+b)/2^k. Appending an even step keeps b; appending an odd step sends b to 3b+2^k. For two representatives a and a+2^k, their final values differ by the odd integer 3^s. Consequently the two lifts of the residue modulo 2^(k+1) realize opposite next parities. Replacing a by a positive representative, if needed, changes the final value by an even multiple of 3^s at depth k+1 congruence scale before the appended step, so does not change that next parity.

If 3^s<2^k, this prefix yields strict descent exactly when (2^k−3^s)x>b. This is a computable sufficient certificate for an infinite tail in a residue class, rather than a universal bound on stopping time. If 3^s≥2^k, b≥0 blocks this certificate at that prefix. A finite union of certified prefixes still cannot cover every positive integer, by the arbitrarily long rising family in stage 1. Next investigate structural restrictions on positive integers surviving nested uncertified prefix sets, rather than trying longer finite covers as a universal proof. This is classical parity/stopping-time machinery, not claimed novel. See [Tao's survey references](https://doi.org/10.1017/fmp.2022.8).

## 2. Erdős–Straus: explicit scaling and residue gates

If m≥2 divides n, write n=dm. From 4/m=1/x+1/y+1/z, dividing by d gives 4/n with denominators dx,dy,dz. Thus the all-n statement is equivalent to its prime restriction, and a least counterexample is prime. For even n use denominators (n/2,n,n). For 3|n use (n/3,2n,2n). For n≡2 mod 3 write x=(n+1)/3 and use (x,n,nx), since n+1=3x. For n≡3 mod 4 take x=(n+1)/4 and use (x,2nx,2nx), since n+1=4x. Each identity follows by clearing positive denominators. A possible counterexample prime must therefore be 1 modulo 12. This is a necessary filter, not a conjecture predicting that every such prime is hard. Next reconstruct the exact exceptional classes and applicability of [Salez's sieve](https://arxiv.org/abs/1406.6307) before changing modular hypotheses. No new numerical verification frontier is claimed.

The finite script replays parity arithmetic and denominator identities. No successful Lean run, fair exact-certificate checker, or verified settlement is claimed by this checkpoint.
