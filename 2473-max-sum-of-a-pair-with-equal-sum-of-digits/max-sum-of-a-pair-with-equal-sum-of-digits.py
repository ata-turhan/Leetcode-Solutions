from heapq import heappush, heappop
from collections import defaultdict
from typing import List

class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        """
        Finds the maximum sum of two numbers in the list whose sum of digits is the same.

        :param nums: List of integers.
        :return: Maximum sum of two numbers with the same digit sum, or -1 if no such pair exists.
        """

        def get_digit_sum(num: int) -> int:
            """Calculates the sum of digits of a number."""
            digit_sum = 0
            while num > 0:
                digit_sum += num % 10
                num //= 10
            return digit_sum

        digit_sum_groups = defaultdict(list)  # Maps digit sums to max-heap of numbers

        # Group numbers by their sum of digits and maintain max-heap for each group
        for num in nums:
            digit_sum = get_digit_sum(num)
            heappush(digit_sum_groups[digit_sum], -num)  # Using min-heap with negation

        max_pair_sum = -1  # Stores the maximum sum of two numbers with the same digit sum

        # Extract the top two largest values for each digit sum group
        for heap in digit_sum_groups.values():
            if len(heap) >= 2:
                first_max, second_max = -heappop(heap), -heappop(heap)
                max_pair_sum = max(max_pair_sum, first_max + second_max)

        return max_pair_sum
