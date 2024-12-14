from collections import deque
from typing import List

class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        """
        Count the number of continuous subarrays satisfying the condition:
        The maximum element is at most 2 units greater than the minimum element.
        
        :param nums: List of integers representing the input array.
        :return: Integer count of such subarrays.
        """
        max_indices = deque()  # Deque to store indices of potential maximum elements
        min_indices = deque()  # Deque to store indices of potential minimum elements
        left_pointer = 0       # Left boundary of the sliding window
        subarray_count = 0     # Total count of valid subarrays

        # Iterate over the array with the right pointer
        for right_pointer in range(len(nums)):
            # Maintain decreasing order in the max_indices deque
            while max_indices and nums[max_indices[-1]] <= nums[right_pointer]:
                max_indices.pop()
            max_indices.append(right_pointer)

            # Maintain increasing order in the min_indices deque
            while min_indices and nums[min_indices[-1]] >= nums[right_pointer]:
                min_indices.pop()
            min_indices.append(right_pointer)

            # Adjust the left pointer if the subarray condition is violated
            while nums[max_indices[0]] - nums[min_indices[0]] > 2:
                if max_indices[0] == left_pointer:
                    max_indices.popleft()
                if min_indices[0] == left_pointer:
                    min_indices.popleft()
                left_pointer += 1

            # Add the count of valid subarrays ending at the current right pointer
            subarray_count += right_pointer - left_pointer + 1

        return subarray_count
