from typing import List
from collections import defaultdict

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        """
        Finds the length of the longest subarray with at most two distinct fruit types.
        This models the problem as finding the longest subarray with at most two distinct values.
        """
        basket = defaultdict(int)  # Stores fruit type -> count
        left = 0
        max_length = 0

        for right, fruit in enumerate(fruits):
            basket[fruit] += 1

            # If there are more than 2 types, shrink window from the left
            while len(basket) > 2:
                basket[fruits[left]] -= 1
                if basket[fruits[left]] == 0:
                    del basket[fruits[left]]
                left += 1

            # Update max window size
            max_length = max(max_length, right - left + 1)

        return max_length
