# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Initialize the result list to store the traversal output
        res = []
        
        # Helper function to perform postorder traversal
        def traverse(root, res):
            # Base case: if the current node is None, return immediately
            if not root:
                return
            
            # Recurse on the left subtree
            traverse(root.left, res)
            # Recurse on the right subtree
            traverse(root.right, res)
            # Visit the current node (add its value to the result list)
            res.append(root.val)
        
        # Start the traversal from the root node
        traverse(root, res)
        
        # Return the result list containing the postorder traversal
        return res
