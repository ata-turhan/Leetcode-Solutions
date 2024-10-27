from typing import List

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        total_squares = 0  # Initialize to track the total count of square submatrices

        # Iterate through each cell in the matrix
        for i in range(rows):
            for j in range(cols):
                # Track adjacent squares to the left, above, and top-left diagonal
                left_square, top_square, diagonal_square = 0, 0, 0
                
                # Retrieve values of adjacent squares if within bounds
                if j > 0:
                    left_square = matrix[i][j - 1]
                if i > 0:
                    top_square = matrix[i - 1][j]
                if i > 0 and j > 0:
                    diagonal_square = matrix[i - 1][j - 1]

                # Update the current cell if it can form a square (if cell value is 1)
                if matrix[i][j] == 1:
                    matrix[i][j] = min(left_square, top_square, diagonal_square) + 1

                # Add the square size at this cell to the total count
                total_squares += matrix[i][j]

        return total_squares
