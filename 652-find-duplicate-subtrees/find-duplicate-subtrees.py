# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        def post_order_dfs(root):
            if not root:
                return 0
            left_tree = post_order_dfs(root.left)
            right_tree = post_order_dfs(root.right)

            key = (left_tree, root.val, right_tree)
            tree_counts[key] += 1
            if tree_counts[key] == 2:
                res.append(root)
            return key

        res = []
        tree_counts = defaultdict(int)
        post_order_dfs(root)
        return res

        