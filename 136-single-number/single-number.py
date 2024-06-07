from typing import List
from functools import reduce

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        Finds the single number that appears only once in a list where every other number appears twice.
        
        :param nums: List[int] - The input list of integers.
        :return: int - The single number that appears only once.
        """
        # Use XOR operation to find the single number that appears only once
        return reduce(lambda a, b: a ^ b, nums)

# Example usage:
# sol = Solution()
# print(sol.singleNumber([4, 1, 2, 1, 2]))  # Output: 4
# print(sol.singleNumber([2, 2, 1]))        # Output: 1
