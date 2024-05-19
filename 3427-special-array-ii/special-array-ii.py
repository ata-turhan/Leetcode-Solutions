from typing import List
from bisect import bisect_left, bisect_right

class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        # Determine if the first element is even or odd
        is_even = nums[0] % 2 == 0
        consecutive_errors = []

        # Identify indices where the special condition is violated
        for i in range(1, len(nums)):
            if (is_even and nums[i] % 2 == 0) or (not is_even and nums[i] % 2 != 0):
                consecutive_errors.append(i)
            is_even = nums[i] % 2 == 0  # Toggle the expected parity

        results = []
        
        # Process each query
        for start, end in queries:
            # Use binary search to find the range of error indices within the query range
            left_idx = bisect_left(consecutive_errors, start + 1)
            right_idx = bisect_right(consecutive_errors, end)
            
            # If there are errors in the range, the result is False; otherwise, True
            if right_idx > left_idx:
                results.append(False)
            else:
                results.append(True)
        
        return results
