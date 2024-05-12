from math import inf 

class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        dp = [[0]*cols for _ in range(rows)]
        res = -inf
        
        for i in range(rows):
            for j in range(cols):
                min_val = min(
                    dp[i-1][j] if i else inf,
                    dp[i][j-1] if j else inf
                )
                cur_score = grid[i][j] - min_val
                res = max(res, cur_score)
                dp[i][j] = min(min_val, grid[i][j])

        return res