# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        q = deque([root])
        even = True
        
        while q:
            level_length = len(q)
            prev = float('-inf') if even else float('inf')
            
            for _ in range(level_length):
                node = q.popleft()
                if (even and node.val % 2 == 1 and prev < node.val) or \
                (not even and node.val % 2 == 0 and prev > node.val):
                    prev = node.val
                else:
                    return False
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            even = not even
        
        return True

        