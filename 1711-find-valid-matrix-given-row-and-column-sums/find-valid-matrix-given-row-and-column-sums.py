class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        # Initialize the matrix with zeros
        m, n = len(rowSum), len(colSum)
        matrix = [[0] * n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                # Choose the minimum of rowSum[i] and colSum[j]
                val = min(rowSum[i], colSum[j])
                matrix[i][j] = val
                
                # Subtract the chosen value from both rowSum and colSum
                rowSum[i] -= val
                colSum[j] -= val
                
                # If rowSum[i] or colSum[j] becomes zero, move to the next row or column
                if rowSum[i] == 0:
                    break
        
        return matrix