class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        heights = defaultdict(lambda:float("inf"))
        queue = deque()

        m, n = len(isWater), len(isWater[0])

        for i in range(m):
            for j in range(n):
                if isWater[i][j] == 1:
                    queue.append((i, j, 0))
                    heights[(i, j)] = 0

        directions = [
            [0, 1],
            [0, -1],
            [1, 0],
            [-1, 0]
        ]

        while queue:
            for _ in range(len(queue)):
                i, j, height = queue.popleft()
                for dx, dy in directions:
                    nx = i + dx
                    ny = j + dy
                    if 0 <= nx < m and 0 <= ny < n:
                        if heights[(nx, ny)] == 0:
                            continue
                        else:
                            if height + 1 < heights[(nx, ny)]:
                                heights[(nx, ny)] = height + 1
                                queue.append((nx, ny, heights[(nx, ny)]))



        res = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                res[i][j] = heights[(i, j)]

        return res
        