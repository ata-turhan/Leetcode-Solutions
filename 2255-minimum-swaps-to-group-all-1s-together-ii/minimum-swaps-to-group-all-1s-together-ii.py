from typing import List

class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        # Create a circular version of nums by concatenating it with itself
        circular_nums = nums + nums
        
        # Total number of 1s in the original array
        total_ones = nums.count(1)
        
        # Initialize the minimum number of 0s needed to be swapped with a high value
        min_zeros_to_swap = float('inf')
        
        # Count the number of 0s and 1s in the first window of size total_ones
        current_zero_count = nums[:total_ones].count(0)
        
        # Set the initial minimum number of 0s to the count in the first window
        min_zeros_to_swap = current_zero_count

        # Slide the window across the circular_nums array
        for i in range(total_ones, len(circular_nums)):
            # Include the new element in the window
            if circular_nums[i] == 0:
                current_zero_count += 1
                
            # Exclude the oldest element from the window
            if circular_nums[i - total_ones] == 0:
                current_zero_count -= 1

            # Update the minimum number of 0s found in any window
            min_zeros_to_swap = min(min_zeros_to_swap, current_zero_count)

        # Return the minimum number of swaps required
        return min_zeros_to_swap
