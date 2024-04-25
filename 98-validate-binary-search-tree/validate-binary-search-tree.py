class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Helper function to recursively check if a subtree is a valid BST
        def solve(root, min_val, max_val):
            # Base case: empty subtree is a valid BST
            if not root:
                return True
            
            # Check if the current node's value is within the valid range
            if not (min_val < root.val < max_val):
                return False

            # Recursively check if the left subtree is a valid BST
            is_left_bst = solve(root.left, min_val, root.val)
            if not is_left_bst:
                return False
            
            # Recursively check if the right subtree is a valid BST
            is_right_bst = solve(root.right, root.val, max_val)
            
            # Return True if both left and right subtrees are valid BSTs
            return is_left_bst and is_right_bst 

        # Start the recursive check from the root node with initial minimum and maximum values
        return solve(root, float('-inf'), float('inf'))
