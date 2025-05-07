class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        m, n = len(moveTime), len(moveTime[0]) 

        dirs = [
            [0, 1],
            [0, -1],
            [1, 0],
            [-1, 0],
        ]

        dists = defaultdict(lambda: float("inf"))

        dists[(0, 0)] = 0
        heap = [ [0, (0,0)] ]

        while heap:
            dist, point = heappop(heap)
            x, y = point

            if x == m - 1 and y == n - 1:
                return dist

            for dir in dirs:
                nx, ny = x + dir[0], y + dir[1]

                if 0 <= nx < m and 0 <= ny < n and dist + 1 < dists[(nx, ny)]:
                    dists[(nx, ny)] = max(moveTime[nx][ny] + 1, dist + 1)
                    heappush(heap, [dists[(nx, ny)], (nx, ny)])


        return -1
