class Solution:
    def convertToBase7(self, num: int) -> str:
        """
        Converts an integer to its base-7 representation.
        
        :param num: int - The input integer.
        :return: str - The base-7 representation of the input integer.
        """
        if num == 0:
            return "0"

        res = []  # List to store the digits of the base-7 number
        is_negative = num < 0  # Check if the number is negative
        num = abs(num)  # Take the absolute value of the number

        # Convert the number to base-7
        while num > 0:
            remainder = num % 7  # Get the remainder when num is divided by 7
            res.append(remainder)  # Append the remainder to the result list
            num //= 7  # Update num to the quotient of num divided by 7

        # Convert the list of digits to a string and reverse the order
        base7num = "".join(map(str, res[::-1]))

        # Add a negative sign if the original number was negative
        if is_negative:
            base7num = "-" + base7num

        return base7num  # Return the base-7 representation

# Example usage:
# sol = Solution()
# print(sol.convertToBase7(100))  # Output: "202"
# print(sol.convertToBase7(-7))   # Output: "-10"
# print(sol.convertToBase7(0))    # Output: "0"
