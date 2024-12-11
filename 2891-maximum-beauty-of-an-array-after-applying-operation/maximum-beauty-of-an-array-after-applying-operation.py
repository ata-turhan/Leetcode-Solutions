from typing import List

class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        """
        Calculates the maximum number of elements in a subarray such that the difference
        between the smallest and largest elements in the subarray does not exceed 2 * k.

        :param nums: List of integers representing the input array.
        :param k: Integer representing the tolerance for element differences.
        :return: Integer representing the maximum number of elements satisfying the condition.
        """
        # Step 1: Sort the input list to allow efficient sliding window calculation
        nums.sort()
        
        # Step 2: Initialize pointers for the sliding window and track maximum length
        left_pointer = 0
        max_window_size = 0
        
        # Step 3: Expand the sliding window using the right pointer
        for right_pointer in range(len(nums)):
            # Shrink the window from the left if the condition is violated
            while nums[right_pointer] - nums[left_pointer] > 2 * k:
                left_pointer += 1
            
            # Update the maximum window size
            max_window_size = max(max_window_size, right_pointer - left_pointer + 1)

        return max_window_size
