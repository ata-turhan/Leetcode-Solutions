from typing import List
from collections import defaultdict

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        """
        Partitions the string into as many parts as possible 
        so that each letter appears in at most one part.
        Returns the list of lengths of each partition.
        """
        last_occurrence = {char: i for i, char in enumerate(s)}
        result: List[int] = []
        start, end = 0, 0

        for i, char in enumerate(s):
            end = max(end, last_occurrence[char])
            if i == end:
                result.append(end - start + 1)
                start = i + 1

        return result
