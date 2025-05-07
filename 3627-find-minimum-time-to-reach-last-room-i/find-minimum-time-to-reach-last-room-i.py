from typing import List, Tuple
from heapq import heappush, heappop
from collections import defaultdict

class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        """
        Computes the minimum time to reach the bottom-right cell in a grid where:
        - Moving to a cell takes at least 1 second,
        - You must wait until `moveTime[x][y]` has passed before you can enter cell (x, y).
        """
        m, n = len(moveTime), len(moveTime[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up

        # Priority queue: (time_cost, (x, y))
        min_heap: List[Tuple[int, Tuple[int, int]]] = [(0, (0, 0))]
        min_time = defaultdict(lambda: float('inf'))
        min_time[(0, 0)] = 0

        while min_heap:
            current_time, (x, y) = heappop(min_heap)

            # Early exit if target is reached
            if (x, y) == (m - 1, n - 1):
                return current_time

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if 0 <= nx < m and 0 <= ny < n:
                    next_time = max(current_time + 1, moveTime[nx][ny] + 1)

                    if next_time < min_time[(nx, ny)]:
                        min_time[(nx, ny)] = next_time
                        heappush(min_heap, (next_time, (nx, ny)))

        return -1  # No valid path
