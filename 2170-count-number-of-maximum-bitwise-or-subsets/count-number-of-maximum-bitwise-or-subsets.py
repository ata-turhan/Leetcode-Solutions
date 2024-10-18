from functools import reduce
from typing import List

class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        # Calculate the maximum OR value that can be achieved by OR-ing all numbers in the list
        max_or_val = reduce(lambda a, b: a | b, nums)
        
        # Recursive function to find the number of subsets that achieve the max OR value
        def find_max_subsets(index: int, current_or: int) -> int:
            # Base case: If we've processed all elements, check if current OR matches the max OR
            if index == len(nums):
                return 1 if current_or == max_or_val else 0

            # Option 1: Include nums[index] in the subset
            include = find_max_subsets(index + 1, current_or | nums[index])

            # Option 2: Exclude nums[index] from the subset
            exclude = find_max_subsets(index + 1, current_or)

            # Return the sum of both options
            return include + exclude

        # Start the recursion with index 0 and an initial OR value of 0
        return find_max_subsets(0, 0)
