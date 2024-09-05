from typing import List
import math

class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        # Calculate the sum of the existing rolls and the total expected sum
        sum_m = sum(rolls)
        len_m = len(rolls)
        total_sum = mean * (n + len_m)
        sum_n = total_sum - sum_m
        
        # The sum of the missing rolls should be between n and 6 * n
        if not (n <= sum_n <= 6 * n):
            return []

        # Determine the base value for each of the missing rolls
        base_value = sum_n // n
        extras = sum_n % n
        
        # Construct the missing rolls array
        missing_rolls = [base_value] * n
        
        # Distribute the remaining extras to the first few rolls
        for i in range(extras):
            missing_rolls[i] += 1
        
        return missing_rolls
