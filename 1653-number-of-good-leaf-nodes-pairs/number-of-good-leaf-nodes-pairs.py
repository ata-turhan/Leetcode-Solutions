# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def countPairs(self, root: Optional[TreeNode], distance: int) -> int:
        def dfs(node):
            # Base case: if the node is None, return no distances and 0 pairs
            if not node:
                return [], 0
            
            # Base case: if the node is a leaf, return distance 1 and 0 pairs
            if not node.left and not node.right:
                return [1], 0

            # Recursively get distances and pair counts from left and right subtrees
            left_distances, left_pairs = dfs(node.left)
            right_distances, right_pairs = dfs(node.right)

            # Initialize total pairs with pairs found in left and right subtrees
            total_pairs = left_pairs + right_pairs
            
            # Check pairs formed by nodes from left and right subtrees
            for left_distance in left_distances:
                for right_distance in right_distances:
                    if left_distance + right_distance <= distance:
                        total_pairs += 1

            # Increment distances by 1 for the current node and merge lists
            new_distances = [d + 1 for d in left_distances + right_distances]
            
            return new_distances, total_pairs

        # Call the dfs function starting from the root and get the total pairs
        _, result = dfs(root)
        return result
