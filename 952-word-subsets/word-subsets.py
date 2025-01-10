from collections import defaultdict, Counter
from typing import List

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        """
        Find all words in words1 that are universal to words2.

        :param words1: List[str] - The first list of words.
        :param words2: List[str] - The second list of words.
        :return: List[str] - Words from words1 that are universal to words2.
        """
        # Combine the maximum counts of each letter across all words in words2
        combined_letter_counts = defaultdict(int)
        for word in words2:
            letter_counts = Counter(word)
            for letter, count in letter_counts.items():
                combined_letter_counts[letter] = max(combined_letter_counts[letter], count)

        # Convert to Counter for easy comparison
        combined_letter_counts = Counter(combined_letter_counts)

        # Find words in words1 that satisfy the universal condition
        universal_words = []
        for word in words1:
            letter_counts = Counter(word)
            if letter_counts >= combined_letter_counts:  # Check if word contains required letter counts
                universal_words.append(word)
        
        return universal_words
