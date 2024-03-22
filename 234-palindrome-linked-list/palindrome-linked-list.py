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
        left = prev_node
        if fast:
            middle_node = slow
            right = slow.next
            slow = slow.next
        else:
            right = slow      
  
        prev_node.next = None
        prev_node = None
        
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

        prev = None
        cur = prev_node
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        if middle_node:
            left.next = middle_node
            middle_node.next = right
        else:
            left.next = right
        cur = head
        while cur:
            print(cur.val, end=" ")
            cur = cur.next
        return res

        
        
        