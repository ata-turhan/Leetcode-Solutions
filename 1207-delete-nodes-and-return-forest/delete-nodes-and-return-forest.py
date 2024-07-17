# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        to_delete_set = set(to_delete)  # Convert to_delete list to a set for O(1) lookups
        forest = []  # List to store the roots of the trees in the remaining forest

        # If the root is not in to_delete, add it to the forest
        if root.val not in to_delete_set:
            forest.append(root)

        def postorder(parent, node):
            if not node:
                return
            # Traverse left and right subtrees first
            postorder(node, node.left)
            postorder(node, node.right)
            # If the current node needs to be deleted
            if node.val in to_delete_set:
                # Add the left and right children to the forest if they are not in to_delete
                if node.left and node.left.val not in to_delete_set:
                    forest.append(node.left)
                if node.right and node.right.val not in to_delete_set:
                    forest.append(node.right)
                # Disconnect the current node from its parent
                if parent:
                    if parent.left == node:
                        parent.left = None
                    else:
                        parent.right = None

        # Perform postorder traversal starting from the root
        postorder(None, root)

        return forest
