from typing import List

class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        """
        Find the maximum number of fish that can be caught starting from any cell in the grid.
        
        :param grid: List[List[int]] - A 2D grid where each cell represents the number of fish (0 if no fish).
        :return: int - The maximum number of fish that can be caught.
        """
        # Define directions for 4-way movement (up, down, left, right)
        directions = [
            [0, 1],  # Right
            [0, -1],  # Left
            [1, 0],  # Down
            [-1, 0]  # Up
        ]

        def dfs(row: int, col: int, visited: set) -> int:
            """
            Perform a depth-first search to collect fish from connected cells.

            :param row: Current row position.
            :param col: Current column position.
            :param visited: Set of visited cells to prevent re-visiting.
            :return: int - Total number of fish collected from this connected component.
            """
            visited.add((row, col))
            fish_caught = grid[row][col]

            # Explore all 4 directions
            for dx, dy in directions:
                new_row, new_col = row + dx, col + dy
                if (0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]) and
                        (new_row, new_col) not in visited and grid[new_row][new_col] > 0):
                    fish_caught += dfs(new_row, new_col, visited)

            return fish_caught

        # Track the maximum fish caught
        max_fish_caught = 0
        all_visited = set()  # Keep track of all visited cells globally

        # Iterate through all cells in the grid
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                # If the cell contains fish and hasn't been visited yet
                if (row, col) not in all_visited and grid[row][col] > 0:
                    local_visited = set()  # Track visited cells for this connected component
                    fish_caught = dfs(row, col, local_visited)
                    max_fish_caught = max(max_fish_caught, fish_caught)
                    # Add local visited cells to the global set
                    all_visited |= local_visited

        return max_fish_caught
