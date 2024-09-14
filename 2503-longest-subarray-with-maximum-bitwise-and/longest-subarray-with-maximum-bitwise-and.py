from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # Find the maximum value in the array
        max_value: int = max(nums)
        longest_subarray: int = 0  # Tracks the longest subarray of max_value
        current_count: int = 0     # Tracks the current count of consecutive max_value elements
        
        # Iterate through the list and count consecutive occurrences of max_value
        for num in nums:
            if num == max_value:
                current_count += 1
                longest_subarray = max(longest_subarray, current_count)
            else:
                current_count = 0  # Reset the count when encountering a different value

        return longest_subarray
