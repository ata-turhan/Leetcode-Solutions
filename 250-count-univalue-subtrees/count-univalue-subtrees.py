# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        # Define a recursive function to perform depth-first search (DFS)
        def dfs(node):
            # Base case: if the node is None, return 0 for count, -1001 for value, and True for unival
            if not node:
                return 0, -1001, True
            
            # Base case: if the node is a leaf node, return 1 for count, node value, and True for unival
            if not node.left and not node.right:
                return 1, node.val, True
            
            # Recursively calculate count, value, and unival for the left and right subtrees
            left_count, left_value, left_uni = dfs(node.left)
            right_count, right_value, right_uni = dfs(node.right)
            
            # Handle cases where one of the children is None
            left_value = right_value if left_value == -1001 else left_value
            right_value = left_value if right_value == -1001 else right_value
            
            # Check if the current node forms a unival subtree with its children
            if left_uni and right_uni and left_value == right_value == node.val:
                return 1 + left_count + right_count, node.val, True
            else:
                return left_count + right_count, node.val, False
        
        # Call the dfs function on the root node and return the count of unival subtrees
        return dfs(root)[0]
