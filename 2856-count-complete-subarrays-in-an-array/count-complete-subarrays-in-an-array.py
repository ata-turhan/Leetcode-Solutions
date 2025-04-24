from typing import List
from collections import defaultdict

class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        """
        Counts the number of complete subarrays.
        A subarray is complete if it contains all distinct elements in the original array.
        """
        total_distinct = len(set(nums))
        left = 0
        subarray_count = 0
        frequency_map = defaultdict(int)

        for right in range(len(nums)):
            frequency_map[nums[right]] += 1

            while len(frequency_map) == total_distinct:
                subarray_count += len(nums) - right
                frequency_map[nums[left]] -= 1
                if frequency_map[nums[left]] == 0:
                    del frequency_map[nums[left]]
                left += 1

        return subarray_count
