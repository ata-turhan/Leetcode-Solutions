from typing import List
import heapq

class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        """
        Return the maximum number of queries that can be removed while still
        converting nums into a zero array using the remaining queries.
        """
        # 1. Sort by left endpoint
        queries.sort(key=lambda x: x[0])
        n, q = len(nums), len(queries)

        # available: max-heap of right endpoints (stored as negatives)
        available: List[int] = []
        # running: min-heap of right endpoints currently in use
        running: List[int] = []

        idx = 0  # pointer into the sorted queries list

        # 2. Iterate through each index in nums
        for i, need in enumerate(nums):
            # 2a. Add all queries starting at or before i
            while idx < q and queries[idx][0] <= i:
                heapq.heappush(available, -queries[idx][1])
                idx += 1

            # 2b. Remove expired queries from running
            while running and running[0] < i:
                heapq.heappop(running)

            # 2c. Ensure at least 'need' covering queries
            while len(running) < need:
                if not available or -available[0] < i:
                    return -1
                # Choose the available query with the farthest right endpoint
                r = -heapq.heappop(available)
                heapq.heappush(running, r)

        # 3. The rest of 'available' can be removed
        return len(available)
