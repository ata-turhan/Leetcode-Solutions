from typing import List

class Solution:
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        """
        Compute the number of arrays of length n with values in [1, m]
        having exactly k adjacent equal pairs, modulo 10^9+7.
        """
        MOD: int = 10**9 + 7

        # If k is out of valid range, no arrays satisfy the condition
        if k < 0 or k > n - 1:
            return 0

        # Precompute factorials up to n-1: fact[i] = i! % MOD
        fact: List[int] = [1] * n
        for i in range(1, n):
            fact[i] = fact[i - 1] * i % MOD

        # Precompute inverse factorials via Fermat's little theorem:
        # inv_fact[i] = (i!)^{-1} % MOD
        inv_fact: List[int] = [1] * n
        inv_fact[n - 1] = pow(fact[n - 1], MOD - 2, MOD)
        for i in range(n - 1, 0, -1):
            inv_fact[i - 1] = inv_fact[i] * i % MOD

        # Compute C(n-1, k) = (n-1)! / (k! * (n-1-k)!) mod MOD
        comb_n_1_k: int = fact[n - 1] * inv_fact[k] % MOD * inv_fact[n - 1 - k] % MOD

        # For each of the (n-1-k) positions where adjacents differ,
        # there are (m-1) choices each
        choices_for_unequal: int = pow(m - 1, n - 1 - k, MOD)

        # Multiply by m choices for the first element
        result: int = m % MOD * comb_n_1_k % MOD * choices_for_unequal % MOD
        return result
