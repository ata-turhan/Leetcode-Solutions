class Solution:
    def hammingWeight(self, n: int) -> int:
        """
        Count the number of '1' bits in the binary representation of the given integer.

        Args:
        - n: An integer for which the Hamming weight needs to be calculated.

        Returns:
        - int: The number of '1' bits in the binary representation of n.
        """
        count = 0
        # Loop until n becomes 0
        while n > 0:
            # Clear the least significant '1' bit in n and increment the count
            n &= n - 1
            count += 1
        return count
