from typing import List

class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        # Define possible moves: right, down, left, up
        directions = [
            [0, 1],
            [1, 0],
            [0, -1],
            [-1, 0]
        ]
        
        max_gold = 0  # Variable to store the maximum amount of gold collected

        def dfs(x, y, visited):
            # Current cell's gold value
            current_gold = grid[x][y]

            # Variable to store the maximum remaining gold that can be collected
            max_remaining_gold = 0
            
            # Mark the current cell as visited
            visited.add((x, y))
            
            # Explore all possible directions
            for direction in directions:
                nx, ny = x + direction[0], y + direction[1]
                # Check if the new cell is within bounds, not visited, and not zero
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] != 0 and (nx, ny) not in visited:
                    max_remaining_gold = max(max_remaining_gold, dfs(nx, ny, visited))
            
            # Unmark the current cell as visited
            visited.remove((x, y))

            # Return the current cell's gold value plus the maximum remaining gold
            return current_gold + max_remaining_gold 

        # Iterate over each cell in the grid
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != 0:  # Start DFS from cells that contain gold
                    max_gold = max(max_gold, dfs(i, j, set()))  # Update the maximum gold collected
        
        return max_gold
