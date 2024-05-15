from collections import deque
from typing import List

class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        
        # Initialize distances to -1
        dist = [[-1] * cols for _ in range(rows)]
        deq = deque()

        # Start BFS from all 1's
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    deq.append((i, j))
                    dist[i][j] = 0

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        # Multi-source BFS to compute minimum distances
        while deq:
            i, j = deq.popleft()
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if 0 <= ni < rows and 0 <= nj < cols and dist[ni][nj] == -1:
                    dist[ni][nj] = dist[i][j] + 1
                    deq.append((ni, nj))

        # Function to check if we can reach bottom-right corner with safeness factor at least v
        def canReach(v):
            if dist[0][0] < v or dist[rows - 1][cols - 1] < v:
                return False
            
            deq = deque([(0, 0)])
            visited = set([(0, 0)])
            while deq:
                i, j = deq.popleft()
                if i == rows - 1 and j == cols - 1:
                    return True
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < rows and 0 <= nj < cols and (ni, nj) not in visited and dist[ni][nj] >= v:
                        visited.add((ni, nj))
                        deq.append((ni, nj))
            return False

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
