from typing import List

class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        """
        Find the minimum area of a rectangle that covers all 1's in the grid.
        
        The rectangle must be axis-aligned (horizontal & vertical sides).
        
        Steps:
        1. Traverse the entire grid to find the min/max row and column indices
           that contain a 1.
        2. The rectangle spans from min_row → max_row and min_col → max_col.
        3. Height = (max_row - min_row + 1)
           Width  = (max_col - min_col + 1)
        4. Return area = height * width
        """
        
        rows, cols = len(grid), len(grid[0])
        
        # Initialize bounds
        min_row, max_row = rows, -1
        min_col, max_col = cols, -1
        
        # Find boundaries of all 1's
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    min_row = min(min_row, r)
                    max_row = max(max_row, r)
                    min_col = min(min_col, c)
                    max_col = max(max_col, c)
        
        # Compute dimensions
        height = max_row - min_row + 1
        width = max_col - min_col + 1
        
        return height * width
