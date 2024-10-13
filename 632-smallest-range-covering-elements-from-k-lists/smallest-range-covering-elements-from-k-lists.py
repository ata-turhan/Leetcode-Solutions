import heapq
import math
from typing import List

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        # Initialize the answer range to the largest possible range
        ans = (-math.inf, math.inf)

        # Initialize a min heap and variable to track the highest value in the current range
        min_heap = []
        current_max = -math.inf
        
        # Populate the heap with the first element of each list and track the current maximum
        for i in range(len(nums)):
            heapq.heappush(min_heap, (nums[i][0], i, 0))
            current_max = max(current_max, nums[i][0])

        # Process the heap until one of the lists is exhausted
        while True:
            current_min, list_index, element_index = heapq.heappop(min_heap)

            # Update the answer if we find a smaller range
            if current_max - current_min < ans[1] - ans[0]:
                ans = (current_min, current_max)

            # If we reach the end of one list, return the best range found
            if element_index + 1 == len(nums[list_index]):
                return list(ans)

            # Get the next element from the same list and update the heap
            next_element = nums[list_index][element_index + 1]
            current_max = max(current_max, next_element)  # Update current max in range
            heapq.heappush(min_heap, (next_element, list_index, element_index + 1))
