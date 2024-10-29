class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        moves = [[-1] * n for _ in range(m)]
        for i in range(m):
            moves[i][0] = 0
        
        
        for j in range(n):
            for i in range(m):
                max_move = -1
                if j - 1 >= 0:
                    if grid[i][j-1] < grid[i][j]:
                        max_move = max(max_move, moves[i][j-1])
                    if i - 1 >= 0 and grid[i-1][j-1] < grid[i][j]:
                        max_move = max(max_move, moves[i - 1][j - 1])
                    if i + 1 < m and grid[i+1][j-1] < grid[i][j]:
                        max_move = max(max_move, moves[i + 1][j - 1])
                if max_move != -1:
                    moves[i][j] = max_move + 1

        return max( max(row) for row in moves )


                
        