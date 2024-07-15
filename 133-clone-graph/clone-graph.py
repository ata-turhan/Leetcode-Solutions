"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from typing import Optional, Deque, Dict
from collections import deque

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        # Initialize the queue for BFS and a dictionary to store cloned nodes
        queue: Deque[Node] = deque([node])
        cloned_nodes: Dict[int, Node] = {node.val: Node(node.val, [])}
        
        # Perform BFS
        while queue:
            current_node = queue.popleft()
            current_clone = cloned_nodes[current_node.val]
            
            # Iterate through the neighbors of the current node
            for neighbor in current_node.neighbors:
                if neighbor.val not in cloned_nodes:
                    # Clone the neighbor if it hasn't been cloned yet
                    cloned_nodes[neighbor.val] = Node(neighbor.val, [])
                    queue.append(neighbor)
                
                # Add the cloned neighbor to the current clone's neighbors list
                current_clone.neighbors.append(cloned_nodes[neighbor.val])
                
        return cloned_nodes[node.val]
