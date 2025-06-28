from typing import List
from collections import Counter

class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        """
        Returns a subsequence of length k with the maximum possible sum,
        preserving the relative order of elements in `nums`.
        """
        # Count the k largest elements (may include duplicates)
        top_k_counts = Counter(sorted(nums)[-k:])
        
        subsequence: List[int] = []
        for num in nums:
            if top_k_counts[num] > 0:
                subsequence.append(num)
                top_k_counts[num] -= 1
        
        return subsequence
