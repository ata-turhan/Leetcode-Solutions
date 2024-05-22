class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Initialize a 2D dp array with all elements set to 0
        dp = [[0] * n for _ in range(m)]
        
        # The starting point
        dp[0][0] = 1
        
        # Iterate over each cell in the grid
        for i in range(m):
            for j in range(n):
                # If there is a cell above the current cell, add its path count
                if (i - 1) >= 0:
                    dp[i][j] += dp[i - 1][j]
                # If there is a cell to the left of the current cell, add its path count
                if (j - 1) >= 0:
                    dp[i][j] += dp[i][j - 1]
        
        # The number of unique paths to reach the bottom-right corner
        return dp[m - 1][n - 1]
