from typing import List

class Solution:
    def maxSum(self, nums: List[int]) -> int:
        """
        Returns the sum of unique non-negative numbers in the list.
        If all numbers are negative, returns the maximum number.
        """
        non_negative_nums = {num for num in nums if num >= 0}

        if non_negative_nums:
            return sum(non_negative_nums)
        else:
            return max(nums)
