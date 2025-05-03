from typing import List

class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        """
        Finds the minimum number of rotations needed to make all the values in either the top
        or the bottom row equal. If impossible, returns -1.
        """
        def min_swaps(target: int) -> int:
            top_swaps = bottom_swaps = 0
            for top, bottom in zip(tops, bottoms):
                if top != target and bottom != target:
                    return float('inf')  # Impossible to align this domino
                if top != target:
                    top_swaps += 1
                if bottom != target:
                    bottom_swaps += 1
            return min(top_swaps, bottom_swaps)

        candidates = {tops[0], bottoms[0]}
        min_rotations = min(min_swaps(c) for c in candidates)

        return min_rotations if min_rotations != float('inf') else -1
