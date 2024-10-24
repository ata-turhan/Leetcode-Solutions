# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def isFlipEquivalent(node1: Optional[TreeNode], node2: Optional[TreeNode]) -> bool:
            # If both nodes are None, they are equivalent
            if not node1 and not node2:
                return True
            # If one is None and the other is not, they are not equivalent
            if not node1 or not node2:
                return False
            # If their values are not the same, they are not equivalent
            if node1.val != node2.val:
                return False

            # Check if the left and right children are equivalent in flipped or unflipped form
            return (isFlipEquivalent(node1.left, node2.left) and isFlipEquivalent(node1.right, node2.right)) or \
                   (isFlipEquivalent(node1.left, node2.right) and isFlipEquivalent(node1.right, node2.left))

        # Start the recursion from the root nodes
        return isFlipEquivalent(root1, root2)
