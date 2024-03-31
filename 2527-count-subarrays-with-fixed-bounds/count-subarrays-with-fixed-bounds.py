from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        # Initialize result variable
        res = 0
        
        # Initialize variables to keep track of indices
        left_bound = -1  # Left bound of the current subarray
        recent_min_index = -1  # Index of the most recent occurrence of minK
        recent_max_index = -1  # Index of the most recent occurrence of maxK
        
        # Loop through each element in nums
        for i, num in enumerate(nums):
            # Check if the current number is outside the range [minK, maxK]
            if num < minK or num > maxK:
                # If so, update the left bound of the subarray
                left_bound = i
            else:
                # If the current number is within the range [minK, maxK]
                if num == minK:
                    # Update the index of the most recent occurrence of minK
                    recent_min_index = i
                if num == maxK:
                    # Update the index of the most recent occurrence of maxK
                    recent_max_index = i
            
            # Calculate the number of valid subarrays ending at the current index
            valid_subarray_count = min(recent_min_index, recent_max_index) - left_bound
            
            # Add the count of valid subarrays to the result
            res += valid_subarray_count if valid_subarray_count > 0 else 0
        
        # Return the total count of valid subarrays
        return res
