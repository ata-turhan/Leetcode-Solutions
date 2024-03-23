"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        new_node = Node(val=insertVal)
        if not head:
            new_node.next = new_node
            return new_node

        cur = head
        nodes = set()

        # Find the insertion position
        while cur.val <= cur.next.val:
            if cur in nodes:
                nxt = cur.next
                cur.next = new_node
                new_node.next = nxt
                return head
            nodes.add(cur)
            cur = cur.next

        # Insert the new node
        if new_node.val > cur.val or new_node.val < cur.next.val:
            smallest = cur.next
            cur.next = new_node
            new_node.next = smallest
            return head
        else:
            prev = cur
            cur = cur.next
            while cur.val < new_node.val:
                prev = cur
                cur = cur.next
            prev.next = new_node
            new_node.next = cur
            return head
        