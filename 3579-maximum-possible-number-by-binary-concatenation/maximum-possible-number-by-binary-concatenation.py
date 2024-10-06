from itertools import permutations
from typing import List

class Solution:
    def maxGoodNumber(self, nums: List[int]) -> int:
        # Convert each number to its binary string representation without the '0b' prefix
        binary_representations = [bin(num)[2:] for num in nums]
        
        max_value = 0
        
        # Generate all possible permutations of the binary representations
        for perm in permutations(binary_representations):
            # Concatenate the binary strings from the current permutation
            concatenated_binary = ''.join(perm)
            # Convert the concatenated binary string to an integer
            current_value = int(concatenated_binary, 2)
            # Update the maximum value encountered
            max_value = max(max_value, current_value)
        
        return max_value
