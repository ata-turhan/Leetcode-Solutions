from collections import deque
from typing import List

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Modify rooms in-place to represent distances from gates to each room.
        
        Args:
            rooms (List[List[int]]): Matrix representing rooms and walls.
        """
        # Set to track visited cells
        visited = set()
        # Queue for BFS
        q = deque()

        # Find gates and add their positions to the queue
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:
                    visited.add((i, j))
                    q.append((i, j, 0))
        
        # Possible moves: up, right, down, left
        moves = [
            [-1, 0],  # Up
            [0, 1],   # Right
            [1, 0],   # Down
            [0, -1]   # Left
        ]

        # Perform BFS
        while q:
            i, j, dist = q.popleft()
            for move in moves:
                # Calculate new position
                ri, rj = i + move[0], j + move[1]
                # Check if the new position is valid and unvisited
                if ri in range(len(rooms)) and rj in range(len(rooms[0])) \
                and (ri, rj) not in visited and rooms[ri][rj] == 2**31-1:
                    # Mark as visited
                    visited.add((ri, rj))
                    # Update distance
                    rooms[ri][rj] = dist + 1
                    # Add new position to the queue
                    q.append((ri, rj, dist+1))
