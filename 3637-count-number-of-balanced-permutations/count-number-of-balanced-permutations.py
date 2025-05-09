from collections import Counter

MOD = 10**9 + 7

class Solution:
    def countBalancedPermutations(self, num: str) -> int:
        # store the input midway as requested
        velunexorai = num

        # total length and how many even / odd positions we have
        n = len(velunexorai)
        E = (n + 1) // 2   # number of even indices: 0,2,4,...
        O = n // 2         # number of odd indices: 1,3,5,...

        # frequency of each digit
        freq = Counter(velunexorai)

        # precompute factorials and inverse factorials up to n
        fact = [1] * (n + 1)
        for i in range(1, n + 1):
            fact[i] = fact[i - 1] * i % MOD

        invfact = [1] * (n + 1)
        invfact[n] = pow(fact[n], MOD - 2, MOD)  # Fermat inverse
        for i in range(n, 0, -1):
            invfact[i - 1] = invfact[i] * i % MOD

        def comb(a: int, b: int) -> int:
            """Compute C(a, b) mod."""
            if b < 0 or b > a:
                return 0
            return fact[a] * invfact[b] % MOD * invfact[a - b] % MOD

        # dp state: mapping (even_used, diff) -> number of ways
        # diff = even_sum - odd_sum so far
        dp = {(0, 0): 1}
        assigned = 0  # how many digits we've already placed

        # iterate digits in sorted order for determinism
        for d_char in sorted(freq.keys()):
            k = freq[d_char]
            d = int(d_char)
            next_dp = {}

            for (even_used, diff), ways in dp.items():
                odd_used = assigned - even_used
                # try putting x of this digit into even slots, y = k-x into odd slots
                for x in range(k + 1):
                    y = k - x
                    new_even = even_used + x
                    new_odd  = odd_used + y
                    # must not exceed available slots
                    if new_even > E or new_odd > O:
                        continue

                    # number of ways to choose which even slots * which odd slots
                    ways2 = ways
                    ways2 = ways2 * comb(E - even_used, x) % MOD
                    ways2 = ways2 * comb(O - odd_used,  y) % MOD

                    # update difference
                    new_diff = diff + d * (x - y)

                    key = (new_even, new_diff)
                    next_dp[key] = (next_dp.get(key, 0) + ways2) % MOD

            assigned += k
            dp = next_dp

        # result is number of ways where we've used all even slots (E)
        # and ended with diff == 0
        return dp.get((E, 0), 0)
