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
        prev_end_node = ListNode()
        prev_end_node.next = head
        slow_ptr = head
        fast_ptr = head
        
        while fast_ptr and fast_ptr.next:
            prev_end_node = slow_ptr
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next 
        
        left_end = prev_end_node
        
        if fast_ptr:
            middle_node = slow_ptr
            right_start = slow_ptr.next
            slow_ptr = slow_ptr.next
        else:
            right_start = slow_ptr      
    
        prev_end_node.next = None
        prev_end_node = None
        
        while slow_ptr:
            next_node = slow_ptr.next
            slow_ptr.next = prev_end_node
            prev_end_node = slow_ptr
            slow_ptr = next_node
        
        tail_ptr = prev_end_node
        curr_ptr = head
        is_palindrome = True
        
        while curr_ptr:
            if curr_ptr.val != tail_ptr.val:
                is_palindrome = False
                break
            curr_ptr = curr_ptr.next
            tail_ptr = tail_ptr.next

        prev_ptr = None
        curr_ptr = prev_end_node
        
        while curr_ptr:
            next_node = curr_ptr.next
            curr_ptr.next = prev_ptr
            prev_ptr = curr_ptr
            curr_ptr = next_node
        
        if middle_node:
            left_end.next = middle_node
            middle_node.next = right_start
        else:
            left_end.next = right_start
        
        return is_palindrome
        
        
        