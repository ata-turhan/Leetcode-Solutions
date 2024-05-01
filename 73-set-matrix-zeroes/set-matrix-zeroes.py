class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Modify the matrix in-place to set entire row and column to zero if any cell is zero.
        
        Args:
        - matrix: A 2D list representing the matrix.
        
        Returns:
        None (modifies the input matrix in-place).
        """
        # Flag to track if the first row needs to be zeroed out
        first_row_zero = False
        # Get the number of rows and columns in the matrix
        rows = len(matrix)
        cols = len(matrix[0])

        # Iterate through each cell in the matrix
        for i in range(rows):
            for j in range(cols):
                # If the cell value is zero, mark the corresponding row and column
                if matrix[i][j] == 0:
                    # If it's the first row, set the flag to True
                    if i == 0:
                        first_row_zero = True
                    else:
                        # Mark the first cell of the current row and column as zero
                        matrix[i][0] = 0
                    matrix[0][j] = 0

        # Iterate through the matrix again to update the entire rows and columns based on the marks
        for i in range(1, rows):
            if matrix[i][0] == 0:
                # Set the entire row to zero if the first cell of that row is marked
                matrix[i] = [0] * cols
        for j in range(cols):
            if matrix[0][j] == 0:
                # Set the entire column to zero if the first cell of that column is marked
                for k in range(rows):
                    matrix[k][j] = 0

        # If the first row was marked, set the entire first row to zero
        if first_row_zero:
            matrix[0] = [0] * cols
