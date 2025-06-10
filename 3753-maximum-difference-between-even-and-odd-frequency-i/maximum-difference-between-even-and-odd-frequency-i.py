class Solution:
    def maxDifference(self, s: str) -> int:
        frequencies = Counter(s)
        a1 = max(val for val in frequencies.values() if val % 2 == 1)
        a2 = min(val for val in frequencies.values() if val % 2 == 0)
        return a1 - a2
        