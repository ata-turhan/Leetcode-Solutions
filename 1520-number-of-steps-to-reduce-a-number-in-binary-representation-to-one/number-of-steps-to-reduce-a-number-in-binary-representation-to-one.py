class Solution:
    def numSteps(self, s: str) -> int:
        """
        Finds the number of steps to reduce the binary string representation of a number to 1.
        
        :param s: str - The binary string representation of the number.
        :return: int - The number of steps required to reduce the number to 1.
        """
        steps = 0  # Initialize the count of steps
        num = int(s, 2)  # Convert the binary string to an integer
        
        # Loop until the number is greater than 1
        while num > 1:
            # If the number is odd, add 1
            if num & 1 == 1:
                num += 1
            else:
                # If the number is even, divide by 2
                num >>= 1
            steps += 1  # Increment the step count

        return steps  # Return the total number of steps

# Example usage:
# sol = Solution()
# print(sol.numSteps("1101"))  # Output: 6
# print(sol.numSteps("10"))    # Output: 1
# print(sol.numSteps("1"))     # Output: 0
