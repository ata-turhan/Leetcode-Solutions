class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        # Handle the edge case where the matrix has only one element
        if n == 1:
            return matrix[0][0]
        
        # Iterate through the matrix starting from the second row
        for i in range(1, n):
            for j in range(n):
                left, up, right = [float('inf')] * 3
                # Check the left diagonal value if it exists
                if j - 1 >= 0:
                    left = matrix[i - 1][j - 1]
                # Check the value directly above
                up = matrix[i - 1][j]
                # Check the right diagonal value if it exists
                if j + 1 < n:
                    right = matrix[i - 1][j + 1]
                # Update the current cell with the minimum path sum
                matrix[i][j] += min(left, up, right)
        
        # Return the minimum value from the last row
        return min(matrix[-1])
