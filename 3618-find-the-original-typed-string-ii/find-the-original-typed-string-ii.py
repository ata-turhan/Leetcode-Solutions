from typing import List

class Solution:
    def possibleStringCount(self, word: str, k: int) -> int:
        MOD: int = 10**9 + 7
        # 1. Run‐length encode 'word' into g[0..R-1]
        g: List[int] = []
        n: int = len(word)
        i: int = 0
        while i < n:
            j: int = i
            while j < n and word[j] == word[i]:
                j += 1
            g.append(j - i)
            i = j
        R: int = len(g)

        # 2. Compute total assignments = ∏ g_j (each run can choose r_j in [1..g_j])
        total: int = 1
        for length in g:
            total = (total * length) % MOD

        # 3. If the minimum possible original length R ≥ k, all assignments are valid
        if R >= k:
            return total

        # 4. Otherwise, subtract assignments with total length < k
        threshold: int = k - 1
        # dp[s] = #ways to choose runs so far with sum of r_j = s
        dp: List[int] = [0] * (threshold + 1)
        dp[0] = 1  # base: zero runs → sum = 0

        for length in g:
            max_r: int = min(length, threshold)
            # Build prefix sums of previous dp
            prefix: List[int] = [0] * (threshold + 2)
            for s in range(threshold + 1):
                prefix[s + 1] = (prefix[s] + dp[s]) % MOD

            # Compute new dp for this run
            new_dp: List[int] = [0] * (threshold + 1)
            for s in range(1, threshold + 1):
                # sum dp[s - r] for r = 1..min(max_r, s)
                low: int = s - max_r
                if low < 0:
                    low = 0
                new_dp[s] = (prefix[s] - prefix[low]) % MOD

            dp = new_dp

        # 5. Sum dp[0..k-1]: assignments of length < k
        invalid: int = sum(dp) % MOD
        # Valid = total - invalid
        return (total - invalid + MOD) % MOD
