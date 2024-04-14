# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def sum_left_leaves(parent, child):
            if child is None:
                return 0
            if child.left is None and child.right is None:
                if parent is not None and parent.left == child:
                    return child.val
            parent = child
            return sum_left_leaves(parent, parent.left) + sum_left_leaves(parent, parent.right) 

        return sum_left_leaves(None, root)
        