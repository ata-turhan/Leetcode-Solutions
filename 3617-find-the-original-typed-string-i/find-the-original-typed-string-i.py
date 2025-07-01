from typing import List

class Solution:
    def possibleStringCount(self, word: str) -> int:
        """
        Count the total number of substrings where adjacent characters are the same.
        For each consecutive sequence of identical characters of length `n`, 
        there are (n - 1) such substrings.
        """
        total_count: int = 1  # Start with 1 for the first character
        run_length: int = 1

        for i in range(1, len(word)):
            if word[i] == word[i - 1]:
                run_length += 1
            else:
                total_count += run_length - 1
                run_length = 1

        total_count += run_length - 1  # Account for the last run

        return total_count
