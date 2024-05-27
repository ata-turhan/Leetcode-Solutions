from heapq import heapify, heappop, heappush
from typing import List

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        """
        Initializes the KthLargest object with the integer k and the list of integers nums.
        The object maintains a min-heap of the k largest elements seen so far.
        
        :param k: int - The kth position to find the largest element.
        :param nums: List[int] - List of initial numbers.
        """
        self.k = k  # Store the value of k
        heapify(nums)  # Convert the list nums into a min-heap
        # Reduce the heap size to k by popping the smallest elements
        while len(nums) > k:
            heappop(nums)
        self.heap = nums  # Store the heap

    def add(self, val: int) -> int:
        """
        Adds a new integer val to the stream and returns the kth largest element.
        
        :param val: int - New integer to add.
        :return: int - The kth largest element.
        """
        heappush(self.heap, val)  # Add the new value to the heap
        # Ensure the heap size does not exceed k by removing the smallest element
        while len(self.heap) > self.k:
            heappop(self.heap)
        return self.heap[0]  # The kth largest element is the root of the min-heap

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
