from typing import List

class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        """Finds the maximum count of either negative or positive numbers using binary search."""
        
        def find_first_non_negative() -> int:
            """Finds the index of the first non-negative number using binary search."""
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] < 0:
                    left = mid + 1
                else:
                    right = mid - 1
            return left  # First non-negative index

        def find_first_positive() -> int:
            """Finds the index of the first positive number using binary search."""
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] <= 0:
                    left = mid + 1
                else:
                    right = mid - 1
            return left  # First positive index

        negative_count = find_first_non_negative()
        positive_count = len(nums) - find_first_positive()

        return max(negative_count, positive_count)
