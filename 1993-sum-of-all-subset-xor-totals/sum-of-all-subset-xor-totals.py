from typing import List

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        n = len(nums)
        total_sum = 0

        # Iterate over all possible subsets
        for subset in range(1 << n):  # 1 << n is 2^n, representing all subsets
            subset_xor = 0
            for i in range(n):
                # Check if the i-th element is in the current subset
                if subset & (1 << i):
                    subset_xor ^= nums[i]
            total_sum += subset_xor

        return total_sum
