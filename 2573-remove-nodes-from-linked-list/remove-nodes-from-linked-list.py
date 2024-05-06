# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return head
        prev = None
        cur = head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        tail = prev
        max_val = tail.val
        cur = tail
        while cur:
            max_val = max(max_val, cur.val)
            while cur.next and cur.next.val < max_val:
                cur.next = cur.next.next
            cur = cur.next
        prev = None
        cur = tail
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        return prev
        