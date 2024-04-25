# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # Define a helper function to recursively create the balanced BST
        def create(l, r):
            # Base case: if left index exceeds right index, return None
            if l > r:
                return None
            
            # Calculate the middle index
            mid = l + (r-l) // 2
            
            # Create a new TreeNode with the value of the middle element
            root = TreeNode(nums[mid])
            
            # Recursively build the left and right subtrees
            root.left = create(l, mid - 1)
            root.right = create(mid + 1, r)
            
            return root
        
        # Call the helper function with the initial left and right indices
        return create(0, len(nums) - 1)
