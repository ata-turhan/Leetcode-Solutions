class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        rows, cols = [0] * m, [0] * n

        pos = dict()
        for i in range(m):
            for j in range(n):
                pos[mat[i][j]] = (i, j)

        for i in range(m * n):
            num = arr[i]
            row, col = pos[num]
            rows[row] += 1
            if rows[row] == n:
                return i
            cols[col] += 1
            if cols[col] == m:
                return i

        return -1
        