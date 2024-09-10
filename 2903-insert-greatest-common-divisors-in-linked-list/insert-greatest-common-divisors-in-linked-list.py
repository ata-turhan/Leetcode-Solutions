# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return head

        cur: Optional[ListNode] = head

        while cur.next:
            nxt = cur.next
            gcd = math.gcd(cur.val, nxt.val)
            new_node = ListNode(val=gcd, next=nxt)
            cur.next = new_node
            cur = nxt

        return head
        