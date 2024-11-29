import heapq
from typing import List

class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        # Check if it's possible to start moving from (0, 0)
        if (rows > 1 and grid[1][0] > 1) and (cols > 1 and grid[0][1] > 1):
            return -1

        # Initialize the minimum arrival time matrix with infinity
        min_arrival_time = [[float('inf')] * cols for _ in range(rows)]
        min_arrival_time[0][0] = 0

        # Min-heap to store the cells to process: (time, x, y)
        priority_queue = [(0, 0, 0)]

        # Directions for moving in 4 directions: Up, Down, Left, Right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while priority_queue:
            current_time, x, y = heapq.heappop(priority_queue)

            # If we reach the bottom-right corner, return the time
            if x == rows - 1 and y == cols - 1:
                return current_time

            # Skip if a better path to (x, y) has already been found
            if current_time > min_arrival_time[x][y]:
                continue

            # Explore neighbors
            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if 0 <= nx < rows and 0 <= ny < cols:
                    # Calculate the next possible time to reach (nx, ny)
                    if grid[nx][ny] <= current_time + 1:
                        next_time = current_time + 1
                    else:
                        # Calculate delay needed to wait before moving to (nx, ny)
                        delay = grid[nx][ny] - (current_time + 1)
                        next_time = grid[nx][ny] if delay % 2 == 0 else grid[nx][ny] + 1

                    # Update the arrival time if a better path is found
                    if min_arrival_time[nx][ny] > next_time:
                        min_arrival_time[nx][ny] = next_time
                        heapq.heappush(priority_queue, (next_time, nx, ny))

        # If the destination is not reachable, return -1
        return -1
