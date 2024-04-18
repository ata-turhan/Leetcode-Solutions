class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        moves = [
            [0, 1],
            [1, 0],
            [0, -1],
            [-1, 0],
        ]
        m = len(grid)
        n = len(grid[0])
        def dfs(visited, i , j):
            res = 0
            for move in moves:
                ni, nj = i + move[0], j + move[1]
                if ni not in range(m) or nj not in range(n) or grid[ni][nj] == 0:
                    res += 1
            visited.add((i, j))
            for move in moves:
                ni, nj = i + move[0], j + move[1]
                if ni in range(m) and nj in range(n) and (ni, nj) not in visited and grid[ni][nj] == 1:
                    res += dfs(visited, ni, nj)
            return res



        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return dfs(visited, i, j)
        