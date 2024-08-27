class Solution:       
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        def go_back():
            """Helper function to move the robot back to its previous position."""
            robot.turnRight()
            robot.turnRight()
            robot.move()
            robot.turnRight()
            robot.turnRight()
            
        def backtrack(position, current_direction):
            """Recursive backtracking function to explore and clean the entire room."""
            visited_positions.add(position)
            robot.clean()

            # Explore all four directions (clockwise: 0 - up, 1 - right, 2 - down, 3 - left)
            for i in range(4):
                new_direction = (current_direction + i) % 4
                next_position = (
                    position[0] + movement_directions[new_direction][0], 
                    position[1] + movement_directions[new_direction][1]
                )
                
                if next_position not in visited_positions and robot.move():
                    backtrack(next_position, new_direction)
                    go_back()
                
                # Turn the robot to the next direction (clockwise)
                robot.turnRight()
    
        # Directions array representing movement in order: up, right, down, left
        movement_directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        visited_positions = set()
        starting_position = (0, 0)
        starting_direction = 0
        backtrack(starting_position, starting_direction)
