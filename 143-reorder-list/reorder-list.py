# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow_ptr = head
        fast_ptr = head
        while fast_ptr and fast_ptr.next:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
        # Reverse the second half of the linked list
        prev_ptr = slow_ptr
        cur_ptr = slow_ptr.next
        prev_ptr.next = None
        while cur_ptr:
            next_ptr = cur_ptr.next
            cur_ptr.next = prev_ptr
            prev_ptr = cur_ptr
            cur_ptr = next_ptr
        # Merge the two halves
        start_ptr = head
        end_ptr = prev_ptr
        while end_ptr.next:
            start_next = start_ptr.next
            end_next = end_ptr.next
            start_ptr.next = end_ptr
            end_ptr.next = start_next
            start_ptr = start_next
            end_ptr = end_next
        

            


        