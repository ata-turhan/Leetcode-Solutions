from typing import List

class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        # Count the number of only even and only odd numbers
        count_only_evens = len([num for num in nums if num % 2 == 0])
        count_only_odds = len([num for num in nums if num % 2 == 1])
        
        # Inner function to calculate the maximum alternating sequence length
        def max_alternating_length(start_with_even: bool) -> int:
            choose_even = start_with_even
            max_length = 0
            for num in nums:
                if choose_even:
                    if num % 2 == 0:
                        max_length += 1
                        choose_even = False
                else:
                    if num % 2 == 1:
                        max_length += 1
                        choose_even = True
            return max_length

        # Calculate the maximum alternating sequence lengths
        max_length_even_start = max_alternating_length(True)
        max_length_odd_start = max_alternating_length(False)
        
        # Return the maximum length among only evens, only odds, and alternating sequences
        return max(count_only_evens, count_only_odds, max_length_even_start, max_length_odd_start)
