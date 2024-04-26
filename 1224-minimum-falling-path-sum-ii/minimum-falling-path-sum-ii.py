class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        @cache
        def dfs(prev, row):
            if row == len(grid):
                return 0
            min_val = float("inf")
            for col in range(len(grid[0])):
                if col != prev:
                    min_val = min(min_val, grid[row][col] + dfs(col, row+1))
            return min_val
        return dfs(-1, 0)
        