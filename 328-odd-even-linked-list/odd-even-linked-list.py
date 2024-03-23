# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Check if the list is empty or has less than 3 nodes
        if not head or not head.next or not head.next.next:
            return head
        
        # Initialize pointers for odd and even nodes
        odd = head
        even_head = head.next
        even = even_head
        
        # Traverse the list, rearranging odd and even nodes
        while even and even.next:
            # Connect odd nodes
            odd.next = even.next
            odd = odd.next
            # Connect even nodes
            even.next = odd.next
            even = even.next
        
        # Connect the last odd node to the head of even nodes
        odd.next = even_head
        
        return head
        