from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        # Base case: If head is None, the linked list is fully matched.
        if not head:
            return True
        
        # If root is None, but head is not None, there's no path, so return False.
        if not root:
            return False
        
        # Check if the current root can be the start of the subpath
        def dfs(head: ListNode, root: TreeNode) -> bool:
            if not head:
                return True  # Reached the end of the linked list, so it's a match
            if not root:
                return False  # Reached the end of the tree path without finishing the list
            if head.val != root.val:
                return False  # Values do not match, no valid path
            # Continue checking the left and right subtrees
            return dfs(head.next, root.left) or dfs(head.next, root.right)
        
        # Either the linked list starts at the current root, or it starts somewhere in the subtrees
        return dfs(head, root) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)
