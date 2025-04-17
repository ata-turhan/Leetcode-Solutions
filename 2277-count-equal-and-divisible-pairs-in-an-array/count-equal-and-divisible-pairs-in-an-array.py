from typing import List

class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        """
        Counts the number of pairs (i, j) where:
        - nums[i] == nums[j]
        - i < j
        - (i * j) % k == 0
        """
        pair_count = 0
        n = len(nums)

        for i in range(n - 1):
            for j in range(i + 1, n):
                if nums[i] == nums[j] and (i * j) % k == 0:
                    pair_count += 1

        return pair_count
