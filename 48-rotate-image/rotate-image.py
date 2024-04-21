from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Rotate the given matrix 90 degrees clockwise in place.

        Args:
            matrix: The matrix to be rotated.

        Returns:
            None. The function modifies the matrix in place.
        """
        n = len(matrix)
        # Iterate through each layer of the matrix from outer to inner layers.
        for layer in range(n // 2):
            # Iterate through each element in the current layer.
            for i in range(layer, n - 1 - layer):
                # Store the top element.
                top = matrix[layer][i]
                # Move left element to top.
                matrix[layer][i] = matrix[n - 1 - i][layer]
                # Move bottom element to left.
                matrix[n - 1 - i][layer] = matrix[n - 1 - layer][n - 1 - i]
                # Move right element to bottom.
                matrix[n - 1 - layer][n - 1 - i] = matrix[i][n - 1 - layer]
                # Move top element to right.
                matrix[i][n - 1 - layer] = top
