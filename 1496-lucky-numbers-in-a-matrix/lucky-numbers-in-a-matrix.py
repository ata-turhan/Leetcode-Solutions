class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        
        # Initialize arrays to track the smallest values in each row and the largest values in each column
        min_in_rows = [float("inf")] * m
        max_in_cols = [0] * n

        # Find the minimum value in each row
        for i in range(m):
            for j in range(n):
                if matrix[i][j] < min_in_rows[i]:
                    min_in_rows[i] = matrix[i][j]

        # Find the maximum value in each column
        for j in range(n):
            for i in range(m):
                if matrix[i][j] > max_in_cols[j]:
                    max_in_cols[j] = matrix[i][j]

        lucky_numbers = []

        # Check for elements that are both the minimum in their row and the maximum in their column
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == min_in_rows[i] and matrix[i][j] == max_in_cols[j]:
                    lucky_numbers.append(matrix[i][j])

        return lucky_numbers
