# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: Optional[Node]) -> Optional[Node]:
        # Define a depth-first search (DFS) function to connect nodes on the same level
        def dfs(node):
            # Base case: if the node is None, return None
            if not node:
                return None
            
            # Store the next node on the same level
            next_node = node.next
            
            # Iterate to find the next non-null node on the same level
            while next_node and not (next_node.left or next_node.right):
                next_node = next_node.next
                
            # Connect the left and right child nodes
            if node.left and node.right:
                node.left.next = node.right
                if next_node:
                    node.right.next = next_node.left or next_node.right
            elif node.left and next_node:
                node.left.next = next_node.left or next_node.right
            elif node.right and next_node:
                node.right.next = next_node.left or next_node.right
            
            # Recursively call the DFS function on the right and left child nodes
            dfs(node.right)
            dfs(node.left)
            
            return node

        # Call the DFS function on the root node and return the root
        return dfs(root)
