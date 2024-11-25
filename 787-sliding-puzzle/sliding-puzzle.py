from typing import List
from collections import deque

class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        # Define the target state and the possible moves
        target = "123450"
        start = "".join(str(num) for row in board for num in row)  # Flatten the board into a string
        directions = {
            0: [1, 3],
            1: [0, 2, 4],
            2: [1, 5],
            3: [0, 4],
            4: [1, 3, 5],
            5: [2, 4]
        }

        # Perform BFS
        queue = deque([(start, start.index("0"), 0)])  # (current state, index of 0, steps)
        visited = set()
        visited.add(start)

        while queue:
            current_state, zero_index, steps = queue.popleft()
            
            # Check if the current state matches the target
            if current_state == target:
                return steps

            # Try all possible moves
            for move in directions[zero_index]:
                new_state = list(current_state)
                new_state[zero_index], new_state[move] = new_state[move], new_state[zero_index]
                new_state_str = "".join(new_state)
                
                if new_state_str not in visited:
                    visited.add(new_state_str)
                    queue.append((new_state_str, move, steps + 1))

        # If no solution is found
        return -1
