class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # Helper function to recursively check if two subtrees are symmetric
        def dfs(left, right):
            # Base cases:
            # If both left and right subtrees are empty, they are symmetric
            if not left and not right:
                return True
            # If only one of the subtrees is empty, they are not symmetric
            if not left or not right:
                return False
            # If the values of the current nodes are different, the subtrees are not symmetric
            if left.val != right.val:
                return False
            # Recursively check if the children of the subtrees are symmetric
            return dfs(left.left, right.right) and dfs(left.right, right.left)

        # Start the recursive check from the left and right children of the root
        return dfs(root.left, root.right)
