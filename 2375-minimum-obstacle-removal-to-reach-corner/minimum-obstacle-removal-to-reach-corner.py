class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [
            [-1, 0],
            [0, 1],
            [1, 0],
            [0, -1]
        ]

        heap = []
        visited = defaultdict(lambda: float("inf"))

        heap.append((0, 0, 0))
        visited[(0,0)] = 0

        while heap:
            obstacle_removed, cur_x, cur_y, = heappop(heap)

            if cur_x == m - 1 and cur_y == n - 1:
                return visited[(cur_x, cur_y)]

            for direction in directions:
                new_x, new_y = cur_x + direction[0], cur_y + direction[1]

                if 0 <= new_x < m and 0 <= new_y < n and obstacle_removed + grid[new_x][new_y] < visited[(new_x, new_y)]:
                    visited[(new_x, new_y)] = obstacle_removed + grid[new_x][new_y]
                    heappush(heap, (obstacle_removed + grid[new_x][new_y], new_x, new_y, ))

        return -1

        