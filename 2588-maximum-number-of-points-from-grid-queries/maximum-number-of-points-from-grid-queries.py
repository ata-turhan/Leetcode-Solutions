import heapq
from typing import List

class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        m, n = len(grid), len(grid[0])
        # Pair each query with its original index and sort by the query value.
        sorted_queries = sorted([(q, i) for i, q in enumerate(queries)], key=lambda x: x[0])
        
        # Prepare the answer array.
        ans = [0] * len(queries)
        # Create a visited matrix to mark cells we have already added to the heap.
        visited = [[False] * n for _ in range(m)]
        # Min-heap for BFS expansion; start from the top-left cell.
        heap = []
        heapq.heappush(heap, (grid[0][0], 0, 0))
        visited[0][0] = True
        
        # This variable counts the number of points (cells visited) so far.
        count = 0
        # Directions for 4-way movement.
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        # Process each query in sorted order.
        for q, idx in sorted_queries:
            # Expand the BFS as long as the smallest cell in the heap has a value less than q.
            while heap and heap[0][0] < q:
                val, x, y = heapq.heappop(heap)
                count += 1  # We have visited a new cell.
                # Check all 4 adjacent neighbors.
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    # Ensure the neighbor is within bounds and not visited.
                    if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                        visited[nx][ny] = True
                        heapq.heappush(heap, (grid[nx][ny], nx, ny))
            # Store the number of points for this query based on current BFS expansion.
            ans[idx] = count
        
        return ans
