from collections import Counter
from typing import Dict

class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        """
        Return the minimum number of deletions to make `word` k-special,
        i.e., max frequency difference <= k across all characters.
        """
        freq: Dict[str, int] = Counter(word)
        # List of all character frequencies
        counts = list(freq.values())
        # If there's at most one distinct character, no deletions needed
        if len(counts) <= 1:
            return 0

        min_deletions = float('inf')
        # Try each frequency as the smallest frequency x in the final string
        for x in counts:
            deletions = 0
            # For each character frequency y, compute deletions
            for y in counts:
                if y < x:
                    # Must delete all occurrences of characters below x
                    deletions += y
                elif y > x + k:
                    # Must delete down to x + k for characters above x + k
                    deletions += y - (x + k)
                # Otherwise, no deletion needed

            # Track the minimal deletions across all x
            min_deletions = min(min_deletions, deletions)

        return min_deletions
