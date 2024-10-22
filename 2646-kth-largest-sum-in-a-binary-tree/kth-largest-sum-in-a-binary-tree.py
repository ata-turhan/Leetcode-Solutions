from collections import deque
from heapq import heapify, heappop
from typing import Optional, List

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        # Initialize a queue for level-order traversal
        node_queue = deque()
        
        # Add root to the queue if it's not null
        if root:
            node_queue.append(root)
        
        level_sums = []  # List to store the sum of each level
        
        # Perform level-order traversal
        while node_queue:
            current_level_size = len(node_queue)
            current_level_sum = 0  # Sum of the current level
            
            # Process all nodes at the current level
            for _ in range(current_level_size):
                current_node = node_queue.popleft()
                current_level_sum += current_node.val
                
                # Add children to the queue if they exist
                if current_node.left:
                    node_queue.append(current_node.left)
                if current_node.right:
                    node_queue.append(current_node.right)
            
            # Store the sum of the current level
            level_sums.append(current_level_sum)
        
        # If there are fewer levels than k, return -1
        if len(level_sums) < k:
            return -1
        
        # Convert the list of level sums into a min-heap
        heapify(level_sums)
        
        # Get the k-th largest level sum by popping the smallest ones
        target_index = len(level_sums) - k
        for _ in range(target_index):
            heappop(level_sums)

        # Return the k-th largest level sum
        return level_sums[0]
