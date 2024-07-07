from typing import List

class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        count = 0
        rows = len(grid)
        cols = len(grid[0])

        # Initialize previous row to keep track of 'X' and 'Y' counts
        prev_row_counts = [[0, 0] for _ in range(cols)]

        # Iterate through each row of the grid
        for i in range(rows):
            # Initialize current row counts for 'X' and 'Y'
            current_row_counts = [0, 0]
            for j in range(cols):
                # Calculate cumulative counts of 'X' and 'Y' up to the current cell
                x_count = prev_row_counts[j][0] + current_row_counts[0] + (grid[i][j] == "X")
                y_count = prev_row_counts[j][1] + current_row_counts[1] + (grid[i][j] == "Y")

                # If there is at least one 'X' and the counts of 'X' and 'Y' are equal, increment count
                if x_count > 0 and x_count == y_count:
                    count += 1

                # Update the previous row counts for the current column
                prev_row_counts[j][0] = x_count
                prev_row_counts[j][1] = y_count

                # Update the current row counts
                current_row_counts[0] += (grid[i][j] == "X")
                current_row_counts[1] += (grid[i][j] == "Y")

        return count
