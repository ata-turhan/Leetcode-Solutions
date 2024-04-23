class Solution:
    def reverse(self, x: int) -> int:
        """
        Reverses the digits of a 32-bit signed integer.

        Args:
        - x: Integer to be reversed

        Returns:
        - Reversed integer or 0 if the result overflows
        """
        INT_MIN, INT_MAX = -2**31, 2**31 - 1

        # Handle negative numbers
        sign = -1 if x < 0 else 1
        x = abs(x)

        # Reverse the digits of the integer
        rev_x = 0
        while x != 0:
            digit = x % 10
            # Check for overflow before adding the next digit
            if sign == 1 and rev_x > (INT_MAX - digit) // 10:
                return 0
            elif sign == -1 and rev_x > (-INT_MIN - digit) // 10:
                return 0
            rev_x = rev_x * 10 + digit
            x //= 10

        # Apply sign to the reversed integer
        rev_x *= sign
 
        return rev_x
