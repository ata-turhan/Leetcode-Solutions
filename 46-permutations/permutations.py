from typing import List
from itertools import permutations
from collections import deque

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # Using built-in permutations function
        return permutations(nums)

    # Another solution using recursion and backtracking
    def permute_v2(self, nums: List[int]) -> List[List[int]]:
        # Base case: if the list has only one element, return a list containing that element
        if len(nums) == 1:
            return [nums.copy()]
        
        # Initialize a list to store permutations
        res = []
        nums = deque(nums)
        # Iterate through each element in the list
        for _ in range(len(nums)):
            # Remove the first element from the list
            n = nums.popleft()
            # Recursively generate permutations for the remaining elements
            perms = self.permute(nums)

            # Append the current element to each permutation
            for p in perms:
                p.append(n)
            
            # Extend the result list with the permutations
            res.extend(perms)
            # Add the current element back to the end of the list
            nums.append(n)
        
        return res
