import heapq
from typing import List

class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        # Convert the happiness values to negative and heapify
        happiness = [-h for h in happiness]
        heapq.heapify(happiness)
        
        # Initialize the result variable
        res = 0
        
        # Iterate over the range from 1 to k+1
        for count in range(1, k+1):
            # Pop the maximum happiness value from the heap
            happiness_val = -heapq.heappop(happiness)
            # Calculate the happiness contribution for the current count
            res += max(0, happiness_val - count + 1)
        
        return res
