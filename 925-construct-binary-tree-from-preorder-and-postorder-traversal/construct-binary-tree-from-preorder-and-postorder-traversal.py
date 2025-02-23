from typing import List, Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        """Constructs a binary tree from preorder and postorder traversals."""
        
        def create_tree(pre_idx: int, post_start: int, post_end: int) -> Optional[TreeNode]:
            """Recursively reconstructs the tree."""
            if post_start > post_end:
                return None
            
            node = TreeNode(preorder[pre_idx])
            if post_start == post_end:
                return node  # Base case for single node
            
            left_val = preorder[pre_idx + 1]
            left_post_idx = postorder.index(left_val) 
            
            # Construct left and right subtrees
            node.left = create_tree(pre_idx + 1, post_start, left_post_idx)
            node.right = create_tree(pre_idx + left_post_idx - post_start + 2, left_post_idx + 1, post_end - 1)

            return node
        
        return create_tree(0, 0, len(postorder) - 1)
