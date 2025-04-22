class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        """
        Count the number of length-n arrays where each element divides the next,
        with all values in [1..maxValue]. Return result modulo 10^9+7.
        """
        MOD: int = 10**9 + 7

        # 1. Build smallest-prime-factor (SPF) table up to maxValue
        spf: list[int] = list(range(maxValue + 1))
        limit: int = int(maxValue**0.5)
        for i in range(2, limit + 1):
            if spf[i] == i:  # i is prime
                for j in range(i * i, maxValue + 1, i):
                    if spf[j] == j:
                        spf[j] = i

        # 2. Determine maximum exponent any prime can have in [1..maxValue]
        #    (largest when the prime is 2): floor(log2(maxValue))
        max_exp: int = maxValue.bit_length() - 1

        # 3. Precompute factorials and inverse factorials up to (n-1 + max_exp)
        N: int = (n - 1) + max_exp
        fact: list[int] = [1] * (N + 1)
        for i in range(1, N + 1):
            fact[i] = fact[i - 1] * i % MOD

        invfact: list[int] = [1] * (N + 1)
        invfact[N] = pow(fact[N], MOD - 2, MOD)
        for i in range(N, 0, -1):
            invfact[i - 1] = invfact[i] * i % MOD

        # Helper: compute binomial coefficient C(a, b) in O(1)
        def comb(a: int, b: int) -> int:
            return fact[a] * invfact[b] % MOD * invfact[a - b] % MOD

        # 4. Cache C(n-1 + e, e) for e = 0..max_exp
        comb_cache: list[int] = [comb(n - 1 + e, e) for e in range(max_exp + 1)]

        # 5. Sum contributions for each possible final value v
        total: int = 0
        for v in range(1, maxValue + 1):
            ways: int = 1
            x: int = v
            # Factor v via SPF, multiply by the corresponding binomial for each exponent
            while x > 1:
                p: int = spf[x]
                cnt: int = 0
                while x % p == 0:
                    x //= p
                    cnt += 1
                ways = (ways * comb_cache[cnt]) % MOD

            total = (total + ways) % MOD

        return total
