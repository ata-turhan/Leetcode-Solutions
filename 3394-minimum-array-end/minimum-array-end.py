class Solution:
    def minEnd(self, n: int, x: int) -> int:
        remaining_bits = n - 1  # Start with n - 1 as the remaining bits to process
        result = x              # Initialize result with the value of x
        current_bit = 1         # Current bit position to check

        # Iterate while there are bits left to process in n
        while remaining_bits > 0:
            # If the current bit in x is 0, we may set it in the result based on remaining_bits
            if (current_bit & x) == 0:
                # If the least significant bit in remaining_bits is 1, set the current bit in result
                result |= (remaining_bits & 1) * current_bit
                # Shift remaining_bits to the right for the next bit check
                remaining_bits >>= 1
            
            # Move to the next bit position
            current_bit <<= 1

        return result
