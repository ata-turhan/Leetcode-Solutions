from typing import List
from functools import cache

class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        def can_rob(cap: int) -> bool:
            """Check if we can rob at least k houses with capability <= cap"""
            count = 0
            i = 0
            while i < len(nums):
                if nums[i] <= cap:
                    count += 1
                    i += 1  # Skip the next adjacent house
                i += 1
            return count >= k

        # Binary search on the capability (max money in robbed house)
        left, right = min(nums), max(nums)
        while left < right:
            mid = (left + right) // 2
            if can_rob(mid):
                right = mid  # Try to lower the capability
            else:
                left = mid + 1  # Increase the capability

        return left  # Minimum possible capability
