from typing import List
from functools import reduce

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        # Calculate the bitwise XOR of all elements in the nums list
        total_xor = reduce(lambda a, b: a ^ b, nums)
        # Calculate the desired result by XORing the total_xor with the target value k
        target_xor = total_xor ^ k
        
        # Initialize a counter to track the number of set bits in the target_xor
        set_bits_count = 0
        # Iterate over each bit in the target_xor using Brian Kernighan's algorithm
        while target_xor > 0:
            # Reduce the target_xor by unsetting the rightmost set bit
            target_xor &= target_xor - 1
            # Increment the count of set bits
            set_bits_count += 1
        
        # Return the total count of set bits in the target_xor
        return set_bits_count
