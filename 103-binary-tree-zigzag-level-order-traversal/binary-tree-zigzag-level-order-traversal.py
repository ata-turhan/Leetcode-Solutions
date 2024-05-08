from collections import deque
from typing import List, Optional

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Check if the root is empty
        if not root:
            return []
        
        # Initialize the result list and deque for level order traversal
        res = []
        q = deque([root])
        reverse = False
        
        # Perform level order traversal
        while q:
            level = []
            length = len(q)
            for i in range(length):
                # Pop the nodes from left to right or right to left based on the 'reverse' flag
                if not reverse:
                    node = q.popleft()
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
                else:
                    node = q.pop()
                    if node.right:
                        q.appendleft(node.right)
                    if node.left:
                        q.appendleft(node.left)
                level.append(node.val)
            
            # Append the level to the result list
            res.append(level)
            reverse = not reverse
        
        return res


        #-----------------ANOTHER SOLUTION----------------------


        # Check if the root is empty
        if not root:
            return []
        
        # Initialize the result list, deque for level order traversal, and a counter
        res = []
        q = deque([root])
        c = 1
        
        # Perform level order traversal
        while q:
            level = []
            length = len(q)
            for i in range(length):
                # Pop nodes from the left and append their children
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                level.append(node.val)
            
            # Append the level to the result list based on the counter value
            if c % 2 == 0:
                res.append(level[::-1])  # Reverse the level list for even levels
            else:
                res.append(level)  # Keep the level list as is for odd levels
            
            # Increment the counter
            c += 1
        
        return res
        