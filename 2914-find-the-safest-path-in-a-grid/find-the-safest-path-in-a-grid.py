from collections import deque
from typing import List

class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        
        # Initialize distances to -1
        dist = [[-1] * cols for _ in range(rows)]
        deq = deque()

        # Start BFS from all cells containing 1's
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    deq.append((i, j))
                    dist[i][j] = 0

        # Directions for moving in the grid: right, down, left, up
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        # Multi-source BFS to compute minimum distances from 1's
        while deq:
            i, j = deq.popleft()
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if 0 <= ni < rows and 0 <= nj < cols and dist[ni][nj] == -1:
                    dist[ni][nj] = dist[i][j] + 1
                    deq.append((ni, nj))

        # Function to check if we can reach bottom-right corner with safeness factor at least v using DFS
        def canReach(v):
            # If start or end point's safeness is less than v, return False
            if dist[0][0] < v or dist[rows - 1][cols - 1] < v:
                return False
            
            # DFS to check reachability
            def dfs(i, j, visited):
                if (i, j) in visited:
                    return False
                if i == rows - 1 and j == cols - 1:
                    return True
                visited.add((i, j))
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < rows and 0 <= nj < cols and (ni, nj) not in visited and dist[ni][nj] >= v:
                        if dfs(ni, nj, visited):
                            return True
                return False
            
            return dfs(0, 0, set())

        # Binary search on the possible safeness factor
        left, right = 0, min(rows, cols) - 1
        res = 0
        while left <= right:
            mid = (left + right) // 2
            if canReach(mid):
                res = mid
                left = mid + 1
            else:
                right = mid - 1

        return res
