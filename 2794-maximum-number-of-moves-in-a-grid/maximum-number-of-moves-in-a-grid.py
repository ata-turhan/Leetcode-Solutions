from typing import List

class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        # Initialize moves array with -1, and set the first column to 0
        moves = [[-1] * cols for _ in range(rows)]
        for i in range(rows):
            moves[i][0] = 0
        
        # Traverse each column to calculate the max moves for each cell
        for j in range(cols):
            for i in range(rows):
                max_previous_move = -1  # Store the maximum moves achievable from previous cells

                # Check the cell to the left, if it exists and has a lower value
                if j - 1 >= 0 and grid[i][j - 1] < grid[i][j]:
                    max_previous_move = max(max_previous_move, moves[i][j - 1])
                
                # Check the top-left diagonal cell, if within bounds and has a lower value
                if i - 1 >= 0 and j - 1 >= 0 and grid[i - 1][j - 1] < grid[i][j]:
                    max_previous_move = max(max_previous_move, moves[i - 1][j - 1])

                # Check the bottom-left diagonal cell, if within bounds and has a lower value
                if i + 1 < rows and j - 1 >= 0 and grid[i + 1][j - 1] < grid[i][j]:
                    max_previous_move = max(max_previous_move, moves[i + 1][j - 1])

                # Update moves array if there is a valid move
                if max_previous_move != -1:
                    moves[i][j] = max_previous_move + 1

        # Return the maximum value from the moves array
        return max(max(row) for row in moves)
