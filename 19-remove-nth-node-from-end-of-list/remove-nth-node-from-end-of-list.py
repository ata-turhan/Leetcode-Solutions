class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Create a dummy node and set its next pointer to the head
        dummy = ListNode()
        dummy.next = head
        
        # Initialize slow and fast pointers to the dummy node
        slow = fast = dummy

        # Move the fast pointer ahead by n steps
        for _ in range(n):
            fast = fast.next

        # Move both slow and fast pointers until fast reaches the end
        while fast.next:
            slow = slow.next
            fast = fast.next

        # Remove the nth node from the end by updating the next pointer of the node before it
        slow.next = slow.next.next

        # Return the head of the modified linked list
        return dummy.next
