from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        Calculates the minimum number of jumps required to reach the last index in the given list of non-negative integers.

        Args:
        - nums: List of non-negative integers representing the maximum jump length at each position

        Returns:
        - Minimum number of jumps required
        """
        # Initialize the left and right boundaries of the current jump
        l, r = 0, 0
        # Initialize the result variable to store the minimum number of jumps
        res = 0
        
        # Continue jumping until the right boundary reaches the last index
        while r < (len(nums) - 1):
            maxJump = 0  # Initialize the maximum reachable position in the current jump
            # Iterate through the positions within the current jump boundaries
            for i in range(l, r + 1):
                maxJump = max(maxJump, i + nums[i])  # Update the maximum reachable position
            l = r + 1  # Update the left boundary for the next jump
            r = maxJump  # Update the right boundary for the next jump
            res += 1  # Increment the number of jumps
        return res  # Return the minimum number of jumps required
