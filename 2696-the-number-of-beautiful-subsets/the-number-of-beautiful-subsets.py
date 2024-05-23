from typing import List
from collections import defaultdict

class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        total_count = 1
        freq_map = defaultdict(lambda: defaultdict(int))

        # Calculate frequencies based on remainder when divided by k
        for x in nums:
            freq_map[x % k][x] += 1

        # Calculate subsets for each remainder group
        for remainder_group in freq_map.values():
            sorted_freq_items = sorted(remainder_group.items())
            counts = [-1] * len(sorted_freq_items)  # Memoization array
            total_count *= self._count_beautiful_subsets(sorted_freq_items, k, 0, counts)

        return total_count - 1  # Subtract 1 to exclude the empty subset

    def _count_beautiful_subsets(
        self, subsets: List[List[int]], difference: int, i: int, counts: List[int]
    ) -> int:
        # Base case: If we've considered all subsets
        if i == len(subsets):
            return 1

        # If already calculated, return the stored result
        if counts[i] != -1:
            return counts[i]

        # Calculate subsets where the current subset is not included
        skip = self._count_beautiful_subsets(subsets, difference, i + 1, counts)

        # Calculate the number of subsets where the current subset is included
        take = (1 << subsets[i][1]) - 1

        # If the next number has a difference of 'difference', handle accordingly
        if i + 1 < len(subsets) and subsets[i + 1][0] - subsets[i][0] == difference:
            take *= self._count_beautiful_subsets(subsets, difference, i + 2, counts)
        else:
            take *= self._count_beautiful_subsets(subsets, difference, i + 1, counts)

        # Store the result in the memoization array
        counts[i] = skip + take
        return counts[i]

# Example usage:
# sol = Solution()
# print(sol.beautifulSubsets([1, 2, 3, 4, 5], 2))  # Example input
