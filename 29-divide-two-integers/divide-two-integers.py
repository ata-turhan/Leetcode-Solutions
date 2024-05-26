class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Constants for 32-bit signed integer range.
        MAX_INT = 2**31 - 1
        MIN_INT = -2**31
        
        # Handle division by zero case.
        if divisor == 0:
            raise ValueError("Division by zero is not allowed.")
        
        # Handle overflow cases.
        if dividend == MIN_INT and divisor == -1:
            return MAX_INT
        
        # Determine the sign of the quotient.
        negative = (dividend < 0) != (divisor < 0)
        
        # Work with positive values for simplicity.
        dividend, divisor = abs(dividend), abs(divisor)
        
        quotient = 0
        # Shift the divisor until it is larger than the dividend.
        while dividend >= divisor:
            temp, multiple = divisor, 1
            while dividend >= (temp << 1):
                temp <<= 1
                multiple <<= 1
            # Subtract the largest shifted divisor from the dividend.
            dividend -= temp
            quotient += multiple
        
        # Apply the sign to the quotient.
        if negative:
            quotient = -quotient
        
        # Ensure the quotient is within the 32-bit signed integer range.
        return min(max(MIN_INT, quotient), MAX_INT)

# Example usage:
# sol = Solution()
# print(sol.divide(10, 3))  # Output: 3
# print(sol.divide(7, -3))  # Output: -2
