from typing import List
from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Initialize variables
        prefix_sum = 0
        count_subarrays = 0
        freq_map = defaultdict(int)
        
        # Base case: empty subarray sum is 0
        freq_map[0] = 1
        
        # Iterate through the array
        for num in nums:
            # Update the cumulative sum
            prefix_sum += num
            
            # Check if there is a prefix sum that would make a subarray sum equal to k
            if (prefix_sum - k) in freq_map:
                count_subarrays += freq_map[prefix_sum - k]
            
            # Record the current prefix sum in the frequency map
            freq_map[prefix_sum] += 1
        
        return count_subarrays
