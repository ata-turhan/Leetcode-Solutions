from collections import Counter
from typing import List

class Solution:
    def countPairs(self, nums: List[int]) -> int:
        def can_become_almost_equal(x: int, y: int) -> bool:
            # Convert numbers to strings to facilitate digit comparison
            x_str, y_str = str(x), str(y)
            
            # Pad the shorter string with leading zeros to make both strings of equal length
            if len(x_str) > len(y_str):
                y_str = "0" * (len(x_str) - len(y_str)) + y_str
            elif len(x_str) < len(y_str):
                x_str = "0" * (len(y_str) - len(x_str)) + x_str
            
            # Count the frequency of each digit in both numbers
            x_count = Counter(x_str)
            y_count = Counter(y_str)

            # If the frequency counts do not match, they cannot become almost equal
            if x_count != y_count:
                return False

            # Count the number of differing digits between the two strings
            different_chars = 0
            for x_char, y_char in zip(x_str, y_str):
                if x_char != y_char:
                    different_chars += 1

            # They can become almost equal if there are at most two differing digits
            return different_chars <= 2

        n = len(nums)
        count = 0
        
        # Check all pairs of numbers to see if they can become almost equal
        for i in range(n):
            for j in range(i + 1, n):
                if can_become_almost_equal(nums[i], nums[j]):
                    count += 1
                    
        return count
