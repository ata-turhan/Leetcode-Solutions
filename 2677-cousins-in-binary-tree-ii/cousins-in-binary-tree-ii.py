from collections import deque
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        # First pass to calculate the sum of each level
        node_queue = deque([root])
        level_sums = []

        while node_queue:
            level_size = len(node_queue)
            current_level_sum = 0

            # Traverse all nodes at the current level
            for _ in range(level_size):
                current_node = node_queue.popleft()
                current_level_sum += current_node.val
                if current_node.left:
                    node_queue.append(current_node.left)
                if current_node.right:
                    node_queue.append(current_node.right)
            
            # Store the sum of the current level
            level_sums.append(current_level_sum)

        # Second pass to modify the tree values based on level sums
        node_queue = deque([root])
        level = 0

        while node_queue:
            level_size = len(node_queue)
            # Calculate the sum for the next level (avoid out-of-range access)
            if level + 1 < len(level_sums):
                next_level_sum = level_sums[level + 1]
            else:
                next_level_sum = 0  # No more levels to process after this
            
            # Traverse all nodes at the current level
            for _ in range(level_size):
                current_node = node_queue.popleft()

                # Compute the sum of sibling values at the current level
                sibling_sum = 0
                if current_node.left:
                    sibling_sum += current_node.left.val
                    node_queue.append(current_node.left)
                if current_node.right:
                    sibling_sum += current_node.right.val
                    node_queue.append(current_node.right)

                # Update the node values as per problem's requirement
                if level == 0:
                    current_node.val = 0  # Root node value set to 0
                if current_node.left:
                    current_node.left.val = next_level_sum - sibling_sum
                if current_node.right:
                    current_node.right.val = next_level_sum - sibling_sum
            
            level += 1
            # Stop when we've processed all the levels
            if level >= len(level_sums) - 1:
                break

        return root
