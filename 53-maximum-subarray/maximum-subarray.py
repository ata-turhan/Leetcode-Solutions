from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        Find the maximum sum of any contiguous subarray within the given array.

        Args:
            nums (List[int]): List of integers.

        Returns:
            int: The maximum sum of any contiguous subarray.
        """
        # Initialize variables
        max_sum = nums[0]   # Maximum sum initialized with the first element of the array
        current_sum = 0     # Current sum initialized as 0
        
        # Iterate through the array
        for num in nums:
            # Update the current sum by taking the maximum of the current element and the sum of the current element and previous sum
            current_sum = max(current_sum + num, num)
            
            # Update the maximum sum encountered so far
            max_sum = max(max_sum, current_sum)
        
        # Return the maximum sum
        return max_sum
