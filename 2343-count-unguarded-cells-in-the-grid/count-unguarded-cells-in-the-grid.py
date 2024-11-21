from typing import List

class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        # Initialize the grid with True values, indicating cells are initially unguarded
        grid = [[True] * n for _ in range(m)]
        guard_positions = set(tuple(guard) for guard in guards)
        wall_positions = set(tuple(wall) for wall in walls)

        # Horizontal pass (left to right and right to left)
        for row in range(m):
            is_guard_active = False
            for col in range(n):
                # Left to right
                if (row, col) in wall_positions:
                    grid[row][col] = False
                    is_guard_active = False
                elif (row, col) in guard_positions:
                    grid[row][col] = False
                    is_guard_active = True
                elif is_guard_active:
                    grid[row][col] = False

            is_guard_active = False
            for col in range(n - 1, -1, -1):
                # Right to left
                if (row, col) in wall_positions:
                    grid[row][col] = False
                    is_guard_active = False
                elif (row, col) in guard_positions:
                    grid[row][col] = False
                    is_guard_active = True
                elif is_guard_active:
                    grid[row][col] = False

        # Vertical pass (top to bottom and bottom to top)
        for col in range(n):
            is_guard_active = False
            for row in range(m):
                # Top to bottom
                if (row, col) in wall_positions:
                    grid[row][col] = False
                    is_guard_active = False
                elif (row, col) in guard_positions:
                    grid[row][col] = False
                    is_guard_active = True
                elif is_guard_active:
                    grid[row][col] = False

            is_guard_active = False
            for row in range(m - 1, -1, -1):
                # Bottom to top
                if (row, col) in wall_positions:
                    grid[row][col] = False
                    is_guard_active = False
                elif (row, col) in guard_positions:
                    grid[row][col] = False
                    is_guard_active = True
                elif is_guard_active:
                    grid[row][col] = False

        # Count the remaining unguarded cells
        return sum(sum(row) for row in grid)
