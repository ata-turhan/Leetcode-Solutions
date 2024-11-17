from typing import List
from heapq import heappush, heappop

class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        # Initialize shortest length with a value greater than possible
        shortest_length = len(nums) + 1
        cumulative_sum = 0
        previous_sums = []  # Min-heap to store cumulative sums with their indices
        heappush(previous_sums, (0, -1))  # Base case: cumulative sum before the array starts

        for current_index in range(len(nums)):
            cumulative_sum += nums[current_index]

            # Check if any previous cumulative sum satisfies the condition for a valid subarray
            while previous_sums and cumulative_sum - previous_sums[0][0] >= k:
                _, prev_index = heappop(previous_sums)
                shortest_length = min(shortest_length, current_index - prev_index)

            # Push the current cumulative sum with its index into the heap
            heappush(previous_sums, (cumulative_sum, current_index))

        # Return the shortest valid subarray length or -1 if no valid subarray exists
        return shortest_length if shortest_length <= len(nums) else -1
