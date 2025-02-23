# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def create_tree(preorder, postorder):
            if not preorder:
                return None
            elif len(preorder) == 1:
                return TreeNode(preorder[0])
            else:
                node = TreeNode(preorder[0])
                left_node = preorder[1]
                idx_left_node = postorder.index(left_node)
                right_node = postorder[-2]
                idx_right_node = preorder.index(right_node)
                left_size = idx_right_node - 1
                node.left = create_tree(preorder[1:idx_right_node], postorder[:left_size])
                node.right = create_tree(preorder[1 + left_size:], postorder[left_size:-1])
                return node

        return create_tree(preorder, postorder)
        