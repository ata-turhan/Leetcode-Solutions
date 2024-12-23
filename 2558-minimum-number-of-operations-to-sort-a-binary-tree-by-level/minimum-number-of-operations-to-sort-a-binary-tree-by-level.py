from collections import deque
from typing import List, Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        """
        Calculate the minimum number of operations required to make the binary tree 
        level-wise sorted by performing minimum swaps on each level.
        """
        def min_swaps_to_sort(arr: List[int]) -> int:
            """
            Calculate the minimum number of swaps required to sort an array.
            
            :param arr: List of integers representing values at a tree level.
            :return: Minimum number of swaps to sort the array.
            """
            n = len(arr)
            indexed_array = [(value, idx) for idx, value in enumerate(arr)]
            indexed_array.sort()  # Sort by value to determine target positions.
            visited = [False] * n
            swaps = 0

            for i in range(n):
                # Skip if already in correct position or visited in another cycle
                if visited[i] or indexed_array[i][1] == i:
                    continue
                
                # Count the size of the cycle
                cycle_size = 0
                j = i
                while not visited[j]:
                    visited[j] = True
                    j = indexed_array[j][1]
                    cycle_size += 1
                
                # For a cycle of size `k`, `k-1` swaps are required
                if cycle_size > 1:
                    swaps += cycle_size - 1
            
            return swaps

        if not root:
            return 0  # No operations needed for an empty tree.

        queue = deque([root])
        total_operations = 0

        # Level-order traversal to process each level of the tree
        while queue:
            level_size = len(queue)
            level_values = []

            # Collect all node values at the current level
            for _ in range(level_size):
                current_node = queue.popleft()
                level_values.append(current_node.val)
                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)

            # Add minimum swaps required to sort the current level
            total_operations += min_swaps_to_sort(level_values)
        
        return total_operations
