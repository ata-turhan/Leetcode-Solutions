from typing import List

class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        """
        Finds the maximum difference (nums[j] - nums[i]) such that j > i and nums[j] > nums[i].
        If no such pair exists, returns -1.
        """
        max_diff: int = -1
        max_from_right: int = nums[-1]

        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < max_from_right:
                max_diff = max(max_diff, max_from_right - nums[i])
            max_from_right = max(max_from_right, nums[i])

        return max_diff
