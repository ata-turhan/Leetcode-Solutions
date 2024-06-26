# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        inorder_nodes = []
        def inorder(node):
            if not node:
                return

            inorder(node.left)
            inorder_nodes.append(node.val)
            inorder(node.right)

        inorder(root)

        def create_balanced_bst(array, l, r):
            if l > r:
                return None
            elif l == r:
                return TreeNode(val=array[l])

            mid = l + (r-l) // 2
            left_subtree = create_balanced_bst(array, l, mid-1)
            root = TreeNode(val=array[mid])
            right_subtree = create_balanced_bst(array, mid + 1, r)
            root.left = left_subtree
            root.right = right_subtree

            return root

        new_root = create_balanced_bst(inorder_nodes, 0, len(inorder_nodes)-1)
        return new_root

