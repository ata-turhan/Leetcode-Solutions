import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Check if a string is a palindrome, ignoring non-alphanumeric characters
        and considering case-insensitive.

        Args:
        - s: Input string

        Returns:
        - True if the string is a palindrome, False otherwise
        """
        # Remove all non-alphanumeric characters using regular expression
        s = re.sub("[^A-Za-z0-9]", "", s)
        
        # Convert the string to lowercase
        s = s.lower()
        
        # Check if the modified string is equal to its reverse
        return s == s[::-1]
