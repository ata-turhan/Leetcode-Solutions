from typing import List

class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        """
        Counts the number of valid starting values that keep all array elements within [lower, upper],
        given the difference array.
        """
        cumulative_sum = 0
        min_prefix_sum = 0
        max_prefix_sum = 0

        for diff in differences:
            cumulative_sum += diff
            min_prefix_sum = min(min_prefix_sum, cumulative_sum)
            max_prefix_sum = max(max_prefix_sum, cumulative_sum)

        min_start = lower - min_prefix_sum
        max_start = upper - max_prefix_sum

        if min_start > max_start:
            return 0
        
        return max_start - min_start + 1
