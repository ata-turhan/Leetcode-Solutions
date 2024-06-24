from sortedcontainers import SortedList

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        left = 0
        max_length = 0
        window = SortedList()
        
        for right in range(len(nums)):
            window.add(nums[right])
            current_diff = window[-1] - window[0]
            
            # Shrink the window from the left until the difference is within the limit
            while left < right and current_diff > limit:
                window.remove(nums[left])
                left += 1
                current_diff = window[-1] - window[0]
            
            # Update the maximum length of the subarray
            max_length = max(max_length, len(window))
        
        return max_length
