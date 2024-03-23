"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        
        # Dictionary to store original nodes as keys and corresponding copied nodes as values
        nodes = {}
        cur = head
        prev = None
        
        # First pass: create new nodes and link them together
        while cur:
            new_node = Node(x=cur.val)  # Create a new node with the same value as the original
            if prev:
                prev.next = new_node  # Link the new node to the previous node
            nodes[cur] = new_node  # Store the original node and its copy in the dictionary
            prev = new_node  # Update the previous node pointer
            cur = cur.next  # Move to the next node in the original list
        
        # Second pass: assign random pointers to copied nodes
        copy_cur = nodes[head]  # Start from the copied head node
        cur = head  # Start from the original head node
        while cur:
            # Assign random pointer to the copied node if the original node has one
            copy_cur.random = nodes[cur.random] if cur.random else None
            copy_cur = copy_cur.next  # Move to the next copied node
            cur = cur.next  # Move to the next original node
        
        # Return the head of the copied list
        return nodes[head]
