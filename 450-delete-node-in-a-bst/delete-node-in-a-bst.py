# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # Base case: if the root is None, return None
        if not root:
            return None
        
        # If the key is found at the root node
        if root.val == key:
            # Case 1: If the node is a leaf node, return None
            if not root.left and not root.right:
                return None
            # Case 2: If the node has both left and right children
            elif root.left and root.right:
                parent = root.right
                # Find the leftmost node in the right subtree
                if not parent.left:
                    parent.left = root.left
                    return parent
                cur = parent
                while cur.left:
                    parent = cur
                    cur = cur.left
                # Replace the root with the leftmost node in the right subtree
                parent.left = cur.right
                cur.left = root.left
                cur.right = root.right
                return cur
            # Case 3: If the node has only one child
            else:
                return root.left or root.right
        # If the key is smaller than the root value, delete from the left subtree
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        # If the key is greater than the root value, delete from the right subtree
        else:
            root.left = self.deleteNode(root.left, key)
        
        return root
