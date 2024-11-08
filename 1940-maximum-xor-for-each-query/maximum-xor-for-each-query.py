from typing import List
from functools import reduce

class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        # Calculate the XOR of all numbers in nums
        total_xor = reduce(lambda a, b: a ^ b, nums)
        results = []

        # Iterate from the last index to the first
        for i in range(len(nums) - 1, -1, -1):
            # Initialize k to hold the maximum XOR result for the current total_xor
            max_xor = 0
            for bit_position in range(maximumBit):
                # Set each bit in k to the opposite of the corresponding bit in total_xor
                max_xor |= (((total_xor >> bit_position) & 1) ^ 1) << bit_position

            # Append the current max_xor result to the results list
            results.append(max_xor)

            # Update total_xor by removing the effect of nums[i]
            total_xor ^= nums[i]

        return results
