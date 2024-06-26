# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        sorted_values = []
        
        # Perform an inorder traversal to collect the node values in sorted order
        def inorder_traversal(node):
            if not node:
                return
            inorder_traversal(node.left)
            sorted_values.append(node.val)
            inorder_traversal(node.right)

        inorder_traversal(root)

        # Create a balanced BST from the sorted array of node values
        def build_balanced_bst(values, left, right):
            if left > right:
                return None
            mid = left + (right - left) // 2
            new_root = TreeNode(val=values[mid])
            new_root.left = build_balanced_bst(values, left, mid - 1)
            new_root.right = build_balanced_bst(values, mid + 1, right)
            return new_root

        # Generate the balanced BST
        balanced_root = build_balanced_bst(sorted_values, 0, len(sorted_values) - 1)
        return balanced_root
