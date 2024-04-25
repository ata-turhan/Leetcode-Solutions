from collections import deque
from typing import List, Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Check if the tree is empty
        if not root:
            return []

        result = []  # List to store the final result
        queue = deque([root])  # Queue to perform level order traversal

        # Iterate until the queue is empty
        while queue:
            current_level_values = []  # List to store values at the current level
            level_size = len(queue)  # Number of nodes in the current level
            
            # Process each node in the current level
            for _ in range(level_size):
                node = queue.popleft()  # Dequeue the front node
                current_level_values.append(node.val)  # Add its value to the current level list
                
                # Enqueue left and right children, if present
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            result.append(current_level_values)  # Add the current level list to the result list
        
        return result  # Return the final result
