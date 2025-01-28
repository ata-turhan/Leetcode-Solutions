class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        directions = [
            [0, 1],
            [0, -1],
            [1, 0],
            [-1, 0]
        ]

        def dfs(r, c, visited):
            visited.add((r, c))
            catched_fish = grid[r][c]

            for dx, dy in directions:
                nr, nc = r + dx, c + dy
                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and (nr, nc) not in visited and grid[nr][nc] > 0:
                    catched_fish += dfs(nr, nc, visited)

            return catched_fish

        all_visited = set()
        max_catched_fish = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) not in all_visited and grid[i][j] > 0:
                    visited = set()
                    catched_fish = dfs(i, j, visited)
                    max_catched_fish = max(max_catched_fish, catched_fish)
                    all_visited |= visited

        return max_catched_fish
        