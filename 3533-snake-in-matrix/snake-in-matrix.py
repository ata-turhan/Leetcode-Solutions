class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        # Starting position at (0, 0)
        x, y = 0, 0
        
        for command in commands:
            if command == "UP":
                x = max(0, x - 1)  # Ensure snake doesn't move out of the grid
            elif command == "DOWN":
                x = min(n - 1, x + 1)  # Ensure snake doesn't move out of the grid
            elif command == "RIGHT":
                y = min(n - 1, y + 1)  # Ensure snake doesn't move out of the grid
            elif command == "LEFT":
                y = max(0, y - 1)  # Ensure snake doesn't move out of the grid
        
        # Convert 2D position (x, y) to a 1D position in an n x n grid
        return x * n + y
