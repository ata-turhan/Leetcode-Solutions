from collections import Counter
from typing import List

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        """
        Returns the largest lucky integer in the array.
        A lucky integer is one whose value is equal to its frequency in the array.
        If no such integer exists, returns -1.
        """
        frequencies: Counter[int] = Counter(arr)
        lucky_numbers: List[int] = [num for num, count in frequencies.items() if num == count]
        return max(lucky_numbers, default=-1)
