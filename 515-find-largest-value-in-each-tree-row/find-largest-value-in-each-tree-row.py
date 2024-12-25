from collections import deque
from typing import List, Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        """
        Find the largest value in each level of a binary tree.
        
        :param root: The root of the binary tree.
        :return: A list of the largest values in each tree level.
        """
        if not root:
            return []

        queue = deque([root])  # Queue for level-order traversal
        largest_values = []  # Result list to store largest values per level

        while queue:
            level_size = len(queue)
            max_value_in_level = float('-inf')  # Initialize to negative infinity for each level

            # Process all nodes at the current level
            for _ in range(level_size):
                current_node = queue.popleft()
                max_value_in_level = max(max_value_in_level, current_node.val)

                # Add child nodes to the queue
                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)

            largest_values.append(max_value_in_level)  # Store the largest value for this level

        return largest_values
