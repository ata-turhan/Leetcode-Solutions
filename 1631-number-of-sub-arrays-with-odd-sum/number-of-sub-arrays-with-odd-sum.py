from typing import List
from collections import defaultdict

class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        """Counts the number of subarrays with an odd sum using prefix sum and hashmap optimization."""
        MOD = 10**9 + 7
        odd_count, even_count = 0, 1  # Even count starts at 1 to handle cases where subarray itself is odd
        cur_prefix_sum, num_pairs = 0, 0
        
        for num in arr:
            cur_prefix_sum += num
            if cur_prefix_sum % 2 == 0:
                num_pairs += odd_count  # Only odd prefixes contribute to odd subarrays
                even_count += 1
            else:
                num_pairs += even_count  # Only even prefixes contribute to odd subarrays
                odd_count += 1

        return num_pairs % MOD
