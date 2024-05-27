from heapq import heapify, heappop, heappush
from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        """
        Simulates the stone smashing game and returns the weight of the last remaining stone.
        If all stones are smashed to zero weight, returns 0.
        
        :param stones: List[int] - List of initial stone weights.
        :return: int - The weight of the last remaining stone or 0 if all stones are smashed.
        """
        # Convert the stones list into a max-heap by negating the values
        max_heap = [-stone for stone in stones]
        heapify(max_heap)  # Transform the list into a heap in-place
        
        # Continue smashing stones until there is one or zero stones left
        while len(max_heap) > 1:
            # Pop the two heaviest stones
            heaviest = heappop(max_heap)
            second_heaviest = heappop(max_heap)
            
            # If the stones are not of equal weight, push the difference back into the heap
            if heaviest != second_heaviest:
                heappush(max_heap, heaviest - second_heaviest)
        
        # Return the weight of the last remaining stone or 0 if no stones are left
        return -max_heap[0] if max_heap else 0

# Example usage:
# sol = Solution()
# print(sol.lastStoneWeight([2, 7, 4, 1, 8, 1]))  # Output: 1
