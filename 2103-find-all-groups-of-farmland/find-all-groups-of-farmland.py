class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        moves = [
            [0, 1],
            [1, 0],
            [0, -1],
            [-1, 0]
        ]
        m = len(land)
        n = len(land[0])
        def dfs(r, c, visited, mix, miy, _max, may):
            visited.add((r, c))
            mix = min(mix, r)
            _max = max(_max, r)
            miy = min(miy, c)
            may = max(may, c)
            for move in moves:
                nr, nc = r + move[0], c + move[1]
                if nr in range(m) and nc in range(n) and (nr, nc) not in visited and land[nr][nc] == 1:
                    coords = dfs(nr, nc, visited, mix, miy, _max, may)
                    mix = min(mix, coords[0])
                    _max = max(_max, coords[2])
                    miy = min(miy, coords[1])
                    may = max(may, coords[3])
            return [mix, miy, _max, may]

        res = []
        visited = set()
        for i in range(m):
            for j in range(n):
                if (i, j) not in visited and land[i][j] == 1:
                    rect = dfs(i, j, visited, float("inf"), float("inf"), float("-inf"), float("-inf"))
                    res.append(rect)

        return res
        