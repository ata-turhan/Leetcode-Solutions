from typing import List

class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        """
        Returns the maximum absolute difference between adjacent elements
        including the edge case between the first and last elements.
        """
        if not nums or len(nums) < 2:
            return 0  # No distance to measure

        max_distance: int = abs(nums[0] - nums[-1])

        for i in range(1, len(nums)):
            current_distance = abs(nums[i] - nums[i - 1])
            max_distance = max(max_distance, current_distance)

        return max_distance
