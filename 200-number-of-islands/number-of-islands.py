class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Define the possible directions (up, left, down, right)
        directions = [
            [-1, 0],
            [0, -1],
            [1, 0],
            [0, 1],
        ]

        def dfs(grid, r, c):
            """
            Depth-first search to explore the island and mark visited cells.

            Args:
                grid (List[List[str]]): The grid representing the map.
                r (int): Row index.
                c (int): Column index.
            """
            grid[r][c] = "0"  # Mark the current cell as visited

            # Explore all four directions
            for d in directions:
                nr, nc = r + d[0], c + d[1]
                # Check if the next cell is within the grid and is part of an island
                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == "1":
                    dfs(grid, nr, nc)  # Recursively explore the island

        M = len(grid)  # Number of rows
        N = len(grid[0])  # Number of columns
        count = 0  # Initialize island count

        # Iterate through the grid to find islands
        for i in range(M):
            for j in range(N):
                if grid[i][j] == "1":  # If the cell is part of an island
                    count += 1  # Increment island count
                    dfs(grid, i, j)  # Start DFS to explore the island and mark visited cells

        return count  # Return the total number of islands
