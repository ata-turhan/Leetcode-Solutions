from collections import deque
from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        # Check if the root is empty
        if not root:
            return root
        
        # Initialize a deque for level order traversal and a list to store nodes at each level
        q = deque([root])
        levels = []
        
        # Perform level order traversal
        while q:
            level = []
            length = len(q)
            for _ in range(length):
                # Pop the nodes from the queue and append them to the current level list
                node = q.popleft()
                level.append(node)
                # Add the left and right children of the current node to the queue if they exist
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            # Connect nodes at the same level using the next pointer
            for i in range(length - 1):
                level[i].next = level[i + 1]
            level[length - 1].next = None
        
        return root
