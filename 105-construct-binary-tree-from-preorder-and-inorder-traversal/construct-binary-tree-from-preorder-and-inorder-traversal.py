from typing import List, Optional
from collections import deque

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Create a dictionary to store the index of each value in the inorder list
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        # Create a deque from the preorder list for efficient popping
        preorder_deque = deque(preorder)

        # Recursive function to build the tree
        def treeHelper(left, right):
            # Base case: if left index is greater than right index, return None
            if left > right:
                return None

            # Pop the leftmost value from the preorder deque as the current node value
            node_val = preorder_deque.popleft()
            # Create a TreeNode with the current node value
            root = TreeNode(node_val)

            # Find the index of the current node value in the inorder list
            inorder_index = inorder_map[node_val]

            # Recursively build the left subtree with values to the left of the current node in the inorder list
            root.left = treeHelper(left, inorder_index - 1)
            # Recursively build the right subtree with values to the right of the current node in the inorder list
            root.right = treeHelper(inorder_index + 1, right)

            return root

        # Start building the tree from the entire range of inorder list indices
        return treeHelper(0, len(inorder) - 1)
