# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        def search(root, target, min_val, max_val):
            if not root:
                return [-1, float("inf")]
            if root.val == target:
                return [root.val, 0]
            cur = [root.val, abs(root.val-target)]
            left, right = [-1, float("inf")], [-1, float("inf")]
            if root.val < target <= max_val:
                right = search(root.right, target, root.val, max_val)
            if min_val <= target < root.val:
                left = search(root.left, target, min_val, root.val)
            if left[1] <= right[1]:
                if left[1] <= cur[1]:
                    return left
                else:
                    return cur
            else:
                if cur[1] <= right[1]:
                    return cur
                else:
                    return right
        return search(root, target, float("-inf"), float("inf"))[0]

        