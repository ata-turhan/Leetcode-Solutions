from typing import List
from collections import Counter

class Solution:
    def sumDigitDifferences(self, nums: List[int]) -> int:
        total_difference_sum = 0
        n = len(nums)
        
        # Determine the maximum number of digits in the largest number
        max_digits = 0
        max_num = max(nums)
        while max_num > 0:
            max_num //= 10
            max_digits += 1

        # Loop through each digit place (units, tens, hundreds, etc.)
        for digit_place in range(max_digits):
            digit_values = [num // (10 ** digit_place) % 10 for num in nums]
            digit_counter = Counter(digit_values)
            
            # Calculate the contribution of each digit to the total difference sum
            for digit in digit_counter:
                count = digit_counter[digit]
                total_difference_sum += count * (n - count)

        # Each difference is counted twice, so divide the total by 2
        return total_difference_sum // 2
