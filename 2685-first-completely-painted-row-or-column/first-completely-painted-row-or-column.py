from typing import List

class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        """
        Find the first index in `arr` where a row or column in `mat` becomes completely marked.

        :param arr: List[int] - Order in which numbers are marked.
        :param mat: List[List[int]] - The matrix with numbers to be marked.
        :return: int - The index in `arr` at which a row or column in `mat` is completely marked.
        """
        rows_count = len(mat)   # Number of rows in the matrix
        cols_count = len(mat[0])  # Number of columns in the matrix

        # Track the count of marked elements in each row and column
        marked_rows = [0] * rows_count
        marked_cols = [0] * cols_count

        # Map each number in the matrix to its (row, column) position
        num_positions = {}
        for row in range(rows_count):
            for col in range(cols_count):
                num_positions[mat[row][col]] = (row, col)

        # Process each number in `arr` to mark its position in the matrix
        for idx, num in enumerate(arr):
            row, col = num_positions[num]  # Get the row and column of the current number
            marked_rows[row] += 1
            marked_cols[col] += 1

            # Check if the current row or column is completely marked
            if marked_rows[row] == cols_count or marked_cols[col] == rows_count:
                return idx  # Return the index at which the row or column is fully marked

        return -1  # Return -1 if no row or column becomes fully marked
