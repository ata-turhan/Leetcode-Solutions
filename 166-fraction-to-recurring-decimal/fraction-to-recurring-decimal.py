class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"
        
        result = []
        
        # Determine the sign of the result
        if (numerator < 0) ^ (denominator < 0):
            result.append("-")
        
        # Convert both numbers to positive for ease of calculation
        numerator, denominator = abs(numerator), abs(denominator)
        
        # Append the integer part
        integer_part = numerator // denominator
        result.append(str(integer_part))
        
        # Calculate the remainder
        remainder = numerator % denominator
        if remainder == 0:
            return "".join(result)
        
        result.append(".")
        
        # Dictionary to store remainders and their corresponding indices in the result
        remainder_map = {}
        
        while remainder != 0:
            if remainder in remainder_map:
                result.insert(remainder_map[remainder], "(")
                result.append(")")
                break
            
            remainder_map[remainder] = len(result)
            remainder *= 10
            result.append(str(remainder // denominator))
            remainder %= denominator
        
        return "".join(result)

# Example usage:
# sol = Solution()
# print(sol.fractionToDecimal(1, 2))  # Output: "0.5"
# print(sol.fractionToDecimal(2, 1))  # Output: "2"
# print(sol.fractionToDecimal(4, 333))  # Output: "0.(012)"
