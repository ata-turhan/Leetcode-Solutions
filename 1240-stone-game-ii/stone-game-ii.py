class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        @cache
        def dp(i, m, is_alice):
            if i >= len(piles):
                return 0

            if is_alice:
                res = 0
            else:
                res = float("inf")
            for x in range(1, 2*m+1):
                if is_alice:
                    res = max(res, sum(piles[i:i+x]) + dp(i+x, max(x, m), False))
                else:
                    res = min(res,  dp(i+x, max(x, m), True))

            return res

        return dp(0, 1, True)        