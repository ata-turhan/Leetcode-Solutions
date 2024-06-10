from typing import List

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        count = 0
        sorted_heights = sorted(heights)  # Create a sorted version of heights
        for i in range(len(heights)):
            if sorted_heights[i] != heights[i]:  # Compare the sorted list with the original list
                count += 1  # Increment count for each mismatch
        return count
