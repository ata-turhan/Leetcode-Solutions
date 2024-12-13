from heapq import heapify, heappop
from typing import List

class Solution:
    def findScore(self, nums: List[int]) -> int:
        """
        Finds the score by selecting the smallest unmarked number and marking its adjacent indices.

        :param nums: List of integers representing the input numbers.
        :return: Integer representing the calculated score.
        """
        # Set to keep track of marked indices
        marked_indices = set()
        
        # Create a heap of (value, index) pairs for processing in increasing order
        value_index_pairs = [(num, index) for index, num in enumerate(nums)]
        heapify(value_index_pairs)

        score = 0

        # Process heap until empty
        while value_index_pairs:
            num, index = heappop(value_index_pairs)
            
            # If the current index is not already marked, process it
            if index not in marked_indices:
                score += num  # Add the value to the score
                marked_indices.add(index - 1)  # Mark left neighbor
                marked_indices.add(index + 1)  # Mark right neighbor

        return score
