from typing import List
from collections import defaultdict

class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        """Merges two sorted arrays by summing values with the same ID and returning a sorted result."""
        id_to_values = defaultdict(int)

        # Merge both lists into the dictionary
        for nums in (nums1, nums2):
            for id_, val in nums:
                id_to_values[id_] += val

        # Return sorted merged list
        return [[key, id_to_values[key]] for key in sorted(id_to_values)]
