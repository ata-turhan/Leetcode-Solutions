import heapq
from typing import List

class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        min_heap = []

        # Push fractions (arr[i]/arr[-1]) into the heap for all i
        for i in range(len(arr) - 1):
            heapq.heappush(min_heap, (arr[i] / arr[-1], i, len(arr) - 1))

        # Pop the smallest fraction from the heap (k-1) times
        for _ in range(k - 1):
            smallest_frac, numerator, denominator = heapq.heappop(min_heap)
            # If the nominator is less than the denominator - 1, push the next smaller fraction
            if numerator < denominator - 1:
                next_frac = arr[numerator] / arr[denominator - 1]
                heapq.heappush(min_heap, (next_frac, numerator, denominator - 1))

        # Get the kth smallest fraction from the heap
        kth_frac, kth_numerator, kth_denominator = heapq.heappop(min_heap)
        # Return the kth smallest fraction as a list [nominator, denominator]
        return [arr[kth_numerator], arr[kth_denominator]]
