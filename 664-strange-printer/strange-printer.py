class Solution:
    def strangePrinter(self, s: str) -> int:
        # Remove consecutive duplicate characters
        s = ''.join(c for i, c in enumerate(s) if i == 0 or s[i] != s[i - 1])

        n = len(s)
        memo = [[0] * n for _ in range(n)]

        def dp(start: int, end: int) -> int:
            # Base case: if the range is invalid, no turns are needed
            if start > end:
                return 0
            # Return the result if it's already computed
            if memo[start][end] > 0:
                return memo[start][end]

            # Initial case: one more turn than the subproblem excluding the first character
            min_turns = dp(start + 1, end) + 1

            # Try to optimize by finding a matching character
            for k in range(start + 1, end + 1):
                if s[start] == s[k]:
                    min_turns = min(min_turns, dp(start, k - 1) + dp(k + 1, end))

            # Store the computed result
            memo[start][end] = min_turns
            return min_turns

        # Start the dynamic programming from the full string
        return dp(0, n - 1)
