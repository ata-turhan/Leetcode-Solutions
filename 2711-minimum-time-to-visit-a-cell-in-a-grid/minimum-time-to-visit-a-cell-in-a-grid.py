import heapq
from typing import List

class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        import heapq

        m, n = len(grid), len(grid[0])

        # Check if it's possible to start moving from (0, 0)
        if (m > 1 and grid[1][0] > 1) and (n >1 and grid[0][1] > 1):
            return -1

        arrival_time = [[float('inf')] * n for _ in range(m)]
        arrival_time[0][0] = 0

        heap = [(0, 0, 0)]  # (time, x, y)

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right

        while heap:
            t, x, y = heapq.heappop(heap)

            if x == m -1 and y == n -1:
                return t  # Reached destination

            if t > arrival_time[x][y]:
                continue  # Skip if we have already found a better path

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0<= nx < m and 0 <= ny < n:
                    if grid[nx][ny] <= t + 1:
                        next_t = t + 1
                    else:
                        delta = grid[nx][ny] - (t + 1)
                        if delta % 2 == 0:
                            next_t = grid[nx][ny]
                        else:
                            next_t = grid[nx][ny] + 1
                    if arrival_time[nx][ny] > next_t:
                        arrival_time[nx][ny] = next_t
                        heapq.heappush(heap, (next_t, nx, ny))

        return -1
