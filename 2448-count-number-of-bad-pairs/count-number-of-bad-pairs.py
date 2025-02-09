from math import factorial

class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        diff_counts = defaultdict(int)

        for i, num in enumerate(nums):
            diff_counts[i - num] += 1

        good_pairs = 0
        for value in diff_counts.values():
            if value >= 2:
                good_pairs += value * (value - 1) / 2

        n = len(nums)

        return int(n * (n - 1) / 2 - good_pairs)

        