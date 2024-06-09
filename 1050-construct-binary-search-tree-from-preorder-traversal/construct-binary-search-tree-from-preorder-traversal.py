# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        def buildBST(left_index, right_index):
            if left_index > right_index:
                return None
            if left_index == right_index:
                return TreeNode(preorder[left_index])

            root = TreeNode(preorder[left_index])
            
            # Find the first element greater than the root to split into left and right subtrees
            for split_index in range(left_index + 1, right_index + 1):
                if preorder[split_index] > preorder[left_index]:
                    break
            else:
                split_index = right_index + 1

            root.left = buildBST(left_index + 1, split_index - 1)
            root.right = buildBST(split_index, right_index)

            return root

        return buildBST(0, len(preorder) - 1)
