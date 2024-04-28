class Solution:
    def reverseBits(self, n: int) -> int:
        """
        Reverse the bits of a 32-bit unsigned integer.

        Args:
        - n: The input 32-bit unsigned integer.

        Returns:
        - int: The integer with reversed bits.
        """
        res = 0
        # Iterate 32 times to process each bit
        for _ in range(32):
            res <<= 1          # Left shift res to make space for the next bit
            res += n & 1       # Add the least significant bit of n to res
            n >>= 1            # Right shift n to process the next bit
        return res
