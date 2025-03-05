class Solution:
    def coloredCells(self, n: int) -> int:
        result = 1

        for i in range(1, n):
            result += i * 4

        return result
        