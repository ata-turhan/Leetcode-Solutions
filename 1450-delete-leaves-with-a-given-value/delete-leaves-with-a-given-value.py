# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def remove(node, parent, target):
            if not node:
                return None

            remove(node.left, node, target)
            remove(node.right, node, target)

            if not node.left and not node.right and node.val == target:
                if not parent:
                    return None
                elif parent.left == node:
                    parent.left = None
                else:
                    parent.right = None


            return node

        return remove(root, None, target)

        
        