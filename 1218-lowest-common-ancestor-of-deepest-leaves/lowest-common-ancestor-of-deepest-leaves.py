# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lcaDeepestLeaves(self, root: Optional['TreeNode']) -> Optional['TreeNode']:
        def dfs(node):
            if not node:
                return (None, 0)
            left_lca, left_depth = dfs(node.left)
            right_lca, right_depth = dfs(node.right)
            if left_depth > right_depth:
                return (left_lca, left_depth + 1)
            elif right_depth > left_depth:
                return (right_lca, right_depth + 1)
            else:
                # When both depths are equal, current node is the LCA.
                return (node, left_depth + 1)
        
        return dfs(root)[0]
