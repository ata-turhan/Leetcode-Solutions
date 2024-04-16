# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        # If depth is 1, create a new root node with given value and add current root as its left child
        if depth == 1:
            new_root = TreeNode(val)
            new_root.left = root
            return new_root
        else:
            # Define DFS helper function to traverse to the target depth and add nodes
            def dfs(node, val, depth):
                # Base case: If node is None, return
                if not node:
                    return
                # If target depth is reached, add new nodes with given value as left and right children
                if depth == 1:
                    new_left = TreeNode(val)
                    new_right = TreeNode(val)
                    new_left.left = node.left
                    new_right.right = node.right
                    node.left = new_left
                    node.right = new_right
                    return
                # Recursively traverse left and right subtrees with decremented depth
                dfs(node.left, val, depth - 1)
                dfs(node.right, val, depth - 1)
            
            # Start DFS from the root with depth decremented by 1
            dfs(root, val, depth - 1)
            return root
