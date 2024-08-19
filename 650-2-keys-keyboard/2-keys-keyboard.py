class Solution:
    def minSteps(self, n: int) -> int:
        @cache
        def dp(i, copied_chars):
            if i == n:
                return 0
            if i > n:
                return float("inf")

            if copied_chars == -1:
                return 2 + dp(2, 1)
            else:
                return min(1+dp(i+copied_chars, copied_chars), 2+dp(i+i, i))

        return dp(1, -1)
        