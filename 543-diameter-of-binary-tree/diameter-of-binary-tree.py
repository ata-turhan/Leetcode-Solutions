# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:    
        def dfs(root):
            if not root:
                return -1, -1
            left_path, left_max = dfs(root.left)
            right_path, right_max = dfs(root.right)
            return max(left_path, right_path) + 1, max(left_path + right_path + 2, left_max, right_max)

        result = dfs(root)[1]
        return result