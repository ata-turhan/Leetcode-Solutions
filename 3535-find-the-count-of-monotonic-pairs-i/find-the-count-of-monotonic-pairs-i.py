from typing import List
from functools import cache

class Solution:
    def countOfPairs(self, nums: List[int]) -> int:
        MOD = 10**9 + 7  # Define the modulus to prevent overflow in large numbers
        
        @cache
        def dp(index: int, val: int) -> int:
            """
            Dynamic programming function to calculate the number of valid pairs.

            :param index: The current index in the nums list.
            :param val: The current value used in pair formation.
            :return: The count of valid pairs from the current index onwards.
            """
            # Base case: if we reach the last index, return 1 as this path is valid
            if index == len(nums) - 1:
                return 1
            
            val1 = val  # The value from the current pair
            val2 = nums[index] - val1  # Calculate the corresponding value
            
            res = 0
            # Iterate over possible new values for the next pair
            for new_val1 in range(val1, nums[index + 1] + 1):
                new_val2 = nums[index + 1] - new_val1
                # Ensure the new pair is valid by checking the decreasing condition
                if new_val2 > val2:
                    continue
                res += dp(index + 1, new_val1) % MOD
            
            return res
        
        # Initialize the result by iterating over all possible starting values
        result = 0
        for i in range(nums[0] + 1):
            result += dp(0, i) % MOD
        
        return result % MOD
