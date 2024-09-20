from typing import List

class Solution:
    def shortestPalindrome(self, s: str) -> str:
        # Edge case: if the string is empty, return it as is
        if not s:
            return s

        # Reverse the original string
        reversed_s: str = s[::-1]

        # Concatenate the original string, a separator, and the reversed string
        concatenated_s: str = s + '#' + reversed_s
        n: int = len(concatenated_s)

        # Initialize the LPS (Longest Prefix Suffix) array
        lps: List[int] = [0] * n

        # Build the LPS array for concatenated_s
        for i in range(1, n):
            length: int = lps[i - 1]
            while length > 0 and concatenated_s[i] != concatenated_s[length]:
                length = lps[length - 1]
            if concatenated_s[i] == concatenated_s[length]:
                length += 1
            lps[i] = length

        # Calculate the substring from the reversed string that needs to be added
        # This is the portion of the reverse string that isn't part of the palindrome
        to_add: str = reversed_s[:len(s) - lps[-1]]

        # Return the shortest palindrome by adding the necessary part of the reversed string to the original string
        return to_add + s
