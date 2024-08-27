from collections import deque
from typing import List

class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        rows, cols = len(grid), len(grid[0])
        # The 3D visited array tracks the minimum obstacles removed for each cell (row, col)
        visited = [[[float('inf')] * (k + 1) for _ in range(cols)] for _ in range(rows)]
        
        # BFS queue stores tuples of the form (row, col, steps, obstacles_removed)
        queue = deque([(0, 0, 0, 0)])  # Start from (0, 0) with 0 steps and 0 obstacles removed
        visited[0][0][0] = 0
        
        # Possible movements: right, down, left, up
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        while queue:
            row, col, steps, obstacles_removed = queue.popleft()
            
            # If we reach the bottom-right corner, return the number of steps
            if (row, col) == (rows - 1, cols - 1):
                return steps
            
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                
                # Check if the new position is within the grid boundaries
                if 0 <= new_row < rows and 0 <= new_col < cols:
                    # Calculate the number of obstacles removed if we move to this new position
                    new_obstacles_removed = obstacles_removed + grid[new_row][new_col]
                    
                    # If the new position can be reached with fewer or equal obstacles removed
                    # than previously recorded, proceed with this path
                    if new_obstacles_removed <= k and new_obstacles_removed < visited[new_row][new_col][new_obstacles_removed]:
                        # Update the visited array with the new count of obstacles removed
                        visited[new_row][new_col][new_obstacles_removed] = new_obstacles_removed
                        
                        # Add the new position to the queue with an incremented step count
                        queue.append((new_row, new_col, steps + 1, new_obstacles_removed))
        
        # If no valid path is found, return -1
        return -1
