from typing import List
from collections import defaultdict

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        # Transform the array: 1 for odd, 0 for even
        transformed = [1 if num % 2 == 1 else 0 for num in nums]
        
        # Initialize prefix sum and count dictionary
        prefix_sum = 0
        count = defaultdict(int)
        count[0] = 1  # To handle the case when the subarray starts from index 0
        nice_count = 0
        
        for num in transformed:
            # Update the prefix sum
            prefix_sum += num
            
            # Check if there is a subarray that ends at the current index
            # and contains exactly k odd numbers
            if prefix_sum - k in count:
                nice_count += count[prefix_sum - k]
            
            # Update the count of the current prefix sum
            count[prefix_sum] += 1
        
        # Return the total number of nice subarrays
        return nice_count

