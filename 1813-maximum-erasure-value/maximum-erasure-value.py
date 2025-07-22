from typing import List

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        """
        Returns the maximum sum of any contiguous subarray of 'nums' with all unique elements.
        """
        # Initialize pointers and accumulators
        left = 0                  # Left boundary of our sliding window
        current_sum = 0           # Sum of elements in the current window
        max_sum = 0               # Best sum seen so far
        seen = set()              # Set to track unique elements in the window

        # Expand the window by moving 'right'
        for right, value in enumerate(nums):
            # If 'value' is already in the window, shrink from the left
            while value in seen:
                # Remove the leftmost element to restore uniqueness
                removed = nums[left]
                seen.remove(removed)
                current_sum -= removed
                left += 1

            # Add the new unique element
            seen.add(value)
            current_sum += value

            # Record the best sum encountered
            if current_sum > max_sum:
                max_sum = current_sum

        return max_sum
