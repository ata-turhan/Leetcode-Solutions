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
        # Base case: if the current column index exceeds the total number of columns,
        # return 0 as no more operations are needed.
        if idx >= cols:
            return 0
        # If the result for the current state is already calculated, return it from the memoization table.
        if dp[idx][prev] != -1:
            return dp[idx][prev]
        # Initialize the answer as positive infinity.
        ans = float('inf')
        # Iterate through each possible digit (0 to 9).
        for j in range(10):
            # If the current digit is different from the previous one, proceed.
            if j != prev:
                # Calculate the minimum operations recursively for the next column
                # and update the answer accordingly.
                ans = min(ans, rows - cnt[idx][j] + self.solve(idx + 1, j, rows, cols, cnt, dp))
        # Memoize the result for the current state.
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
        # Matrix to store the count of each digit in each column
        cnt = [[0] * 10 for _ in range(m)]
        for c in range(m):
            for r in range(n):
                cnt[c][grid[r][c]] += 1
        # Memoization table for dynamic programming
        dp = [[-1] * 11 for _ in range(m+1)]
        # Find the minimum operations starting from column index 0 and previous digit as 10 (invalid).
        ans = self.solve(0, 10, n, m, cnt, dp)
        return ans
