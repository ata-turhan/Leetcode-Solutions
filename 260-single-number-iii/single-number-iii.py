from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        """
        Finds the two unique numbers in an array where every other number appears exactly twice.

        :param nums: List[int] - The input array of integers.
        :return: List[int] - A list containing the two unique numbers.
        """
        xor_all = 0  # XOR of all elements in nums

        # XOR all numbers to get the XOR of the two unique numbers
        for num in nums:
            xor_all ^= num

        # Find the rightmost set bit (lsb1) in xor_all
        lsb1 = xor_all & -xor_all

        res1, res2 = 0, 0  # Initialize the results for the two unique numbers

        # Divide the numbers into two groups and XOR within each group
        for num in nums:
            if num & lsb1:
                res1 ^= num  # XOR of one group
            else:
                res2 ^= num  # XOR of the other group

        return [res1, res2]  # Return the two unique numbers

# Example usage:
# sol = Solution()
# print(sol.singleNumber([1, 2, 1, 3, 2, 5]))  # Output: [3, 5]
