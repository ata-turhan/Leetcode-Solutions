class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        # Define possible movements (up, down, left, right)
        moves = [
            [0, 1],
            [1, 0],
            [0, -1],
            [-1, 0]
        ]
        m = len(land)  # Number of rows
        n = len(land[0])  # Number of columns

        def dfs(r, c, visited, min_x, min_y, max_x, max_y):
            """
            Depth-first search to explore the farmland and find the boundaries.

            Args:
                r (int): Row index.
                c (int): Column index.
                visited (set): Set to track visited cells.
                min_x (int): Minimum row index of the farmland.
                min_y (int): Minimum column index of the farmland.
                max_x (int): Maximum row index of the farmland.
                max_y (int): Maximum column index of the farmland.

            Returns:
                List[int]: List containing coordinates of the farmland.
            """
            visited.add((r, c))  # Mark the current cell as visited
            min_x = min(min_x, r)  # Update minimum row index
            max_x = max(max_x, r)  # Update maximum row index
            min_y = min(min_y, c)  # Update minimum column index
            max_y = max(max_y, c)  # Update maximum column index
            
            # Explore all four directions
            for move in moves:
                nr, nc = r + move[0], c + move[1]
                # Check if the next cell is within the grid and is part of the farmland
                if nr in range(m) and nc in range(n) and (nr, nc) not in visited and land[nr][nc] == 1:
                    # Recursively explore the farmland and update coordinates
                    coords = dfs(nr, nc, visited, min_x, min_y, max_x, max_y)
                    min_x = min(min_x, coords[0])
                    max_x = max(max_x, coords[2])
                    min_y = min(min_y, coords[1])
                    max_y = max(max_y, coords[3])

            return [min_x, min_y, max_x, max_y]  # Return coordinates of the farmland

        res = []  # List to store farmland rectangles
        visited = set()  # Set to track visited cells

        # Iterate through each cell in the grid
        for i in range(m):
            for j in range(n):
                # If the cell is not visited and is part of the farmland
                if (i, j) not in visited and land[i][j] == 1:
                    # Explore the farmland and find its boundaries
                    rect = dfs(i, j, visited, float("inf"), float("inf"), float("-inf"), float("-inf"))
                    res.append(rect)  # Add the farmland rectangle to the result

        return res  # Return the list of farmland rectangles
