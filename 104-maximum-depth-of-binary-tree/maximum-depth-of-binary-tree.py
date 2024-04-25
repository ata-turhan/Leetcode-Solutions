class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # If the tree is empty, return 0
        if not root:
            return 0
        
        # Recursively calculate the maximum depth of the left subtree
        left_d = self.maxDepth(root.left)
        
        # Recursively calculate the maximum depth of the right subtree
        right_d = self.maxDepth(root.right)
        
        # Return the maximum depth of the subtree rooted at the current node
        return max(left_d, right_d) + 1
