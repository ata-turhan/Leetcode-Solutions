class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # Iterate through each cell in the grid
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # Skip the starting cell
                if i == 0 and j == 0:
                    continue
                else:
                    # Initialize up and left to infinity
                    up, left = float("inf"), float("inf")
                    # Get the value from the cell above if it exists
                    if i - 1 >= 0:
                        up = grid[i - 1][j]
                    # Get the value from the cell to the left if it exists
                    if j - 1 >= 0:
                        left = grid[i][j - 1]
                    # Update the current cell with the minimum path sum
                    grid[i][j] += min(up, left)
        # Return the value in the bottom-right cell, which is the minimum path sum
        return grid[-1][-1]
