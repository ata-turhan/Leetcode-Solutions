# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        # Base case: If the node is a leaf node, return its boolean value.
        if not root.left and not root.right:
            return bool(root.val)

        # Recursively evaluate the left and right subtrees.
        left_result = self.evaluateTree(root.left)
        right_result = self.evaluateTree(root.right)

        # If the node's value is 2, perform logical OR operation on the results of the subtrees.
        if root.val == 2:
            return left_result or right_result
        # If the node's value is 3, perform logical AND operation on the results of the subtrees.
        elif root.val == 3:
            return left_result and right_result
        # If the node's value is neither 2 nor 3, which should not happen in a valid input, return False.
        else:
            return False
