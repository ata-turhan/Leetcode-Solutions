from sortedcontainers import SortedList

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        left = 0
        max_length = 0
        window = SortedList()
        
        for right in range(len(nums)):
            window.add(nums[right])
            current_diff = window[-1] - window[0]
            
            # Check if the difference within the window exceeds the limit
            if current_diff <= limit:
                max_length = max(max_length, len(window))
            else:
                # If the difference exceeds the limit, remove the leftmost element
                window.remove(nums[left])
                left += 1
        
        return max_length
