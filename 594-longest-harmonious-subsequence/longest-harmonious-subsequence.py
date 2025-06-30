from typing import List
from collections import Counter

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        """
        Find the length of the longest harmonious subsequence.
        A harmonious array is where the difference between the maximum and minimum elements is exactly 1.
        """
        freq: Counter[int] = Counter(nums)
        max_length: int = 0

        for num in freq:
            if num + 1 in freq:
                max_length = max(max_length, freq[num] + freq[num + 1])

        return max_length
