class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])

        dp = [list(map(int, row)) for row in matrix]  # Initialize dp array with integer values

        max_val = 0  # Initialize the maximum value to track the largest square

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == "1":
                    val = 1

                    if i - 1 in range(rows) and j - 1 in range(cols):
                        min_val = min(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j])
                    else:
                        min_val = 0

                    dp[i][j] = val + min_val  # Update dp value based on minimum adjacent values
                    max_val = max(max_val, dp[i][j])  # Update the maximum value if a larger square is found

        return max_val * max_val  # Return the area of the largest square
