# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def isFlipEqual(node1, node2):
            if not (node1 and node2):
                return not (node1 or node2)
            
            if node1.val != node2.val:
                return False

            return (isFlipEqual(node1.left, node2.left) and isFlipEqual(node1.right, node2.right)) or (isFlipEqual(node1.left, node2.right) and isFlipEqual(node1.right, node2.left))

        return isFlipEqual(root1, root2)     