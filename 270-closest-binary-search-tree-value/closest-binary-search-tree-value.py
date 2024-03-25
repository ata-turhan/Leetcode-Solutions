from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        def search(root, target, min_val, max_val):
            if not root:
                return -1, float("inf")
            
            if root.val == target:
                return root.val, 0
            
            cur_val = root.val
            cur_diff = abs(cur_val - target)
            
            left_val, left_diff = -1, float("inf")
            right_val, right_diff = -1, float("inf")
            
            if root.val < target <= max_val:
                right_val, right_diff = search(root.right, target, root.val, max_val)
                
            if min_val <= target < root.val:
                left_val, left_diff = search(root.left, target, min_val, root.val)
                
            if left_diff <= right_diff:
                if left_diff <= cur_diff:
                    return left_val, left_diff
                else:
                    return cur_val, cur_diff
            else:
                if cur_diff <= right_diff:
                    return cur_val, cur_diff
                else:
                    return right_val, right_diff
        
        return search(root, target, float("-inf"), float("inf"))[0]
