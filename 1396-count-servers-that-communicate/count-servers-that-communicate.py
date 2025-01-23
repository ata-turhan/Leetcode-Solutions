from typing import List

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        """
        Count the number of servers that can communicate with at least one other server.
        
        :param grid: List[List[int]] - 2D grid where 1 represents a server and 0 represents an empty space.
        :return: int - The count of servers that can communicate.
        """
        # Get the dimensions of the grid
        rows, cols = len(grid), len(grid[0])
        
        # Track server positions in each row and column
        servers_in_row = [set() for _ in range(rows)]
        servers_in_col = [set() for _ in range(cols)]
        
        # To store all servers that can communicate
        communicated_servers = set()
        
        # Populate row and column server sets
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    servers_in_row[row].add((row, col))
                    servers_in_col[col].add((row, col))
        
        # Check rows for communication
        for row in range(rows):
            if len(servers_in_row[row]) > 1:  # More than one server can communicate
                communicated_servers.update(servers_in_row[row])
        
        # Check columns for communication
        for col in range(cols):
            if len(servers_in_col[col]) > 1:  # More than one server can communicate
                communicated_servers.update(servers_in_col[col])
        
        # Return the total number of communicated servers
        return len(communicated_servers)
