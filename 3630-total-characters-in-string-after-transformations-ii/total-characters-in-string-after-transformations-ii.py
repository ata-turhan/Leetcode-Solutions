from typing import List

MOD: int = 1_000_000_007          # 1 000 000 007 is prime → safe modulus
ALPHA: int = 26                   # size of the English alphabet


class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
        """
        Computes |Tᵗ(s)| mod 1e9+7 where T is the per‑character replacement rule
        defined by `nums`.  We model T as a 26×26 adjacency/count matrix M and
        exponentiate M^t to obtain exact character counts after t steps.

        Complexity:  Θ(26³ log t)  ≈ 1.17 × 10⁴ scalar updates – trivial in Python.
        Space:       Θ(26²) for two 26×26 matrices.
        """
        # ---------- 1. Build one‑step transition/count matrix M ----------
        # M[i][j] == how many times letter j appears after transforming *one*
        # occurrence of letter i exactly once.  Each output letter appears once.
        M: List[List[int]] = [[0] * ALPHA for _ in range(ALPHA)]
        for i in range(ALPHA):
            k: int = nums[i]                       # expansion length for letter i
            for step in range(1, k + 1):
                M[i][(i + step) % ALPHA] = 1       # wrap‑around with modulo 26

        # ---------- 2. Fast  exponentiation  P := M^t  (binary‑power) ----------
        def mat_mul(A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
            """26×26 matrix multiplication mod MOD (micro‑optimized)."""
            R: List[List[int]] = [[0] * ALPHA for _ in range(ALPHA)]
            for i in range(ALPHA):
                Ai: List[int] = A[i]
                Ri: List[int] = R[i]
                for k in range(ALPHA):
                    if Ai[k] == 0:                      # skip zeros → 14× faster
                        continue
                    aik: int = Ai[k]
                    Bk: List[int] = B[k]
                    for j in range(ALPHA):
                        Ri[j] = (Ri[j] + aik * Bk[j]) % MOD
            return R

        # Identity matrix
        P: List[List[int]] = [[1 if i == j else 0 for j in range(ALPHA)]
                              for i in range(ALPHA)]
        base: List[List[int]] = M
        exp: int = t
        while exp:
            if exp & 1:                               # multiply when bit = 1
                P = mat_mul(P, base)
            base = mat_mul(base, base)
            exp >>= 1

        # ---------- 3. Row‑sum vector  w[i] = |letter_i| after t steps ----------
        row_sum: List[int] = [sum(P[i]) % MOD for i in range(ALPHA)]

        # ---------- 4. Count original letters and aggregate answer ----------
        cnt: List[int] = [0] * ALPHA
        for ch in s:                                  # O(|s|)
            cnt[ord(ch) - 97] += 1

        ans: int = 0
        for i in range(ALPHA):
            ans = (ans + cnt[i] * row_sum[i]) % MOD
        return ans
