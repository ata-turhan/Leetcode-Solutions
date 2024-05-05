from collections import Counter

class Solution:
    def minAnagramLength(self, s: str) -> int:
        # Define a function to check if a given length k is valid
        def is_valid(k):
            # Initialize a counter for the first substring of length k
            prev = Counter(s[:k])
            # Iterate through the string with step k
            for i in range(k, len(s), k):
                # Create a counter for the current substring of length k
                cur = Counter(s[i:i+k])
                # Check if the current substring is an anagram of the previous one
                if prev != cur:
                    return False
                prev = cur
            return True
        
        # Count the frequency of each character in the string
        char_freq = Counter(s)
        # Get the minimum frequency of any character
        min_freq = min(char_freq.values())
        # Determine the minimum possible length of the anagram
        min_length = len(s) // min_freq
        
        # Check all possible lengths from min_length to len(s)
        for length in range(min_length, len(s)):
            # Check if the length is a divisor of len(s) and is valid
            if len(s) % length == 0 and is_valid(length):
                return length
        
        return len(s)
