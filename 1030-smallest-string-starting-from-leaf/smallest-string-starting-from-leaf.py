# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        def dfs(node, path):
            if not node:
                return ""
            if not node.left and not node.right:
                path.append(node.val)
                return "".join(reversed(list((map(lambda i: chr(ord("a")+i), path)))))
            path.append(node.val)
            left_str = dfs(node.left, path.copy())
            right_str = dfs(node.right, path.copy())
            if left_str != "" and right_str != "":
                return min(left_str, right_str)
            else:
                return left_str or right_str

        path = []
        return dfs(root, path)
        