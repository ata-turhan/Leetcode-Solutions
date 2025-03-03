from typing import List

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        """Rearranges the array by placing elements smaller, equal, and larger than the pivot in order."""
        smallers, equals, largers = [], [], []

        # Categorize numbers based on their relation to the pivot
        for num in nums:
            if num < pivot:
                smallers.append(num)
            elif num > pivot:
                largers.append(num)
            else:
                equals.append(num)

        # Concatenate lists efficiently
        return smallers + equals + largers
