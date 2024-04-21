from typing import List

class Solution:
    def solve(self, idx: int, prev: int, rows: int, cols: int, cnt: List[List[int]], dp: List[List[int]]) -> int:
        """
        Recursive function to find the minimum operations to make each column unique.

        Args:
            idx: Current column index.
            prev: Value of the previous digit used in the previous column.
            rows: Number of rows in the grid.
            cols: Number of columns in the grid.
            cnt: Matrix storing the count of each digit in each column.
            dp: Memoization table for dynamic programming.

        Returns:
            Minimum operations required to make each column unique.
        """
        if idx >= cols:
            return 0
        if dp[idx][prev] != -1:
            return dp[idx][prev]
        ans = float('inf')
        for j in range(10):
            if j != prev:
                ans = min(ans, rows - cnt[idx][j] + self.solve(idx + 1, j, rows, cols, cnt, dp))
        dp[idx][prev] = ans
        return ans

    def minimumOperations(self, grid: List[List[int]]) -> int:
        """
        Main function to calculate the minimum operations to make each column unique.

        Args:
            grid: 2D grid representing the input grid.

        Returns:
            Minimum operations required to make each column unique.
        """
        n, m = len(grid), len(grid[0])
        cnt = [[0] * 10 for _ in range(m)]
        for c in range(m):
            for r in range(n):
                cnt[c][grid[r][c]] += 1
        dp = [[-1] * 11 for _ in range(1001)]
        ans = self.solve(0, 10, n, m, cnt, dp)
        return ans
