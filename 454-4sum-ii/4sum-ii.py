from collections import defaultdict
from typing import List

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        sum_counts = defaultdict(int)
        
        # Compute all possible sums of pairs from nums1 and nums2
        for num1 in nums1:
            for num2 in nums2:
                sum_counts[num1 + num2] += 1
        
        result = 0
        
        # Check pairs from nums3 and nums4 to find the negation in sum_counts
        for num3 in nums3:
            for num4 in nums4:
                target_sum = -(num3 + num4)
                if target_sum in sum_counts:
                    result += sum_counts[target_sum]
        
        return result
