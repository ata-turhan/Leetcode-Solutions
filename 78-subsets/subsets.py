from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Initialize an empty list to store subsets
        subsets = []
        # Iterate through all possible combinations of elements using their binary representation
        for i in range(2**len(nums)):
            # Initialize a new subset
            new_subset = []
            count = 0
            # Check each bit of the binary representation
            while 2**count <= i:
                # If the bit is set, add the corresponding element to the subset
                if i & (1<<count) > 0:
                    new_subset.append(nums[count])
                count += 1
            # Add the subset to the list of subsets
            subsets.append(new_subset)
        return subsets
