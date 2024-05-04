class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Initialize an empty string to store the result
        res = ""

        # Iterate through each character in the string
        for i in range(len(s)):
            # Check for both odd and even length palindromes centered at the current character
            for l, r in ((i,i), (i,i+1)):
                # Expand around the center to find the longest palindrome
                while l >= 0 and r < len(s) and s[l] == s[r]:
                    # Update the result if the current palindrome is longer
                    if (r - l + 1) > len(res):
                        res = s[l:r + 1]
                    # Expand the palindrome by moving the pointers
                    l -= 1
                    r += 1

        return res
