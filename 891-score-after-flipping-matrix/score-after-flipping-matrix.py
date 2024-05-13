class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        grid = grid.copy()
        m, n = len(grid), len(grid[0])
        
        for i in range(m):
            if grid[i][0] == 0:
                for j in range(n):
                    grid[i][j] ^= 1

        for j in range(1, n):
            counts_1 = 0
            for i in range(m):
                counts_1 += grid[i][j]
            if counts_1 < m/2:
                for i in range(m):
                    grid[i][j] ^= 1

        res = 0
        for i in range(m):
            count = 0
            val = 0
            for j in range(n-1, -1, -1):
                val += grid[i][j] * 2**count
                count += 1
            res += val
            
        return res
        