class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        # Combine the positions, healths, and directions into a list of robots
        robots = [[position, health, direction, index] for index, (position, health, direction) in enumerate(zip(positions, healths, directions))]
        
        # Sort the robots based on their positions
        robots.sort()

        stack = []

        for robot in robots:
            if not stack:
                stack.append(robot)
            else:
                if robot[2] == "R":  # Current robot is moving right
                    stack.append(robot)
                else:  # Current robot is moving left
                    while stack and stack[-1][2] == "R" and stack[-1][1] < robot[1]:
                        # Robot moving left collides with the robot moving right
                        robot[1] -= 1  # Reduce the health of the current robot
                        stack.pop()  # Remove the robot from the stack

                    if not stack:
                        stack.append(robot)
                    elif stack[-1][2] == "L":
                        stack.append(robot)
                    elif stack[-1][1] == robot[1]:
                        stack.pop()  # Both robots destroy each other
                    elif stack[-1][1] > robot[1]:
                        stack[-1][1] -= 1  # Reduce the health of the robot in the stack

        # Prepare the list of surviving robots' healths
        surviving_robots = [(robot[3], robot[1]) for robot in stack]
        surviving_robots.sort()  # Sort based on original indices

        return [health for index, health in surviving_robots]
