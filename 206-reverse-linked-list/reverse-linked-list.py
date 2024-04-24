class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Check if the linked list is empty or contains only one node
        if not head or not head.next:
            return head
        
        # Initialize pointers
        previous_node = None
        current_node = head
        
        # Iterate through the linked list and reverse the links
        while current_node:
            # Store the next node before modifying the link
            next_node = current_node.next
            # Reverse the link
            current_node.next = previous_node
            # Move pointers for the next iteration
            previous_node = current_node
            current_node = next_node
        
        # Return the new head of the reversed linked list
        return previous_node
