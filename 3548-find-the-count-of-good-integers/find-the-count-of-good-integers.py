from collections import Counter
from math import factorial

class Solution:
    def countGoodIntegers(self, length: int, divisor: int) -> int:
        half_length = (length + 1) // 2  # Length of half the palindrome
        total_count = 0
        seen_palindromes = set()
        
        # Iterate through all possible half-palindromes
        for half_palindrome in range(10 ** (half_length - 1), 10 ** half_length):
            # Construct the full palindrome by mirroring the half
            full_palindrome = str(half_palindrome) + str(half_palindrome)[::-1][length % 2:]
            
            # Create a key for unique checking by sorting the digits
            sorted_key = ''.join(sorted(full_palindrome))
            
            # Check divisibility and uniqueness
            if int(full_palindrome) % divisor == 0 and sorted_key not in seen_palindromes:
                seen_palindromes.add(sorted_key)
                
                # Calculate permutations of digits accounting for duplicates
                digit_count = Counter(full_palindrome)
                permutation_count = (length - digit_count['0']) * factorial(length - 1)
                for count in digit_count.values():
                    permutation_count //= factorial(count)
                
                total_count += permutation_count
        
        return total_count
