# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, cur = None, head
        while cur:
            cur.next, prev, cur = prev, cur, cur.next
        cur = prev
        carry = 0
        while cur.next:
            new_val = cur.val * 2 + carry
            carry = new_val // 10
            cur.val = new_val % 10
            cur = cur.next
        new_val = cur.val * 2 + carry
        cur.val = new_val % 10
        carry = new_val // 10
        if carry > 0:
            new_node = ListNode(val=carry)
            cur.next = new_node
            cur = cur.next
        head = cur
        prev, cur = None, prev
        while cur:
            cur.next, prev, cur = prev, cur, cur.next
        return head

        