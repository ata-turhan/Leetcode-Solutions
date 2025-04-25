from typing import List, Dict
from collections import defaultdict

class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        """
        Count subarrays where the number of elements with nums[i] % modulo == k,
        modulo ‘modulo’, equals k.
        """
        freq: Dict[int, int] = defaultdict(int)
        freq[0] = 1  # one way to have prefix count = 0 before starting
        prefix_count = 0
        result = 0

        for num in nums:
            # increment prefix_count when current element matches the condition
            if num % modulo == k:
                prefix_count += 1

            # we need (prefix_count - prev_count) % modulo == k
            # → prev_count % modulo == (prefix_count - k) % modulo
            target = (prefix_count - k) % modulo
            result += freq.get(target, 0)

            # record current prefix_count mod modulo
            freq[prefix_count % modulo] += 1

        return result
