from typing import List
from collections import deque

class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        results = []  # Stores the resulting array
        index_stack = deque([0])  # Deque to keep track of valid indices

        # Initial processing for the first k-1 elements
        for i in range(1, k - 1):
            # Maintain stack only for indices where nums[stack[-1]] == nums[i] - 1
            while index_stack and nums[index_stack[-1]] != (nums[i] - 1):
                index_stack.pop()
            index_stack.append(i)

        # Process the remaining elements
        for i in range(k - 1, len(nums)):
            # Maintain stack only for indices where nums[stack[-1]] == nums[i] - 1
            while index_stack and nums[index_stack[-1]] != (nums[i] - 1):
                index_stack.pop()
            index_stack.append(i)

            # If the stack size matches k, append the result; otherwise, append -1
            if len(index_stack) == k:
                results.append(nums[index_stack[-1]])
            else:
                results.append(-1)

            # Remove indices that fall out of the current window
            if index_stack[0] == (i - k + 1): 
                index_stack.popleft()

        return results
