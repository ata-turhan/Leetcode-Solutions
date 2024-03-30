from collections import defaultdict
from typing import List

class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        
        # Helper function to count subarrays with at most k distinct elements
        def count_subarrays_with_k_distinct_at_most(nums, k):
            counts = defaultdict(int)  # Dictionary to store counts of elements
            left = 0  # Left pointer for sliding window
            result = 0  # Counter for subarrays
            for right in range(len(nums)):  # Iterate through the array with a sliding window
                counts[nums[right]] += 1  # Update count of current element
                while len(counts) > k:  # If number of distinct elements exceeds k
                    counts[nums[left]] -= 1  # Decrease count of leftmost element in the window
                    if counts[nums[left]] == 0:  # If count becomes 0, remove element from counts
                        del counts[nums[left]]
                    left += 1  # Move left pointer to the right to shrink the window
                result += right - left + 1  # Increment result by size of valid subarray
            return result
        
        # Calculate total subarrays with exactly k distinct elements
        return count_subarrays_with_k_distinct_at_most(nums, k) - count_subarrays_with_k_distinct_at_most(nums, k - 1)
