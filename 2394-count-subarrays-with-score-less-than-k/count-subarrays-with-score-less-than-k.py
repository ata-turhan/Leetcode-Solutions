from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        """
        Counts the number of subarrays where the sum of elements 
        multiplied by the length of the subarray is less than k.
        """
        left = 0
        subarray_count = 0
        current_sum = 0

        for right in range(len(nums)):
            current_sum += nums[right]

            # Shrink the window if the current window is invalid
            while left <= right and current_sum * (right - left + 1) >= k:
                current_sum -= nums[left]
                left += 1

            # After shrinking, all subarrays ending at `right` and starting from [left, right] are valid
            subarray_count += (right - left + 1)

        return subarray_count
