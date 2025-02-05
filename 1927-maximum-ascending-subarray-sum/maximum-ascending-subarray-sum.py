from typing import List

class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        """
        Finds the maximum sum of any ascending subarray in the given list.

        :param nums: List of integers.
        :return: Maximum sum of an ascending subarray.
        """
        max_ascending_sum = max(nums)  # Initialize with the maximum single element
        current_sum = nums[0]  # Start with the first element

        # Iterate through the list to find the max sum of an ascending subarray
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:  
                current_sum += nums[i]  # Continue adding to the current subarray sum
            else:
                current_sum = nums[i]  # Reset sum to the current element
            
            # Update the maximum sum encountered so far
            max_ascending_sum = max(max_ascending_sum, current_sum)

        return max_ascending_sum
