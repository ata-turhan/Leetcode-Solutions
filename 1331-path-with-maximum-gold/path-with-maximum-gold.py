class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        moves = [
            [0, 1],
            [1, 0],
            [0, -1],
            [-1, 0]
        ]
        max_val = 0
       
        def dfs(i, j, path):
            val = grid[i][j]

            max_remaining = 0
            path.add((i, j))
            for move in moves:
                ni, nj = i + move[0], j + move[1]
                if ni in range(len(grid)) and nj in range(len(grid[0])) and grid[ni][nj] != 0 and (ni, nj) not in path:
                    max_remaining = max(max_remaining, dfs(ni, nj, path))
            path.remove((i, j))

            return val + max_remaining 

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != 0:
                    val = dfs(i, j, set())
                    max_val = max(max_val, val)
        return max_val
        