from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        """
        Calculates the length of the longest palindrome that can be built with the given string.
        
        :param s: str - The input string.
        :return: int - The length of the longest possible palindrome.
        """
        has_odd = False  # Flag to check if there's any character with an odd count
        char_count = Counter(s)  # Count the occurrences of each character in the string
        length = 0  # Initialize the length of the longest palindrome

        # Iterate over the character counts
        for count in char_count.values():
            if count % 2 == 1:  # If the count is odd
                has_odd = True  # Set the odd flag to True
            length += (count // 2) * 2  # Add the largest even number <= count to the length

        # If there's any odd count, add 1 to the length to place one odd character in the middle
        return length + has_odd

# Example usage:
# sol = Solution()
# print(sol.longestPalindrome("abccccdd"))  # Output: 7
# print(sol.longestPalindrome("a"))         # Output: 1
# print(sol.longestPalindrome("bb"))        # Output: 2
