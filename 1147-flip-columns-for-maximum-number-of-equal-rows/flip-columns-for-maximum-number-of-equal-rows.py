class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        row_patterns = defaultdict(int)

        for row in range(len(matrix)):
            pattern = []
            prev_el = matrix[row][0]
            cur_count = 1
            for col in range(1, len(matrix[0])):        
                if matrix[row][col] == prev_el:
                    cur_count += 1
                else:
                    pattern.append(cur_count)
                    cur_count = 1
                    prev_el = matrix[row][col]
            pattern.append(cur_count)
            row_patterns[tuple(pattern)] += 1

        return max(row_patterns.values())