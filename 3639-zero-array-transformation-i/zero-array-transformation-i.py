from typing import List

class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        """
        Determines whether it's possible to make all elements in `nums` zero
        or less by applying a set of decrement operations over specified ranges.

        Each query [l, r] applies a decrement of 1 to all nums[l...r].
        """
        n = len(nums)
        decrements = [0] * (n + 1)  # Extra element to handle r+1 safely

        for l, r in queries:
            decrements[l] += 1
            if r + 1 < n:
                decrements[r + 1] -= 1

        # Accumulate prefix sums to compute total decrements per index
        for i in range(1, n):
            decrements[i] += decrements[i - 1]

        # Check if all elements in nums can be zeroed out
        for i in range(n):
            if decrements[i] < nums[i]:
                return False

        return True
