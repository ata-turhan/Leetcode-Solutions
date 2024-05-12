from math import inf
from typing import List

class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        # Get the number of rows and columns in the grid
        rows = len(grid)
        cols = len(grid[0])

        # Initialize the dynamic programming table
        dp = [[0]*cols for _ in range(rows)]
        # Initialize the result variable to negative infinity
        max_score = -inf
        
        # Iterate over each cell in the grid
        for i in range(rows):
            for j in range(cols):
                # Calculate the minimum value from the top and left neighbors
                min_neighbor = min(
                    dp[i-1][j] if i else inf,
                    dp[i][j-1] if j else inf
                )
                # Calculate the current score for the cell
                current_score = grid[i][j] - min_neighbor
                # Update the maximum score if needed
                max_score = max(max_score, current_score)
                # Update the dynamic programming table with the minimum of the current value and the grid value
                dp[i][j] = min(min_neighbor, grid[i][j])

        return max_score
