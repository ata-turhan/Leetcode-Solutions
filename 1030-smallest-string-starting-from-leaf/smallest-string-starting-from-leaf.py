# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        # Define DFS helper function to traverse the tree and find the smallest string
        def dfs(node, path):
            # Base case: If node is None, return an empty string
            if not node:
                return ""
            # If leaf node is reached, convert path to string and return
            if not node.left and not node.right:
                path.append(node.val)
                return "".join(reversed(list((map(lambda i: chr(ord("a")+i), path)))))
            # Append current node value to the path
            path.append(node.val)
            # Recursively traverse left and right subtrees
            left_str = dfs(node.left, path.copy())
            right_str = dfs(node.right, path.copy())
            # Return the smallest string among left and right subtrees
            if left_str != "" and right_str != "":
                return min(left_str, right_str)
            else:
                return left_str or right_str

        # Initialize an empty path list and start DFS from the root
        path = []
        return dfs(root, path)
