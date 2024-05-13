from typing import List

class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        # Make a copy of the grid
        grid_copy = grid.copy()
        
        # Get the dimensions of the grid
        m, n = len(grid_copy), len(grid_copy[0])
        
        # Toggle rows to ensure the first element of each row is 1
        for i in range(m):
            if grid_copy[i][0] == 0:
                for j in range(n):
                    grid_copy[i][j] ^= 1

        # Toggle columns to maximize the score
        for j in range(1, n):
            ones_count = sum(grid_copy[i][j] for i in range(m))
            if ones_count < m/2:
                for i in range(m):
                    grid_copy[i][j] ^= 1

        # Calculate the final score
        score = 0
        for i in range(m):
            val = 0
            for j in range(n-1, -1, -1):
                val += grid_copy[i][j] * 2**(n-1-j)
            score += val
            
        return score
