import math
from heapq import heapify, heappop, heappush
from typing import List

class Solution:
    def pickGifts(self, giftCounts: List[int], reductionCount: int) -> int:
        """
        Reduces the largest gift count by taking its square root `reductionCount` times and returns the total sum.

        :param giftCounts: List of integers representing the initial gift counts.
        :param reductionCount: Integer representing the number of reduction operations.
        :return: Integer representing the total sum of gift counts after operations.
        """
        # Convert the gift counts into a max-heap by storing negative values
        maxHeap = [-gift for gift in giftCounts]
        heapify(maxHeap)

        # Perform `reductionCount` operations to reduce the largest gift count
        for _ in range(reductionCount):
            largestGift = -heappop(maxHeap)  # Extract the largest gift count
            reducedGift = math.floor(largestGift ** 0.5)  # Reduce the gift count using square root
            heappush(maxHeap, -reducedGift)  # Push the reduced gift count back into the heap

        # Return the total sum of the remaining gift counts
        totalSum = -sum(maxHeap)
        return totalSum
