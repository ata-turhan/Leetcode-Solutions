from typing import List
from collections import deque

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        # If the tree is empty, return an empty list
        if not root:
            return []
        
        # Initialize a deque for level order traversal
        queue = deque()
        queue.append(root)
        
        # Initialize the result list
        result = []

        # Perform level order traversal using the queue
        while queue:
            # Get the number of nodes at the current level
            level_size = len(queue)
            # Initialize a list to store the values at the current level
            current_level = []
            # Process all nodes at the current level
            for _ in range(level_size):
                # Remove the node from the queue
                node = queue.popleft()
                # Append the node's value to the current level list
                current_level.append(node.val)
                # Add the children of the node to the queue
                if node.children:
                    queue.extend(node.children)
            # Append the current level list to the result list
            result.append(current_level)

        return result
