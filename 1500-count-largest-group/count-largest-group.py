from typing import Dict
from collections import defaultdict

class Solution:
    def countLargestGroup(self, n: int) -> int:
        """
        Counts how many groups (based on digit sums) have the maximum size.
        Each number from 1 to n is grouped by the sum of its digits.
        """

        def digit_sum(num: int) -> int:
            return sum(int(digit) for digit in str(num))

        group_sizes: Dict[int, int] = defaultdict(int)

        # Count the size of each group based on digit sum
        for num in range(1, n + 1):
            group_sizes[digit_sum(num)] += 1

        max_group_size = max(group_sizes.values())

        # Count how many groups have the maximum size
        return sum(1 for size in group_sizes.values() if size == max_group_size)
