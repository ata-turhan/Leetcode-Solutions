class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])

        for i in range(m):
            for j in range(n):
                left_val, diagonal_val, up_val = [0] * 3
                if j > 0:
                    left_val = matrix[i][j-1]
                if i > 0:
                    up_val = matrix[i-1][j]
                if i > 0 and j > 0:
                    diagonal_val = matrix[i-1][j-1]

                if matrix[i][j] == 1:
                    matrix[i][j] = min(left_val, diagonal_val, up_val) + 1
        
        return sum(sum(row) for row in matrix)
        