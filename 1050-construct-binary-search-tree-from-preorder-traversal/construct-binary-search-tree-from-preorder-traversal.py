# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        def create(left, right):
            if left > right:
                return None
            if left == right:
                return TreeNode(preorder[left])

            root = TreeNode(preorder[left])
            
            # Find the first element greater than the root to split into left and right subtrees
            for i in range(left + 1, right + 1):
                if preorder[i] > preorder[left]:
                    break
            else:
                i = right + 1

            root.left = create(left + 1, i - 1)
            root.right = create(i, right)

            return root

        return create(0, len(preorder) - 1)
