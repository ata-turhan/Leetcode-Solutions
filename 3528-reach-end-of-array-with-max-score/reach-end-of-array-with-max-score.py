from typing import List

class Solution:
    def findMaximumScore(self, nums: List[int]) -> int:
        max_score: int = 0
        index_stack: List[int] = [0]  # Stack to hold indexes, starting with the first element

        # Iterate through nums to build the stack with increasing elements
        for i in range(1, len(nums) - 1):
            if nums[i] > nums[index_stack[-1]]:
                index_stack.append(i)

        # Append the last index to the stack
        index_stack.append(len(nums) - 1)

        # Calculate the score by multiplying each valid range with its corresponding element
        for i in range(1, len(index_stack)):
            max_score += nums[index_stack[i - 1]] * (index_stack[i] - index_stack[i - 1])

        return max_score
