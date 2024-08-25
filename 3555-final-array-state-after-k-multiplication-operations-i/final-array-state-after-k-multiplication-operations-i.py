import heapq
from typing import List

class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        # Initialize a min-heap to store the (value, index) pairs
        heap = []
        for i, num in enumerate(nums):
            heapq.heappush(heap, (num, i))

        # Perform k operations, each time multiplying the smallest value by the multiplier
        for _ in range(k):
            min_val, i = heapq.heappop(heap)  # Extract the smallest value
            heapq.heappush(heap, (min_val * multiplier, i))  # Push the updated value back with the same index

        # Sort the heap based on the original indices to restore the original order
        heap.sort(key=lambda x: x[1])

        # Extract and return the final values from the heap, in the original order
        return [num for num, i in heap]
