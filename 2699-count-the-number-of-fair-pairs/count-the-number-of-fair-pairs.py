from bisect import bisect_left, bisect_right
from typing import List

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        num_pairs = 0
        n = len(nums)

        for i in range(n):
            num = nums[i]
            left = bisect_left(nums, lower - num, i + 1)
            right = bisect_right(nums, upper - num, i + 1)
            num_pairs += right - left

        return num_pairs
