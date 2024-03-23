"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        def flatten_sublist(node):
            if not node:
                return None, None  # Return None for both head and tail if node is None
            cur = node
            prev = None
            while cur:
                next_node = cur.next
                prev = cur
                if cur.child:
                    # Recursively flatten the child sublist
                    child_head, child_tail = flatten_sublist(cur.child)
                    # Connect the flattened child sublist with the current node and its next node
                    cur.next = child_head
                    child_head.prev = cur
                    child_tail.next = next_node
                    if next_node:
                        next_node.prev = child_tail
                    # Remove the child reference from the current node
                    cur.child = None
                    # Update the previous node pointer to the tail of the flattened sublist
                    prev = child_tail
                cur = next_node
            return node, prev  # Return the head and tail of the flattened sublist

        return flatten_sublist(head)[0]  # Return the head of the fully flattened list