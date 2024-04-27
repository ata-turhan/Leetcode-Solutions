from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        Determine the maximum amount of money you can rob tonight without alerting the police.

        Args:
            nums (List[int]): List of non-negative integers representing the amount of money of each house.

        Returns:
            int: The maximum amount of money that can be robbed.
        """
        # Handle edge cases
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        # Initialize the dynamic programming array
        dp = [0] * len(nums)
        
        # Initialize the first two values of the dp array
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        # Iterate through the rest of the array to fill the dp array
        for i in range(2, len(nums)):
            # Choose the maximum between robbing the current house and not robbing it
            dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])
        
        # Return the maximum amount of money that can be robbed
        return dp[-1]
