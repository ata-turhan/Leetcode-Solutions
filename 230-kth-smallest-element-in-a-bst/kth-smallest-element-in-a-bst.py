# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Approach 1: Iterative Inorder Traversal
        order = 0  # Initialize the order of the current node
        stack = []  # Initialize a stack for iterative inorder traversal
        node = root  # Initialize node as the current node starting from root
        while stack or node:
            while node:
                stack.append(node)  # Push nodes onto the stack until the leftmost node is reached
                node = node.left
            node = stack.pop()  # Pop the node from the stack
            order += 1  # Increment the order
            if order == k:  # Check if the current node is the kth smallest
                return node.val  # Return the value of the kth smallest node
            node = node.right  # Move to the right child of the popped node

        # Return -1 if kth smallest node is not found
        return -1

        # Approach 2: Recursive Inorder Traversal
        res = []

        def inorder(root):
            if not root:
                return
            
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)
            
        inorder(root)
        return res[k-1]  # Return the kth smallest value found through inorder traversal
