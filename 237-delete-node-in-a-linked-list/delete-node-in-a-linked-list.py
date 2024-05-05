class Solution:
    def deleteNode(self, node):
        """
        Delete the given node from the linked list.

        Args:
        - node: The node to be deleted (of type ListNode).

        Returns:
        - None. Modifies the linked list in place.
        """
        # Iterate until the second-to-last node
        while node.next.next is not None:
            # Copy the value of the next node to the current node
            node.val = node.next.val
            # Move to the next node
            node = node.next

        # Copy the value of the last node to the current node
        node.val = node.next.val
        # Remove the last node by setting the next pointer to None
        node.next = None
