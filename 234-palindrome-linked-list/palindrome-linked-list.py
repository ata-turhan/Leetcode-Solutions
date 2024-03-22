# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head.next:
            return True
        middle_node = None
        prev_node = ListNode()
        prev_node.next = head
        slow = head
        fast = head
        while fast and fast.next:
            prev_node = slow
            slow = slow.next
            fast = fast.next.next  
        middle_node = slow
        prev_node.next = None
        prev_node = None
        if fast:
            slow = slow.next
        while slow:
            nxt = slow.next
            slow.next = prev_node
            prev_node = slow
            slow = nxt
        tail = prev_node
        cur = head
        res = True
        while cur:
            if cur.val != tail.val:
                res = False
                break
            cur = cur.next
            tail = tail.next
        return res

        
        
        