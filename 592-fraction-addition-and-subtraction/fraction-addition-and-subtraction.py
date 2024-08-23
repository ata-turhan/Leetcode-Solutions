from math import gcd
from functools import reduce

class Solution:
    @staticmethod
    def lcm(a, b):
        # Calculate the Least Common Multiple (LCM) using the GCD
        return a * b // gcd(a, b)

    def fractionAddition(self, expression: str) -> str:
        fractions = []
        i = 0
        
        # Parse the expression to extract each fraction
        while i < len(expression):
            sign = 1
            # Handle signs ('+' or '-')
            if expression[i] == '-':
                sign = -1
                i += 1
            elif expression[i] == '+':
                i += 1
            
            # Extract numerator
            j = i
            while expression[j] != '/':
                j += 1
            numerator = int(expression[i:j])
            
            # Extract denominator
            i = j + 1
            j = i
            while j < len(expression) and expression[j].isdigit():
                j += 1
            denominator = int(expression[i:j])
            
            # Store the fraction with its sign
            fractions.append((sign * numerator, denominator))
            i = j
        
        # Find the Least Common Multiple (LCM) of all denominators to have a common denominator
        common_denom = reduce(lcm, (denom for _, denom in fractions))
        
        # Compute the sum of numerators after adjusting to the common denominator
        numerator_sum = sum(numerator * (common_denom // denom) for numerator, denom in fractions)
        
        # Simplify the resulting fraction by dividing both the numerator and denominator by their GCD
        common_divisor = gcd(abs(numerator_sum), common_denom)
        simplified_numerator = numerator_sum // common_divisor
        simplified_denominator = common_denom // common_divisor
        
        # Return the simplified fraction as a string
        return f"{simplified_numerator}/{simplified_denominator}"
