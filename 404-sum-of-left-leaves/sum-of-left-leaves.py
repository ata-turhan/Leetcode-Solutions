class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        # Helper function to perform depth-first search (DFS)
        def dfs(node, is_left):
            # Base case: If node is None, return 0
            if not node:
                return 0
            # If node is a leaf and a left child, return its value
            if not node.left and not node.right:
                return node.val if is_left else 0
            # Recursively calculate sum of left leaves and right leaves
            return dfs(node.left, True) + dfs(node.right, False)

        # Start DFS traversal from the root node with is_left = False
        return dfs(root, False)
