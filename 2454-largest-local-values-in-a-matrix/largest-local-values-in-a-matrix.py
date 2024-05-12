from typing import List

class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        # Get the number of rows and columns in the grid
        rows, cols = len(grid), len(grid[0])
        # Initialize the result grid with zeros
        res = [[0]*(cols-2) for _ in range(rows-2)]
        
        # Iterate over the grid, excluding the last two rows and columns
        for i in range(rows-2):
            for j in range(cols-2):
                # Calculate the maximum value among the local neighbors
                max_val = max(
                    grid[i][j],
                    grid[i+1][j],
                    grid[i+2][j],
                    grid[i][j+1],
                    grid[i][j+2],
                    grid[i+1][j+1],
                    grid[i+2][j+2],
                    grid[i+1][j+2],
                    grid[i+2][j+1],
                )
                # Store the maximum value in the result grid
                res[i][j] = max_val

        return res
