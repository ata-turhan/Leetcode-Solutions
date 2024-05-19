# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def remove(node: Optional[TreeNode], target: int) -> Optional[TreeNode]:
            if not node:
                return None

            # Recursively remove leaf nodes in the left and right subtrees
            node.left = remove(node.left, target)
            node.right = remove(node.right, target)

            # Check if the current node is a leaf node with the target value
            if not node.left and not node.right and node.val == target:
                return None  # Remove this leaf node by returning None

            return node

        # Start the removal process from the root
        return remove(root, target)
