from typing import List, Optional

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []  # Initialize a stack to perform iterative inorder traversal
        node = root  # Initialize node as the current node starting from root
        res = []  # Initialize an empty list to store the inorder traversal result
        
        # Perform iterative inorder traversal using a stack
        while node or stack:
            while node:
                stack.append(node)  # Push nodes onto the stack until the leftmost node is reached
                node = node.left
            node = stack.pop()  # Pop the node from the stack
            res.append(node.val)  # Add the popped node's value to the result list
            node = node.right  # Move to the right child of the popped node
        
        return res  # Return the inorder traversal result
        
        # Recursive approach (not executed because of the return statement above)
        def traverse(root):
            if not root:
                return []
            res1 = traverse(root.left)
            res2 = traverse(root.right)
            return res1 + [root.val] + res2
        
        return traverse(root)  # Return the result of recursive inorder traversal
