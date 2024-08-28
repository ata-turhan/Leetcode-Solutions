class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        directions = [
            [0, 1],
            [0, -1],
            [-1, 0],
            [1, 0],
        ]
        
        def dfs(grid, rows, cols, i, j, visited):
            visited.add((i, j))
            for di, dj in directions:
                new_i, new_j = i + di, j + dj
                if new_i in range(rows1) and new_j in range(cols1) and grid[new_i][new_j] == 1 and (new_i, new_j) not in visited:
                    dfs(grid, rows, cols, new_i, new_j, visited)

        rows1, cols1 = len(grid1), len(grid1[0])
        grid1_sub_islands = []
        all_visited1 = set()
        for i in range(rows1):
            for j in range(cols1):
                if grid1[i][j] == 1 and (i, j) not in all_visited1:
                    visited = set()
                    dfs(grid1, rows1, cols1, i, j, visited)
                    grid1_sub_islands.append(visited)
                    all_visited1 |= visited

        rows2, cols2 = len(grid2), len(grid2[0])
        grid2_sub_islands = []
        all_visited = set()
        for i in range(rows2):
            for j in range(cols2):
                if grid2[i][j] == 1 and (i, j) not in all_visited:
                    visited = set()
                    dfs(grid2, rows2, cols2, i, j, visited)
                    grid2_sub_islands.append(visited)
                    all_visited |= visited

        sub_island_count = 0
        for island2 in grid2_sub_islands:
            if len(island2 & all_visited1) >= len(island2):
                sub_island_count += 1

        return sub_island_count
            