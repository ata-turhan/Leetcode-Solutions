class Solution:
    def trailingZeroes(self, n: int) -> int:
        """
        Returns the number of trailing zeroes in n!.
        
        :param n: int - the number for which to calculate the factorial trailing zeroes
        :return: int - the number of trailing zeroes in n!
        """
        count = 0
        power_of_five = 5
        
        # Count the number of multiples of 5, 25, 125, etc.
        while n >= power_of_five:
            count += n // power_of_five
            power_of_five *= 5
        
        return count

# Example usage:
# sol = Solution()
# print(sol.trailingZeroes(100))  # Output: 24
