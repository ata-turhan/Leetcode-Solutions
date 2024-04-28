from functools import reduce
from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """
        Find the missing number in the given list of integers.

        Args:
        - nums: List of integers containing all numbers from 0 to n except one.

        Returns:
        - int: The missing number.
        """
        # Calculate the XOR of all numbers from 0 to n
        expected_xor = reduce(lambda a, b: a ^ b, range(len(nums) + 1))
        # Calculate the XOR of all numbers in the given list
        actual_xor = reduce(lambda a, b: a ^ b, nums)
        # Return the XOR of the expected and actual XORs, which will result in the missing number
        return expected_xor ^ actual_xor
