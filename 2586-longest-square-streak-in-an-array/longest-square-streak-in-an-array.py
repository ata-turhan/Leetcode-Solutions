from typing import List
from collections import Counter

class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        # Count occurrences of each number in the list
        frequency_map = Counter(nums)
        max_streak = 0

        # Iterate through each unique number in the frequency map
        for num in frequency_map:
            current_streak = 0
            current_num = num
            
            # Keep squaring the number if it exists in the frequency map
            while current_num in frequency_map:
                current_streak += 1
                current_num **= 2
            
            # Update the max streak if the current streak is longer
            max_streak = max(max_streak, current_streak)

        # Return the longest streak, or -1 if no valid streak is found
        return max_streak if max_streak > 1 else -1
