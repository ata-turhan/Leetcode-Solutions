from collections import deque
from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Reverse the values of nodes at all odd levels of a binary tree.
        
        :param root: The root of the binary tree.
        :return: The root of the modified binary tree with reversed odd levels.
        """
        if not root:
            return None

        # Initialize a queue for level-order traversal
        queue = deque([root])
        current_level = 0  # Tracks the current level in the tree

        while queue:
            level_size = len(queue)
            current_level_nodes = []

            # Process nodes at the current level
            for _ in range(level_size):
                node = queue.popleft()
                # Collect nodes for reversal at odd levels
                if current_level % 2 == 1:
                    current_level_nodes.append(node)
                # Add children to the queue for the next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # Reverse node values if the level is odd
            if current_level % 2 == 1 and current_level_nodes:
                for i in range(len(current_level_nodes) // 2):
                    left_node = current_level_nodes[i]
                    right_node = current_level_nodes[-i - 1]
                    # Swap values
                    left_node.val, right_node.val = right_node.val, left_node.val

            current_level += 1  # Increment the level counter

        return root
