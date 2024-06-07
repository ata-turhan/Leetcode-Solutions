from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        """
        Counts the number of 1's in the binary representation of each number from 0 to n.
        
        :param n: int - The upper limit of the range.
        :return: List[int] - A list containing the count of 1's for each number from 0 to n.
        """
        if n == 0:
            return [0]
        if n == 1:
            return [0, 1]
        
        bits_count = [0] * (n + 1)  # Initialize the result list with zeros
        bits_count[0] = 0
        bits_count[1] = 1
        c = 2  # Initialize the variable to track the current power of 2
        
        for i in range(2, n + 1):
            if i == c:
                c *= 2  # Update c to the next power of 2
            bits_count[i] = bits_count[i - (c // 2)] + 1  # Compute the count of 1's

        return bits_count

# Example usage:
# sol = Solution()
# print(sol.countBits(2))  # Output: [0, 1, 1]
# print(sol.countBits(5))  # Output: [0, 1, 1, 2, 1, 2]
