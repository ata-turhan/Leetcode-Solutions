from typing import List

class Solution:
    def countOfPairs(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        # DP table to store the number of valid pairs up to each index i and value j
        dp = [[0] * 1001 for _ in range(n)]
        
        # Initialize the first row of the DP table
        for j in range(nums[0] + 1):
            dp[0][j] = 1

        # Fill the DP table by iterating over the elements in the nums list
        for i in range(1, n):
            ways = 0
            k = 0
            for j in range(nums[i] + 1):
                # Accumulate the number of ways to form valid pairs
                if k <= min(j, j - (nums[i] - nums[i - 1])):
                    ways = (ways + dp[i - 1][k]) % MOD
                    k += 1
                dp[i][j] = ways

        # Sum up the results in the last row to get the total number of valid pairs
        res = sum(dp[n - 1][j] for j in range(1001)) % MOD

        return res
