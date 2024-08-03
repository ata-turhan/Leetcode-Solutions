from typing import List
from collections import Counter

class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        # Count the frequency of each element in target and arr
        return Counter(target) == Counter(arr)
