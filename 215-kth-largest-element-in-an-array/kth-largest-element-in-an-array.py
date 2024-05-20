import heapq
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Create a min-heap with the first k elements
        heap = nums[:k]
        heapq.heapify(heap)
        
        # Process the remaining elements
        for num in nums[k:]:
            # If the current number is larger than the smallest number in the heap
            if num > heap[0]:
                # Remove the smallest number
                heapq.heappop(heap)
                # Add the current number to the heap
                heapq.heappush(heap, num)
        
        # The root of the heap is the k-th largest number
        return heap[0]
