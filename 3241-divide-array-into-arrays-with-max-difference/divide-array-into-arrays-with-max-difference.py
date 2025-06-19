from typing import List

class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        """
        Divides the input array into groups of 3 such that
        the difference between the max and min in each group is <= k.
        Returns an empty list if it's not possible.
        """
        if len(nums) % 3 != 0:
            return []

        nums.sort()
        grouped_subarrays: List[List[int]] = []

        for i in range(0, len(nums), 3):
            group = nums[i:i+3]
            if group[2] - group[0] > k:
                return []
            grouped_subarrays.append(group)

        return grouped_subarrays
