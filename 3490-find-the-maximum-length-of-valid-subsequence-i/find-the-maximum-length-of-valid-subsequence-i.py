from typing import List

class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        # Count the number of only even and only odd numbers
        count_only_evens = len([num for num in nums if num % 2 == 0])
        count_only_odds = len([num for num in nums if num % 2 == 1])
        
        # Check for the maximum length by alternating starting with an even number
        alternating_even_start = True
        max_length_even_start = 0
        for num in nums:
            if alternating_even_start:
                if num % 2 == 0:
                    max_length_even_start += 1
                    alternating_even_start = False
            else:
                if num % 2 == 1:
                    max_length_even_start += 1
                    alternating_even_start = True
                    
        # Check for the maximum length by alternating starting with an odd number
        alternating_odd_start = False
        max_length_odd_start = 0
        for num in nums:
            if alternating_odd_start:
                if num % 2 == 0:
                    max_length_odd_start += 1
                    alternating_odd_start = False
            else:
                if num % 2 == 1:
                    max_length_odd_start += 1
                    alternating_odd_start = True
                    
        # Return the maximum length among only evens, only odds, and alternating sequences
        return max(count_only_evens, count_only_odds, max_length_even_start, max_length_odd_start)
