# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return None
        while head and head.val == val:
            head = head.next
        if not head:
            return None
        prev = head
        cur = head.next
        while cur:
            if cur.val != val:
                prev.next = cur
                prev = prev.next
            cur = cur.next
        if prev.next:
            prev.next = None
        return head