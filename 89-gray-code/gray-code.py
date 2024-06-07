from typing import List

class Solution:
    def grayCode(self, n: int) -> List[int]:
        """
        Generates the sequence of Gray codes for a given number of bits.
        
        :param n: int - The number of bits.
        :return: List[int] - The sequence of Gray codes.
        """
        if n == 1:
            return [0, 1]

        res = [0, 1]  # Initialize the result with Gray codes for 1 bit

        # Generate Gray codes for each number of bits from 2 to n
        for i in range(2, n + 1):
            # Append mirrored and prefixed Gray codes to the result
            res += [2**(i - 1) + num for num in reversed(res)]

        return res

# Example usage:
# sol = Solution()
# print(sol.grayCode(2))  # Output: [0, 1, 3, 2]
# print(sol.grayCode(3))  # Output: [0, 1, 3, 2, 6, 7, 5, 4]
