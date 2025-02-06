from math import factorial
from collections import defaultdict
from typing import List

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        """
        Finds the number of unique tuples (a, b, c, d) where:
        a * b = c * d and a, b, c, d are distinct numbers from the list.
        
        :param nums: List of distinct positive integers.
        :return: Number of valid tuples.
        """
        product_counts = defaultdict(int)  # Stores the count of each unique product

        # Compute all pairwise products and count their occurrences
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                product = nums[i] * nums[j]
                product_counts[product] += 1

        total_tuples = 0

        # Calculate the number of valid tuples from each product count
        for count in product_counts.values():
            if count >= 2:
                # Calculate combinations of choosing 2 pairs (order doesn't matter)
                total_tuples += (factorial(count) // (factorial(count - 2) * 2)) * 8
        
        return total_tuples
