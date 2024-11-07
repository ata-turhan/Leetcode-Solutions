from typing import List

class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        # Find the maximum number of bits needed based on the largest candidate
        largest_candidate = max(candidates)
        max_bit_length = len(bin(largest_candidate)) - 2  # Exclude '0b' from binary length
        highest_bitwise_count = 0

        # Check each bit position for the maximum count of '1's across candidates
        for bit_position in range(max_bit_length):
            bit_count = 0
            for num in candidates:
                # Check if the current bit position is set to '1'
                if (num >> bit_position) & 1:
                    bit_count += 1
            # Update the highest count of '1's in any bit position
            highest_bitwise_count = max(highest_bitwise_count, bit_count)

        return highest_bitwise_count
