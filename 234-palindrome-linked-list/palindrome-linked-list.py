# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Check if the list is empty or has only one node, it's always a palindrome
        if not head or not head.next:
            return True
        
        # Find the middle of the linked list using the slow and fast pointers
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Reverse the second half of the linked list
        prev = None
        cur = slow
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        
        # Compare values of nodes from both halves of the linked list
        start = head
        end = prev
        while end:
            if start.val != end.val:
                return False
            start = start.next
            end = end.next
        
        # If all values match, it's a palindrome
        return True
        