from typing import List

class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        """
        Counts the number of subarrays of length 3 where
        nums[i+1] is the half of sum of nums[i] and nums[i+2].
        """
        subarray_count = 0
        n = len(nums)

        for i in range(n - 2):
            if nums[i] + nums[i + 2] == nums[i + 1] / 2:
                subarray_count += 1

        return subarray_count
