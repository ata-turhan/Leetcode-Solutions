# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Check if the list is empty or contains only one node
        if not head or not head.next:
            return head
        
        # Calculate the length of the list
        length = 0
        cur = head
        while cur:
            cur = cur.next
            length += 1
        
        # Calculate the effective number of rotations
        k %= length
        
        # If k becomes 0, no rotation is needed
        if k == 0:
            return head
        
        # Initialize pointers for finding the new tail and head nodes
        prev = head
        tail = head
        
        # Move the tail pointer k steps forward
        for _ in range(k):
            tail = tail.next
        
        # Move both pointers until the tail reaches the end of the list
        while tail.next:
            prev = prev.next
            tail = tail.next
        
        # Disconnect the list at the appropriate point to form the new head
        new_head = prev.next
        prev.next = None
        
        # Connect the original tail to the original head to form a circular list
        tail.next = head
        
        # Return the new head of the rotated list
        return new_head

        


        