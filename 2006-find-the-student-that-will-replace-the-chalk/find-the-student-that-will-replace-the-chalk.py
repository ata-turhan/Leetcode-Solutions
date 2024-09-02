class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        total_chalk = sum(chalk)
        k %= total_chalk
        used = 0
        for i, c in enumerate(chalk):
            used += c
            if k < used:
                return i