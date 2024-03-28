# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        """
        Finds the maximum depth of an N-ary tree recursively.

        Args:
            root ('Node'): The root node of the N-ary tree.

        Returns:
            int: The maximum depth of the N-ary tree.
        """
        if not root:
            return 0
        
        # Initialize the depth of the current node to 1
        depth = 1
        # Recursively find the maximum depth of each child node
        for child in root.children:
            depth = max(depth, self.maxDepth(child) + 1)
        
        return depth
