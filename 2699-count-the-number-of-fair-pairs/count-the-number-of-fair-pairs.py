from bisect import bisect_left, bisect_right
from typing import List

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        # Sort nums to enable binary search for valid pairs
        nums.sort()
        fair_pair_count = 0
        n = len(nums)

        # Iterate over each element to find valid pairs
        for i in range(n):
            current_num = nums[i]
            # Find the smallest index j where nums[i] + nums[j] >= lower
            start_index = bisect_left(nums, lower - current_num, i + 1)
            # Find the largest index j where nums[i] + nums[j] <= upper
            end_index = bisect_right(nums, upper - current_num, i + 1)

            # Count valid pairs in the range
            fair_pair_count += end_index - start_index

        return fair_pair_count
