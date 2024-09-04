class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        # Direction vectors for North, East, South, West
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        # Initial direction index, facing North
        dir_idx = 0
        
        # Starting position
        x, y = 0, 0
        # Set to store obstacles for O(1) lookup
        obstacle_set = set(map(tuple, obstacles))
        
        # Variable to track the maximum distance squared
        max_distance_sq = 0
        
        # Iterate over each command
        for command in commands:
            if command == -2:  # Turn left
                dir_idx = (dir_idx - 1) % 4
            elif command == -1:  # Turn right
                dir_idx = (dir_idx + 1) % 4
            else:  # Move forward 'command' steps
                for _ in range(command):
                    # Calculate the next position
                    nx, ny = x + directions[dir_idx][0], y + directions[dir_idx][1]
                    # If next position is not an obstacle, update the position
                    if (nx, ny) not in obstacle_set:
                        x, y = nx, ny
                        # Calculate the current distance squared
                        max_distance_sq = max(max_distance_sq, x * x + y * y)
                    else:
                        # If there's an obstacle, stop moving in this direction
                        break
        
        # Return the maximum distance squared
        return max_distance_sq
