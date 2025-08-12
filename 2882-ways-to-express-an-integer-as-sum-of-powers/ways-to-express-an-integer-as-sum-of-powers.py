class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        """
        Count the number of ways to represent n as a sum of x-th powers of unique positive integers.
        Order does not matter (i.e., combinations, not permutations).
        Uses 0/1 knapsack-style DP over the list of available powers.

        Time:  O(n * m) where m = floor(n ** (1/x))  (m ≤ 300 when n ≤ 300)
        Space: O(n)
        """
        MOD = 10**9 + 7

        # Precompute all x-th powers <= n: [1^x, 2^x, ..., k^x]
        powers = []
        i = 1
        while True:
            val = i ** x
            if val > n:
                break
            powers.append(val)
            i += 1

        # dp[s] = number of ways to form sum s using each power at most once
        # Initialize: one way to make sum 0 (use nothing)
        dp = [0] * (n + 1)
        dp[0] = 1

        # For each power (0/1 use), update sums in descending order to avoid reuse
        for p in powers:
            for s in range(n, p - 1, -1):
                dp[s] = (dp[s] + dp[s - p]) % MOD

        return dp[n] % MOD
