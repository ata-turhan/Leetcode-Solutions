import heapq

class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        # Edge case: if the matrix has fewer than 3 rows or 3 columns, no water can be trapped
        if len(heightMap) < 3 or len(heightMap[0]) < 3:
            return 0

        m, n = len(heightMap), len(heightMap[0])
        visited = [[False] * n for _ in range(m)]
        min_heap = []

        # 1. Push all boundary cells into the priority queue
        for r in range(m):
            for c in range(n):
                if r in (0, m - 1) or c in (0, n - 1):
                    heapq.heappush(min_heap, (heightMap[r][c], r, c))
                    visited[r][c] = True

        # Variable to accumulate total trapped water
        water_trapped = 0

        # Directions for exploring neighbors (down, up, right, left)
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        # 2. Process cells in the priority queue
        while min_heap:
            current_height, r, c = heapq.heappop(min_heap)

            # Explore the 4 neighbors
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                # Check boundaries and whether visited
                if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc]:
                    visited[nr][nc] = True
                    neighbor_height = heightMap[nr][nc]

                    # If neighbor is lower, water can be trapped
                    if neighbor_height < current_height:
                        water_trapped += current_height - neighbor_height
                        # Update the neighbor's height to current_height
                        neighbor_height = current_height

                    # Push the neighbor into the heap with the updated height
                    heapq.heappush(min_heap, (neighbor_height, nr, nc))

        return water_trapped