from typing import Iterator

class Solution:
    def kMirror(self, k: int, n: int) -> int:
        """
        Return the sum of the first n positive integers that are palindromic
        in both base-10 and base-k.
        """

        def is_palindrome(s: str) -> bool:
            # Check if string s is a palindrome
            return s == s[::-1]

        def to_base_k(x: int, k: int) -> str:
            # Convert integer x to its base-k representation (no leading zeros)
            if x == 0:
                return "0"
            digits = []
            while x > 0:
                digits.append(str(x % k))
                x //= k
            return ''.join(reversed(digits))

        def generate_palindromes() -> Iterator[int]:
            """
            Generate all base-10 palindromes in ascending order.
            Handles both odd and even digit lengths.
            """
            length = 1
            while True:
                half_len = (length + 1) // 2
                start = 10**(half_len - 1)
                end = 10**half_len
                # Special case for length == 1: start from 1
                if length == 1:
                    start = 1

                for half in range(start, end):
                    s = str(half)
                    if length % 2 == 1:
                        # Odd-length palindrome: mirror excluding middle digit
                        pal = int(s + s[-2::-1])
                    else:
                        # Even-length palindrome: full mirror
                        pal = int(s + s[::-1])
                    yield pal

                length += 1  # Increase digit length for next batch

        total = 0
        count = 0
        # Iterate palindromes in ascending order
        for p in generate_palindromes():
            # Only consider if it is also palindromic in base-k
            if is_palindrome(to_base_k(p, k)):
                total += p
                count += 1
                if count == n:
                    break

        return total
