from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Finds two numbers in the list that add up to the target.

        Args:
        - nums: List of integers
        - target: Target sum

        Returns:
        - List containing the indices of the two numbers that add up to the target
        """
        hashmap = {}  # Initialize a hashmap to store number-frequency pairs
        for i, num in enumerate(nums):
            complement = target - num  # Calculate the complement needed to reach the target
            if complement in hashmap:
                # If the complement exists in the hashmap, return the indices of the two numbers
                return [hashmap[complement], i]
            # Otherwise, store the current number and its index in the hashmap
            hashmap[num] = i
