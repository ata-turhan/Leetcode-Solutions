from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        # Count occurrences of each character in the string
        char_counts = Counter(s)
        
        # Iterate through the string to find the first unique character
        for i, char in enumerate(s):
            if char_counts[char] == 1:
                # Return the index of the first unique character
                return i
        
        # If no unique character is found, return -1
        return -1
