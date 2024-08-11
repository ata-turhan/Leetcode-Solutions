from typing import List

class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(i, j, visited):
            # Define the possible moves in the grid (right, down, left, up)
            moves = [
                [0, 1],
                [1, 0],
                [0, -1],
                [-1, 0]
            ]
            visited.add((i, j))

            # Explore all four possible directions
            for move in moves:
                ni, nj = i + move[0], j + move[1]
                if ni in range(ROWS) and nj in range(COLS) and (ni, nj) not in visited and grid[ni][nj] == 1:
                    # Perform DFS if the neighboring cell is within bounds, unvisited, and part of the island
                    dfs(ni, nj, visited)

        def count_islands():
            # Count the number of distinct islands in the grid
            count = 0
            visited = set()
            for i in range(ROWS):
                for j in range(COLS):
                    if grid[i][j] == 1 and (i, j) not in visited:
                        dfs(i, j, visited)
                        count += 1
            return count

        # Check the initial number of islands
        count = count_islands()
        if count != 1:
            return 0  # If there are no islands or multiple islands, return 0

        # Try removing each land cell and check the number of islands
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    grid[i][j] = 0  # Temporarily remove the land cell
                    count = count_islands()
                    if count != 1:
                        return 1  # If removing this cell disconnects the island, return 1
                    grid[i][j] = 1  # Restore the land cell

        return 2  # If no single cell removal can disconnect the island, return 2
