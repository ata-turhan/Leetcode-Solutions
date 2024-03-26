from collections import defaultdict
from typing import List, Optional

# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        # Function for post-order traversal with DFS
        def post_order_dfs(root):
            if not root:
                return "#"
            
            # Serialize left and right subtrees
            left_tree = post_order_dfs(root.left)
            right_tree = post_order_dfs(root.right)
            
            # Serialize the current subtree
            key = (left_tree, root.val, right_tree)
            
            # Count occurrences of the subtree
            tree_counts[key] += 1
            
            # Add the root node to the result if it's the second occurrence of the subtree
            if tree_counts[key] == 2:
                res.append(root)
            
            return key
        
        res = []  # Initialize list to store duplicate subtrees
        tree_counts = defaultdict(int)  # Initialize dictionary to store counts of subtrees
        post_order_dfs(root)  # Perform post-order traversal with DFS
        return res  # Return the list of duplicate subtrees
