from typing import List

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        ROWS, COLS = len(points), len(points[0])

        # Initialize the dp array with the first row's points
        dp = points[0][:]

        # Iterate through each row starting from the second one
        for r in range(1, ROWS):
            # Arrays to store the maximum points when moving from left to right and right to left
            left_max = [0] * COLS
            right_max = [0] * COLS
            
            # Compute left_max: max points when coming from the left
            left_max[0] = dp[0]
            for c in range(1, COLS):
                left_max[c] = max(left_max[c - 1] - 1, dp[c])
            
            # Compute right_max: max points when coming from the right
            right_max[COLS - 1] = dp[COLS - 1]
            for c in range(COLS - 2, -1, -1):
                right_max[c] = max(right_max[c + 1] - 1, dp[c])
            
            # Update dp for the current row
            for c in range(COLS):
                dp[c] = points[r][c] + max(left_max[c], right_max[c])

        # The result is the maximum value in the last row of dp
        return max(dp)
