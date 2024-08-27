from collections import deque
from typing import List

class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        start_x, start_y = -1, -1
        
        # Find the starting position denoted by '*'
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "*":
                    start_x, start_y = i, j
                    break 

        # Initialize the BFS queue with the starting position and distance 0
        queue = deque([(start_x, start_y, 0)])
        
        # Possible movements: right, left, up, down
        directions = [
            [0, 1],  # Move right
            [0, -1], # Move left
            [-1, 0], # Move up
            [1, 0],  # Move down
        ]
        
        # Set to keep track of visited cells to avoid revisiting
        visited = set([(start_x, start_y)])
        
        while queue:
            x, y, dist = queue.popleft()
            
            # Explore all possible directions
            for dx, dy in directions:
                new_x, new_y = x + dx, y + dy
                
                # Check if the new position is within the grid boundaries,
                # is not a blocked cell 'X', and hasn't been visited yet
                if 0 <= new_x < rows and 0 <= new_y < cols and grid[new_x][new_y] != "X" and (new_x, new_y) not in visited:
                    # If the new position contains food '#', return the distance + 1
                    if grid[new_x][new_y] == "#":
                        return dist + 1
                    
                    # Otherwise, add the new position to the queue with incremented distance
                    else:
                        queue.append((new_x, new_y, dist + 1))
                        visited.add((new_x, new_y))

        # If no path to food is found, return -1
        return -1
