from collections import defaultdict, deque
import heapq
from typing import List, Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        # Step 1: Calculate height of each node using DFS
        node_heights = {}  # Store the height of each node
        
        def calculate_height(node: Optional[TreeNode]) -> int:
            if not node:
                return -1  # Height of an empty subtree is -1
            left_height = calculate_height(node.left)
            right_height = calculate_height(node.right)
            node_height = 1 + max(left_height, right_height)
            node_heights[node.val] = node_height
            return node_height
        
        calculate_height(root)  # Populate node_heights dictionary

        # Step 2: Calculate levels and populate max-heaps for each level using BFS
        node_levels = {}  # Track the level of each node
        level_max_heights = defaultdict(list)  # Max-heaps for each level based on heights
        
        queue = deque([(root, 0)])  # (node, level)
        while queue:
            node, level = queue.popleft()
            node_levels[node.val] = level
            heapq.heappush(level_max_heights[level], (-node_heights[node.val], node.val))  # Negative for max-heap
            
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))

        # Step 3: Process each query
        results = []
        for node_val in queries:
            node_level = node_levels[node_val]
            node_height = node_heights[node_val]
            
            # Retrieve the max height for the current level
            max_height, max_node = heapq.heappop(level_max_heights[node_level])
            max_height = -max_height
            
            if max_height == node_height:
                # If queried node has the max height, check for second max
                if level_max_heights[node_level]:
                    second_max_height, second_max_node = heappop(level_max_heights[node_level])
                    max_height_after_removal = -second_max_height
                    heappush(level_max_heights[node_level], (second_max_height, second_max_node))
                else:
                    max_height_after_removal = -1
                # Push the original max back onto the heap
                heappush(level_max_heights[node_level], (-max_height, max_node))
            else:
                max_height_after_removal = max_height
                # Re-add max height back onto the heap
                heappush(level_max_heights[node_level], (-max_height, max_node))

            results.append(max_height_after_removal + node_level)

        return results
