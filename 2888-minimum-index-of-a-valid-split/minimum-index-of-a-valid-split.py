from typing import List
from collections import Counter

class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        """Finds the minimum index to split the array such that the dominant element remains dominant in both parts."""
        
        frequency_map = Counter(nums)
        dominant_element = max(frequency_map, key=frequency_map.get)
        total_dominant_count = frequency_map[dominant_element]

        left_dominant_count = 0
        length = len(nums)

        for i in range(length - 1):  # Can't split at last index
            if nums[i] == dominant_element:
                left_dominant_count += 1

            left_length = i + 1
            right_length = length - left_length
            right_dominant_count = total_dominant_count - left_dominant_count

            if (
                left_dominant_count > left_length // 2 and
                right_dominant_count > right_length // 2
            ):
                return i

        return -1
