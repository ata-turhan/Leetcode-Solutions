from typing import List

class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        """
        Constructs a new array such that result[i] = nums[nums[i]] for each index i.
        """
        n = len(nums)
        result = [0] * n

        for i in range(n):
            result[i] = nums[nums[i]]

        return result
