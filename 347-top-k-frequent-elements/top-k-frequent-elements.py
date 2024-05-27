from typing import List
from collections import defaultdict
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Count the frequency of each number in the array
        frequency_map = defaultdict(int)
        for num in nums:
            frequency_map[num] += 1

        # Step 2: Use a max-heap to keep track of the top k frequent elements
        # Since heapq in Python is a min-heap, we use negative frequencies to simulate a max-heap
        max_heap = []
        for num, frequency in frequency_map.items():
            heapq.heappush(max_heap, (-frequency, num))

        # Step 3: Extract the top k elements from the heap
        top_k_frequent = []
        for _ in range(k):
            top_k_frequent.append(heapq.heappop(max_heap)[1])

        return top_k_frequent

# Example usage:
# sol = Solution()
# print(sol.topKFrequent([1,1,1,2,2,3], 2))  # Output: [1, 2]
