from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Checks if two strings are anagrams.

        Args:
        - s: First string
        - t: Second string

        Returns:
        - True if s and t are anagrams, False otherwise
        """
        # Construct dictionaries of character counts for both strings
        s_count = Counter(s)
        t_count = Counter(t)
        
        # Compare the dictionaries for equality
        return s_count == t_count
