import heapq
from typing import List

class Solution:
    def makePrefSumNonNegative(self, nums: List[int]) -> int:
        # Initialize a min heap, cumulative sum, and count for negative sums
        min_heap = []
        cumulative_sum = 0
        negative_count = 0

        # Iterate through the numbers in the input list
        for num in nums:
            # Add the current number to the cumulative sum
            cumulative_sum += num
            # Push the current number onto the min heap
            heapq.heappush(min_heap, num)
            # Check if the cumulative sum becomes negative
            if cumulative_sum < 0:
                # If so, pop the smallest number from the heap
                min_num = heapq.heappop(min_heap)
                # Subtract the popped number from the cumulative sum
                cumulative_sum -= min_num
                # Increment the count of negative sums
                negative_count += 1
        
        # Return the count of negative sums
        return negative_count
