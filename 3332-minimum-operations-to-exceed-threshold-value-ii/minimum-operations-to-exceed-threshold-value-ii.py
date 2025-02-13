from heapq import heapify, heappop, heappush
from typing import List

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        """
        Finds the minimum number of operations required to make all elements in nums at least k.

        :param nums: List of integers.
        :param k: Target minimum value for all elements.
        :return: Minimum number of operations needed.
        """

        heapify(nums)  # Convert the list into a min-heap for efficient retrieval of the smallest elements
        operations_count = 0

        while len(nums) >= 2:
            if nums[0] >= k:
                break  # Stop when the smallest element meets or exceeds k
                
            smallest, second_smallest = heappop(nums), heappop(nums)  # Extract the two smallest elements
            new_value = smallest * 2 + second_smallest  # Compute the new merged value
            heappush(nums, new_value)  # Push the new value back into the heap
            operations_count += 1  # Increment the count of operations

        return operations_count
