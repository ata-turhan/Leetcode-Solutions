class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        diffs = [ abs(ord(sc) - ord(tc)) for sc, tc in zip(s, t)]
        max_len = 0
        cost = 0
        l = 0
        for r in range(len(diffs)):
            cost += diffs[r]
            while cost > maxCost:
                cost -= diffs[l]
                l += 1
            max_len = max(max_len, r-l+1)

        return max_len
        