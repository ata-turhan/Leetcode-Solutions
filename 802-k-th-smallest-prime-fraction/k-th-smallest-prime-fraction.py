import heapq
from typing import List

class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        heap = []

        # Push fractions (arr[i]/arr[-1]) into the heap for all i
        for i in range(len(arr)-1):
            heapq.heappush(heap, (arr[i]/arr[len(arr)-1], i, len(arr)-1))

        # Pop the smallest fraction from the heap (k-1) times
        for _ in range(k-1):
            smallest_frac, nominator, denominator = heapq.heappop(heap)
            # If the nominator is less than the denominator - 1, push the next smaller fraction
            if nominator < denominator - 1:
                heapq.heappush(heap, (arr[nominator]/arr[denominator-1], nominator, denominator-1))

        # Get the kth smallest fraction from the heap
        kth_smallest_frac, kth_smallest_nominator, kth_smallest_denominator = heapq.heappop(heap)
        # Return the kth smallest fraction as a list [nominator, denominator]
        return [arr[kth_smallest_nominator], arr[kth_smallest_denominator]]
