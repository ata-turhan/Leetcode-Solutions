from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []

        # Initialize boundaries
        rows, cols = len(matrix), len(matrix[0])
        top, bottom, left, right = 0, rows - 1, 0, cols - 1
        result = []

        while top <= bottom and left <= right:
            # Traverse from left to right along the top boundary
            for col in range(left, right + 1):
                result.append(matrix[top][col])
            top += 1  # Move the top boundary down

            # Traverse from top to bottom along the right boundary
            for row in range(top, bottom + 1):
                result.append(matrix[row][right])
            right -= 1  # Move the right boundary left

            # Check if there are still rows to process
            if top <= bottom:
                # Traverse from right to left along the bottom boundary
                for col in range(right, left - 1, -1):
                    result.append(matrix[bottom][col])
                bottom -= 1  # Move the bottom boundary up

            # Check if there are still columns to process
            if left <= right:
                # Traverse from bottom to top along the left boundary
                for row in range(bottom, top - 1, -1):
                    result.append(matrix[row][left])
                left += 1  # Move the left boundary right

        return result
