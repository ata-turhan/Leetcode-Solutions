from typing import Optional, Set

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val: int = 0, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None):
        self.val = val
        self.left = left
        self.right = right

class FindElements:
    def __init__(self, root: Optional[TreeNode]):
        """Reconstructs the tree and stores all valid node values for quick lookup."""
        self.nodes: Set[int] = set()
        root.val = 0
        self._recover_tree(root)

    def _recover_tree(self, node: Optional[TreeNode]) -> None:
        """Performs DFS to reconstruct the tree with correct values."""
        if not node:
            return
        self.nodes.add(node.val)
        if node.left:
            node.left.val = 2 * node.val + 1
            self._recover_tree(node.left)
        if node.right:
            node.right.val = 2 * node.val + 2
            self._recover_tree(node.right)

    def find(self, target: int) -> bool:
        """Checks if a given value exists in the reconstructed tree."""
        return target in self.nodes
