from typing import List

class Solution:
    def __init__(self):
        self.dp = [[-1] * 11 for _ in range(1001)]

    def solve(self, idx: int, prev: int, rows: int, cols: int, cnt: List[List[int]]) -> int:
        if idx >= cols:
            return 0
        if self.dp[idx][prev] != -1:
            return self.dp[idx][prev]
        ans = float('inf')
        for j in range(10):
            if j != prev:
                ans = min(ans, rows - cnt[idx][j] + self.solve(idx + 1, j, rows, cols, cnt))
        self.dp[idx][prev] = ans
        return ans

    def minimumOperations(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        cnt = [[0] * 10 for _ in range(m)]
        for c in range(m):
            for r in range(n):
                cnt[c][grid[r][c]] += 1
        ans = self.solve(0, 10, n, m, cnt)
        return ans
