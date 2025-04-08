from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        """
        Determines if the array can be partitioned into two subsets with equal sums.
        Uses top-down DP with memoization.
        """

        total_sum = sum(nums)
        if total_sum % 2 != 0:
            return False  # Cannot partition an odd total sum

        target = total_sum // 2
        n = len(nums)
        memo = [[-1 for _ in range(target + 1)] for _ in range(n)]

        def can_partition(index: int, remaining: int) -> bool:
            if remaining == 0:
                return True
            if index == 0:
                return nums[0] == remaining
            if memo[index][remaining] != -1:
                return memo[index][remaining]

            not_take = can_partition(index - 1, remaining)
            take = False
            if nums[index] <= remaining:
                take = can_partition(index - 1, remaining - nums[index])

            memo[index][remaining] = take or not_take
            return memo[index][remaining]

        return can_partition(n - 1, target)
