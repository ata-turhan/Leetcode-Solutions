from typing import List

class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        """
        Idea:
        - powers = sorted powers of two that sum to n → one for each set bit in n's binary form.
          Example: n=15(1111b) → exponents [0,1,2,3] → powers [1,2,4,8].
        - For any range [l,r], product(powers[l..r]) = 2^(sum(exponents[l..r])) mod MOD.
        - Precompute prefix sums of exponents for O(1) range-sum; answer each query with pow(2, exp, MOD).

        Complexity:
        - Build exponents: O(#bits) ≤ 30.
        - Each query: O(log MOD) for modular exponentiation; total O(q log MOD).
        """
        MOD = 10**9 + 7

        # Collect exponents (bit positions) of set bits, in ascending order.
        exps = []
        i, m = 0, n
        while m:
            if m & 1:
                exps.append(i)
            i += 1
            m >>= 1

        # Prefix sums of exponents for fast range sums.
        pref = [0]
        for e in exps:
            pref.append(pref[-1] + e)

        # Answer queries: product = 2^(sum of exponents in range) mod MOD.
        ans = []
        for L, R in queries:
            exp_sum = pref[R + 1] - pref[L]
            ans.append(pow(2, exp_sum, MOD))
        return ans
