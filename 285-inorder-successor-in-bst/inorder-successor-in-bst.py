# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        # Function to find the node and its path from the root
        def find_node(root, p, path):
            if not root:
                return path, False
            path.append(root)
            if root == p:
                return path, True
            left_dfs = find_node(root.left, p, path.copy())
            if left_dfs[1]:
                return left_dfs[0], True
            right_dfs = find_node(root.right, p, path.copy())
            if right_dfs[1]:
                return right_dfs[0], True
            return path, False
        
        # If p has a right child, find the leftmost child of its right subtree
        if p.right:
            cur = p.right
            while cur.left:
                cur = cur.left
            return cur

        # If p doesn't have a right child, find its parent
        path, found = find_node(root, p, [])
        if not found:
            return None
        
        # Traverse up the path to find the parent
        if len(path) == 1:
            return None  # No successor if p is the root
        child = path[-1]
        i = len(path) - 2
        while i > -1:
            parent = path[i]
            if parent.left == child:
                return parent  # Return the parent if p is its left child
            child = parent
            i -= 1
        return None  # Return None if p is the right child of its parent
