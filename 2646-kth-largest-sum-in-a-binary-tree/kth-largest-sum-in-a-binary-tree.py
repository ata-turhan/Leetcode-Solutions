from collections import deque
from heapq import heapify, heappop
from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        # Initialize a queue for level order traversal
        queue = deque()
        
        # Add root to the queue if it's not null
        if root:
            queue.append(root)
        
        level_sums = []  # List to store the sum of each level
        
        # Perform level order traversal
        while queue:
            level_size = len(queue)
            level_sum = 0  # Sum of the current level
            
            # Process all nodes at the current level
            for _ in range(level_size):
                node = queue.popleft()
                level_sum += node.val
                
                # Add children to the queue if they exist
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # Store the sum of the current level
            level_sums.append(level_sum)
        
        # If there are fewer levels than k, return -1
        if len(level_sums) < k:
            return -1
        
        # Convert the list to a min-heap
        heapify(level_sums)
        
        # Get the k-th largest element by popping the smallest ones
        index = len(level_sums) - k
        for _ in range(index):
            heappop(level_sums)

        # Return the k-th largest level sum
        return level_sums[0]
