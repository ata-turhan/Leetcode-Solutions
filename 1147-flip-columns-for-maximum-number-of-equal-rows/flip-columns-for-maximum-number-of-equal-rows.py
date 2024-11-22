from typing import List
from collections import defaultdict

class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        # Dictionary to count unique row patterns
        row_pattern_counts = defaultdict(int)

        for row in matrix:
            # Generate a normalized pattern for the row
            # If the first element is 1, flip the row to start with 0
            normalized_pattern = tuple(cell ^ row[0] for cell in row)
            # Count the occurrence of this pattern
            row_pattern_counts[normalized_pattern] += 1

        # Return the maximum count of any pattern
        return max(row_pattern_counts.values())
