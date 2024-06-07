class Solution:
    def singleNumber(self, nums):
        """
        Finds the single number that appears only once in a list where every other number appears three times.
        
        :param nums: List[int] - The input list of integers.
        :return: int - The single number that appears only once.
        """
        ans = 0  # Initialize the result to 0

        # Iterate through each bit position (0 to 31)
        for i in range(32):
            bit_sum = 0  # Initialize the sum of bits at position i

            # Iterate through each number in the list
            for num in nums:
                # Convert the number to two's complement representation to handle large test cases
                if num < 0:
                    num = num & (2**32 - 1)
                # Add the bit at position i to the bit_sum
                bit_sum += (num >> i) & 1

            # Take the remainder of bit_sum divided by 3 (to handle numbers appearing three times)
            bit_sum %= 3
            # Set the bit at position i in the result if bit_sum is 1
            ans |= bit_sum << i

        # Convert the result back to two's complement representation if it's negative
        if ans >= 2**31:
            ans -= 2**32

        return ans  # Return the single number

# Example usage:
# sol = Solution()
# print(sol.singleNumber([2, 2, 3, 2]))  # Output: 3
# print(sol.singleNumber([0, 1, 0, 1, 0, 1, 99]))  # Output: 99
