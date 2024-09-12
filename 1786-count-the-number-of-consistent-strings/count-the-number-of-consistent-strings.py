from typing import List

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        # Convert the allowed characters to a set for efficient lookups
        allowed_letters: set = set(allowed)
        consistent_strs: int = 0

        # Iterate over each word in the list
        for word in words:
            # Check if every letter in the word is in the allowed set
            for letter in word:
                if letter not in allowed_letters:
                    break  # If any letter is not allowed, break and move to the next word
            else:
                consistent_strs += 1  # If no break occurred, the word is consistent

        return consistent_strs
