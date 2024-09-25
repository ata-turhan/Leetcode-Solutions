from typing import List
from collections import defaultdict

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        # Dictionary to store the frequency of each prefix
        prefix_count = defaultdict(int)

        # First pass: count the occurrences of each prefix across all words
        for word in words:
            current_prefix = ""
            for char in word:
                current_prefix += char
                prefix_count[current_prefix] += 1

        # Second pass: calculate the prefix sum for each word
        result = []
        for word in words:
            current_prefix = ""
            score = 0
            # Sum the counts of all prefixes for the current word
            for char in word:
                current_prefix += char
                score += prefix_count[current_prefix]
            result.append(score)

        return result
