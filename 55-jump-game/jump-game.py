from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Initialize the goal to the last index
        goal = len(nums) - 1

        # Traverse the list from the second to last element to the first element
        for i in range(len(nums) - 2, -1, -1):
            # Check if the current position can reach the goal
            if i + nums[i] >= goal:
                # Update the goal to the current position
                goal = i

        # Check if the goal has been updated to the first index
        return goal == 0
