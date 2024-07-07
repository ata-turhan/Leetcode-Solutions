class Solution:
    def maximumLength(self, nums, k):
        # Initialize the DP table with zeros
        dp = [[0] * k for _ in range(k)]
        max_length = 0

        # Process each number in the input list
        for num in nums:
            # Calculate the remainder of the current number when divided by k
            remainder = num % k
            # Update the DP table
            for j in range(k):
                dp[remainder][j] = max(dp[remainder][j], dp[j][remainder] + 1)
                # Update the maximum length found so far
                max_length = max(max_length, dp[remainder][j])

        return max_length
