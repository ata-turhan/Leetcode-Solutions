# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        # Define a helper function for depth-first search (DFS)
        def dfs(current):
            # Base case: If the current node is None, return 0 coins
            if current is None:
                return 0, 0

            # Recursively calculate the number of coins and moves in the left subtree
            left_coins, left_moves = dfs(current.left)
            # Recursively calculate the number of coins and moves in the right subtree
            right_coins, right_moves = dfs(current.right)

            # Calculate the total moves needed for the current node
            total_moves = left_moves + right_moves + abs(left_coins) + abs(right_coins)

            # Calculate the number of coins current has available to exchange
            total_coins = (current.val - 1) + left_coins + right_coins

            # Return the total coins and moves for the current node
            return total_coins, total_moves

        # Start DFS from the root node
        _, total_moves = dfs(root)

        # Return the total number of moves required to distribute coins
        return total_moves
