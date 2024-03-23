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
        def return_head_tail(head):
            if not head:
                return [None, None]
            cur = head
            prev = None
            while cur:
                nxt = cur.next
                prev = cur
                if cur.child:
                    new_head, new_tail = return_head_tail(cur.child)
                    cur.next = new_head
                    new_head.prev = cur
                    new_tail.next = nxt
                    if nxt:
                        nxt.prev = new_tail 
                    cur.child = None   
                    prev = new_tail
                cur = nxt
            return head, prev
        return return_head_tail(head)[0]
        