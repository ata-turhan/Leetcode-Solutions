class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        """
        Computes the bitwise AND of all numbers in the range [m, n].
        
        :param m: int - The starting integer of the range.
        :param n: int - The ending integer of the range.
        :return: int - The bitwise AND of all numbers in the range.
        """
        shift = 0  # Initialize the shift counter
        
        # Find the common 1-bits by shifting m and n to the right until they are equal
        while m < n:
            m >>= 1  # Shift m to the right
            n >>= 1  # Shift n to the right
            shift += 1  # Increment the shift counter
        
        # Shift the common bits back to their original position
        return m << shift

# Example usage:
# sol = Solution()
# print(sol.rangeBitwiseAnd(5, 7))  # Output: 4
# print(sol.rangeBitwiseAnd(0, 1))  # Output: 0
