from typing import List
from functools import cache

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        """
        Find the number of ways to assign '+' and '-' signs to elements in nums
        such that their sum equals the target.
        
        :param nums: List of integers.
        :param target: The target sum.
        :return: Number of ways to achieve the target sum.
        """
        @cache
        def countWays(index: int, current_sum: int) -> int:
            """
            Recursive helper function to count ways to reach the target sum.
            
            :param index: Current index in the nums array.
            :param current_sum: Current sum of the assigned signs.
            :return: Number of ways to achieve the target sum from this point.
            """
            # Base case: If all numbers are processed, check if we reached the target
            if index == len(nums):
                return 1 if current_sum == target else 0

            # Recursive case: Try adding and subtracting the current number
            add_ways = countWays(index + 1, current_sum + nums[index])
            subtract_ways = countWays(index + 1, current_sum - nums[index])

            return add_ways + subtract_ways

        return countWays(0, 0)
