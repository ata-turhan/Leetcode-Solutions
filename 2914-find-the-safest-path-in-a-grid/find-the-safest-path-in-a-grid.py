from collections import deque
from typing import List

class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        
        # Initialize distances to -1
        distance = [[-1] * cols for _ in range(rows)]
        queue = deque()

        # Start BFS from all cells containing 1's
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    queue.append((row, col))
                    distance[row][col] = 0

        # Directions for moving in the grid: right, down, left, up
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        # Multi-source BFS to compute minimum distances from 1's
        while queue:
            curr_row, curr_col = queue.popleft()
            for d_row, d_col in directions:
                next_row, next_col = curr_row + d_row, curr_col + d_col
                if 0 <= next_row < rows and 0 <= next_col < cols and distance[next_row][next_col] == -1:
                    distance[next_row][next_col] = distance[curr_row][curr_col] + 1
                    queue.append((next_row, next_col))

        # Function to check if we can reach bottom-right corner with safeness factor at least `safeness`
        def canReach(safeness):
            if distance[0][0] < safeness or distance[rows - 1][cols - 1] < safeness:
                return False
            
            def dfs(row, col, visited):
                if (row, col) in visited:
                    return False
                if row == rows - 1 and col == cols - 1:
                    return True
                visited.add((row, col))
                for d_row, d_col in directions:
                    next_row, next_col = row + d_row, col + d_col
                    if 0 <= next_row < rows and 0 <= next_col < cols and (next_row, next_col) not in visited and distance[next_row][next_col] >= safeness:
                        if dfs(next_row, next_col, visited):
                            return True
                return False
            
            return dfs(0, 0, set())

        # Binary search on the possible safeness factor
        left, right = 0, min(rows, cols) - 1
        max_safeness = 0
        while left <= right:
            mid = (left + right) // 2
            if canReach(mid):
                max_safeness = mid
                left = mid + 1
            else:
                right = mid - 1

        return max_safeness
