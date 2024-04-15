# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        # Define DFS helper function
        def dfs(node, num):
            # Base case: If node is None, return 0
            if not node:
                return 0
            # If node is a leaf, return the sum of the number formed
            if not node.left and not node.right:             
                return num * 10 + node.val
            # Recursively calculate sum for left and right subtrees
            left_sum = dfs(node.left, num * 10 + node.val)
            right_sum = dfs(node.right, num * 10 + node.val)
            return left_sum + right_sum
        
        # Start DFS from the root node with initial number 0
        return dfs(root, 0)
