class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        # Get the dimensions of the grid
        m, n = len(grid), len(grid[0])

        # Initialize a 2D array to store the minimum cost to reach each cell
        # Initially, set the cost to infinity for all cells
        min_cost = [[float('inf')] * n for _ in range(m)]

        # The cost to reach the starting cell (0, 0) is the value of grid[0][0]
        # If grid[0][0] == 0 (safe), cost is 0; if grid[0][0] == 1 (unsafe), cost is 1
        min_cost[0][0] = grid[0][0]

        # Use a deque for performing 0-1 BFS
        queue = deque()
        queue.append((0, 0))  # Start BFS from the top-left corner

        # Define the possible movements: up, down, left, right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # Perform BFS to explore the grid
        while queue:
            # Pop a cell from the front of the deque
            x, y = queue.popleft()

            # If the cost to reach this cell is already greater than or equal to health,
            # we cannot proceed further from this cell
            if min_cost[x][y] >= health:
                continue  # Skip to the next cell in the queue

            # Check if we have reached the destination cell
            if (x, y) == (m - 1, n - 1):
                # If the cost is less than or equal to health - 1, we have at least 1 health remaining
                if min_cost[x][y] <= health - 1:
                    return True  # Path found with sufficient health
                continue  # Else, continue searching for a better path

            # Explore all adjacent cells (up, down, left, right)
            for dx, dy in directions:
                nx, ny = x + dx, y + dy  # Coordinates of the adjacent cell

                # Check if the adjacent cell is within the grid boundaries
                if 0 <= nx < m and 0 <= ny < n:
                    # Calculate the new cost to reach the adjacent cell
                    # It's the current cost plus the cost of entering the adjacent cell
                    new_cost = min_cost[x][y] + grid[nx][ny]

                    # If the new cost is less than the previously known cost for this cell
                    # and is less than health (we cannot proceed if health is depleted)
                    if new_cost < min_cost[nx][ny] and new_cost < health:
                        # Update the minimum cost to reach the adjacent cell
                        min_cost[nx][ny] = new_cost

                        # If the adjacent cell is safe (grid[nx][ny] == 0)
                        if grid[nx][ny] == 0:
                            # Prioritize safe cells by adding them to the front of the deque
                            queue.appendleft((nx, ny))
                        else:
                            # Unsafe cells are added to the back of the deque
                            queue.append((nx, ny))

        # If we exit the loop without returning True, the destination is not reachable within the health constraints
        return False  # No viable path found