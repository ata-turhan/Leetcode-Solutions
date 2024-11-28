from typing import List
from heapq import heappop, heappush
from collections import defaultdict

class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        # Min-heap to prioritize paths with fewer obstacles removed
        min_heap = []
        # Dictionary to track the minimum obstacles removed to reach each cell
        min_obstacles = defaultdict(lambda: float("inf"))

        # Start at (0, 0) with 0 obstacles removed
        heappush(min_heap, (0, 0, 0))
        min_obstacles[(0, 0)] = 0

        while min_heap:
            obstacles_removed, x, y = heappop(min_heap)

            # If we reach the bottom-right cell, return the minimum obstacles removed
            if x == rows - 1 and y == cols - 1:
                return obstacles_removed

            # Explore neighbors
            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if 0 <= nx < rows and 0 <= ny < cols:
                    # Calculate the new obstacle count
                    new_obstacles = obstacles_removed + grid[nx][ny]

                    # If this path is better, update and push to the heap
                    if new_obstacles < min_obstacles[(nx, ny)]:
                        min_obstacles[(nx, ny)] = new_obstacles
                        heappush(min_heap, (new_obstacles, nx, ny))

        # If no path exists (shouldn't happen in valid inputs), return -1
        return -1
