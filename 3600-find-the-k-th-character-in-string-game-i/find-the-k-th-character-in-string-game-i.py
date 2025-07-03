from typing import List

class Solution:
    def kthCharacter(self, k: int) -> str:
        """
        Generate a word by repeatedly appending a character-shifted version of the current word,
        and return the k-th character (1-indexed) of the final word.
        Each character is shifted forward by 1 in the alphabet, wrapping around from 'z' to 'a'.
        """
        def transform_word(word: List[str]) -> List[str]:
            """Return the original word followed by each character shifted forward by 1."""
            shifted = [chr((ord(c) - ord('a') + 1) % 26 + ord('a')) for c in word]
            return word + shifted

        word: List[str] = ['a']

        while len(word) < k:
            word = transform_word(word)

        return word[k - 1]
