# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return head

        # Reverse the linked list
        prev = None
        cur = head
        while cur:
            cur.next, prev, cur = prev, cur, cur.next
        tail = prev
        
        # Find the maximum value to the right and remove nodes with values smaller than max_val in the reversed list
        cur = prev
        max_val = float('-inf')  # Initialize max_val to negative infinity
        while cur:
            max_val = max(max_val, cur.val)
            while cur.next and cur.next.val < max_val:
                cur.next = cur.next.next
            cur = cur.next

        # Reverse the modified linked list back to its original order
        prev = None
        cur = tail
        while cur:
            cur.next, prev, cur = prev, cur, cur.next
        return prev
        