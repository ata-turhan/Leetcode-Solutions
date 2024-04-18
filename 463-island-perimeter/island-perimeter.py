class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # Define the possible moves (up, right, down, left)
        moves = [
            [0, 1],
            [1, 0],
            [0, -1],
            [-1, 0],
        ]
        m = len(grid)  # Number of rows
        n = len(grid[0])  # Number of columns
        
        def dfs(i, j, visited):
            """
            Depth-first search to explore the island and calculate perimeter.

            Args:
                i (int): Row index.
                j (int): Column index.
                visited (set): Set of visited cells.
            """
            if (i, j) in visited:  # Skip visited cells
                return 0
            
            perimeter = 0  # Initialize perimeter for this cell
            visited.add((i, j))  # Mark current cell as visited
            # Check all four directions for water or out of bounds
            for move in moves:
                ni, nj = i + move[0], j + move[1]
                if ni < 0 or ni >= m or nj < 0 or nj >= n or grid[ni][nj] == 0:
                    perimeter += 1  # Increment perimeter for water or boundary
                else:
                    perimeter += dfs(ni, nj, visited)  # Recursively explore land cells
            return perimeter
        
        # Initialize visited set
        visited = set()
        
        # Iterate through the grid to find the first land cell
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return dfs(i, j, visited)  # Start DFS from the first land cell and return perimeter

