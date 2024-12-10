from collections import defaultdict
from typing import List

class Solution:
    def maximumLength(self, s: str) -> int:
        """
        Finds the length of the longest substring in the input string `s` 
        that consists of a single repeating character and occurs at least three times.

        :param s: Input string.
        :return: Length of the longest valid substring, or -1 if none exist.
        """
        # Dictionary to count occurrences of substrings
        substring_counts = defaultdict(int)
        
        # Generate all substrings and count their occurrences
        for start in range(len(s)):
            current_char = s[start]
            length = 0
            for end in range(start, len(s)):
                if s[end] == current_char:
                    length += 1
                    substring_counts[s[start:start+length]] += 1
                else:
                    break

        # Find substrings that occur at least three times
        frequent_substrings = [substr for substr, count in substring_counts.items() if count >= 3]
        
        # If no such substrings exist, return -1
        if not frequent_substrings:
            return -1
        
        # Find the longest substring among the frequent ones
        longest_substring = max(frequent_substrings, key=len)
        return len(longest_substring)
