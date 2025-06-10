from collections import Counter
from typing import List

class Solution:
    def maxDifference(self, s: str) -> int:
        char_frequencies = Counter(s)
        odd_frequencies = [count for count in char_frequencies.values() if count % 2 == 1]
        even_frequencies = [count for count in char_frequencies.values() if count % 2 == 0]

        if not odd_frequencies or not even_frequencies:
            return -1  # Return -1 if either set is missing to avoid invalid max-min

        max_odd = max(odd_frequencies)
        min_even = min(even_frequencies)
        
        return max_odd - min_even
