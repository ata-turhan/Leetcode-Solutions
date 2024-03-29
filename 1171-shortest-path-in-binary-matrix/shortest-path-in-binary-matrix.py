class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        if len(grid) == 1:
            return 1
        moves = [
            [0, 1],
            [0, -1],
            [1, 0],
            [-1, 0],
            [-1, -1],
            [1, 1],
            [1, -1],
            [-1, 1],
        ]

        q = deque()
        q.append((0, 0, 1))
        n = len(grid)
        visited = set()
        visited.add((0,0))

        while q:
            i, j, dist = q.popleft()
            for move in moves:
                ni, nj, ndist = i + move[0], j + move[1], dist + 1
                if ni in range(n) and nj in range(n) and (ni, nj) not in visited \
                and grid[ni][nj] == 0:
                    if ni == n-1 and nj == n-1:
                        return ndist
                    q.append((ni, nj, ndist))
                    visited.add((ni, nj))

        return -1


        