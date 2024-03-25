from collections import deque
from typing import List

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        # Check if target is already at '0000'
        if target == "0000":
            return 0

        # Initialize the queue with the starting combination '0000'
        queue = deque()
        if "0000" not in deadends:
            queue.append(("0000", 0))
        
        # Set to track visited combinations
        visited = set()
        visited.add("0000")

        # Perform BFS
        while queue:
            node, dist = queue.popleft()

            # Generate possible next combinations by turning each wheel
            for i in range(4):
                # Rotate the wheel forward
                new_node1 = node[:i] + str((int(node[i]) + 1) % 10) + node[i+1:]
                # Rotate the wheel backward
                new_node2 = node[:i] + str((int(node[i]) - 1) % 10) + node[i+1:]

                # Check if the target combination is reached
                if new_node1 == target or new_node2 == target:
                    return dist + 1
                
                # Check if the next combination is not a deadend and not visited yet
                if new_node1 not in deadends and new_node1 not in visited:
                    visited.add(new_node1)
                    queue.append((new_node1, dist + 1))
                
                if new_node2 not in deadends and new_node2 not in visited:
                    visited.add(new_node2)
                    queue.append((new_node2, dist + 1))
        
        # Target combination cannot be reached
        return -1
