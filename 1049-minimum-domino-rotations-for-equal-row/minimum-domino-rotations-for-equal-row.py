class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        candidates = set([tops[0], bottoms[0]])

        for top, bottom in zip(tops, bottoms):
            candidates &= set([top, bottom])

        if not candidates:
            return -1

        candidate = candidates.pop()
        top_change = sum(candidate != top for top in tops)
        bottom_change = sum(candidate != bottom for bottom in bottoms)
        min_swap = min(top_change, bottom_change)


        if len(candidates) == 1:
            candidate = candidates.pop()
            top_change = sum(candidate != top for top in tops)
            bottom_change = sum(candidate != bottom for bottom in bottoms)
            min_swap = min(min_swap, top_change, bottom_change)

        return min_swap



        return 0
        