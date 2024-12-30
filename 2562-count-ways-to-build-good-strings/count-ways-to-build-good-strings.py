class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        @cache
        def dp(i):
            ways = 0
            if i > high:
                return ways
            elif low <= i <= high:
                ways += 1

            ways += dp(i + zero)
            ways += dp(i + one)

            return ways % (10**9 + 7)
            

        return dp(0)