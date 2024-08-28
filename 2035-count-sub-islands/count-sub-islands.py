from typing import List

class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        # Define possible directions for DFS exploration: right, left, up, down
        directions = [
            (0, 1),  # right
            (0, -1), # left
            (-1, 0), # up
            (1, 0),  # down
        ]
        
        def dfs(grid, row, col, visited):
            """Perform DFS to mark all cells of an island starting from (row, col)."""
            visited.add((row, col))
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                # Check if the new position is within grid boundaries and is part of the island
                if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]) and grid[new_row][new_col] == 1 and (new_row, new_col) not in visited:
                    dfs(grid, new_row, new_col, visited)

        num_rows, num_cols = len(grid1), len(grid1[0])
        
        # Find all islands in grid1
        visited_grid1 = set()
        for row in range(num_rows):
            for col in range(num_cols):
                if grid1[row][col] == 1 and (row, col) not in visited_grid1:
                    current_island = set()
                    dfs(grid1, row, col, current_island)
                    visited_grid1 |= current_island

        # Find all islands in grid2
        grid2_islands = []
        visited_grid2 = set()
        for row in range(num_rows):
            for col in range(num_cols):
                if grid2[row][col] == 1 and (row, col) not in visited_grid2:
                    current_island = set()
                    dfs(grid2, row, col, current_island)
                    grid2_islands.append(current_island)
                    visited_grid2 |= current_island

        # Count sub-islands in grid2 that are fully contained in grid1
        sub_island_count = 0
        for island2 in grid2_islands:
            # If all cells of the island in grid2 are present in any island in grid1, count it as a sub-island
            if island2 <= visited_grid1:
                sub_island_count += 1

        return sub_island_count
