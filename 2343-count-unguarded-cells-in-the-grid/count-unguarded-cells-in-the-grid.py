class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        cells = [[True] * n for _ in range(m)]
        set_guards = set(tuple(guard) for guard in guards)
        set_walls = set(tuple(wall) for wall in walls)

        for i in range(m):
            guard_watches = False
            for j in range(n):
                if (i, j) in set_walls:
                    cells[i][j] = False
                    guard_watches = False
                elif (i, j) in set_guards:
                    cells[i][j] = False
                    guard_watches = True
                else:
                    if guard_watches:
                        cells[i][j] = False
            for j in range(n-1, -1, -1):
                if (i, j) in set_walls:
                    cells[i][j] = False
                    guard_watches = False
                elif (i, j) in set_guards:
                    cells[i][j] = False
                    guard_watches = True
                else:
                    if guard_watches:
                        cells[i][j] = False

        for j in range(n):
            guard_watches = False
            for i in range(m):
                if (i, j) in set_walls:
                    cells[i][j] = False
                    guard_watches = False
                elif (i, j) in set_guards:
                    cells[i][j] = False
                    guard_watches = True
                else:
                    if guard_watches:
                        cells[i][j] = False
            for i in range(m - 1, -1, -1):
                if (i, j) in set_walls:
                    cells[i][j] = False
                    guard_watches = False
                elif (i, j) in set_guards:
                    cells[i][j] = False
                    guard_watches = True
                else:
                    if guard_watches:
                        cells[i][j] = False

        return sum(sum(row) for row in cells)
        