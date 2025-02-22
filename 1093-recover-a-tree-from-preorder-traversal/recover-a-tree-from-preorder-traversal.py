# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        stack = []  # will hold nodes corresponding to the current path
        i = 0
        while i < len(traversal):
            level = 0
            # Count dashes to determine the depth of the node
            while i < len(traversal) and traversal[i] == '-':
                level += 1
                i += 1
            
            # Read the numeric value of the node
            j = i
            while j < len(traversal) and traversal[j].isdigit():
                j += 1
            val = int(traversal[i:j])
            i = j  # move to the next part of the string
            
            # Create a new TreeNode
            node = TreeNode(val)
            
            # Adjust the stack to match the current depth
            while len(stack) > level:
                stack.pop()
            
            # Attach the new node to the correct parent node if it exists
            if stack:
                if stack[-1].left is None:
                    stack[-1].left = node
                else:
                    stack[-1].right = node
            
            # Push the current node onto the stack
            stack.append(node)
        
        # The root of the tree is at the bottom of the stack (first element)
        return stack[0] if stack else None