from typing import List
from collections import Counter

class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        """Checks if the array can be divided into pairs with equal elements."""
        
        frequency_map = Counter(nums)

        return all(count % 2 == 0 for count in frequency_map.values())
