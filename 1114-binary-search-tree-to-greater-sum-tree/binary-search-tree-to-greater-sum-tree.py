# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def inverse_inorder(node, current_sum):
            if not node:
                return current_sum
            # Traverse the right subtree and update the current sum
            right_sum = inverse_inorder(node.right, current_sum)
            # Update the node value with the sum of greater values
            node.val += right_sum
            # Traverse the left subtree and update the current sum
            left_sum = inverse_inorder(node.left, node.val)
            return left_sum
        
        # Start the inverse inorder traversal with the initial sum as 0
        inverse_inorder(root, 0)
        return root
