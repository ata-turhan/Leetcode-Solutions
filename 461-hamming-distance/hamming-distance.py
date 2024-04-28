class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        """
        Calculate the Hamming distance between two integers.

        Args:
        - x: The first integer.
        - y: The second integer.

        Returns:
        - int: The Hamming distance between x and y, which is the number of differing bits
               in their binary representations.
        """
        # Calculate the bitwise XOR of x and y to find differing bits
        num = x ^ y
        count = 0
        # Count the number of '1' bits in the binary representation of num
        while num > 0:
            num &= num - 1  # Clear the least significant '1' bit in num
            count += 1      # Increment the count for each cleared bit
        return count
