from typing import List, Tuple
from heapq import heappush, heappop
from collections import defaultdict

class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        """
        Computes the minimum time to reach the bottom-right cell in a grid where:
        - You must wait until moveTime[x][y] has passed before entering cell (x, y).
        - Moving to a cell alternates time units between 1 and 2.
        """
        m, n = len(moveTime), len(moveTime[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        # (current_time, (x, y), next_move_time)
        min_heap: List[Tuple[int, Tuple[int, int], int]] = [(0, (0, 0), 1)]
        min_time = defaultdict(lambda: float('inf'))
        min_time[(0, 0)] = 0

        while min_heap:
            current_time, (x, y), move_time = heappop(min_heap)

            if (x, y) == (m - 1, n - 1):
                return current_time

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if 0 <= nx < m and 0 <= ny < n:
                    arrival_time = max(current_time + move_time, moveTime[nx][ny] + move_time)

                    if arrival_time < min_time[(nx, ny)]:
                        min_time[(nx, ny)] = arrival_time
                        # Toggle move time between 1 and 2
                        next_move_time = 2 if move_time == 1 else 1
                        heappush(min_heap, (arrival_time, (nx, ny), next_move_time))

        return -1  # No path found
