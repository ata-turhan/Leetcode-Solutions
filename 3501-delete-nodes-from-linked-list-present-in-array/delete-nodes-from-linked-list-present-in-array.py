# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        # Create a set of values to be deleted
        values_to_delete = set(nums)

        # Ensure the head is not part of the values to delete
        while head and head.val in values_to_delete:
            head = head.next

        # Initialize pointers for previous and current nodes
        prev_node = head
        current_node = head.next if head else None

        # Iterate through the list
        while current_node:
            if current_node.val in values_to_delete:
                # Skip the current node if its value is in the delete set
                prev_node.next = current_node.next
            else:
                # Move the previous pointer to the current node
                prev_node = current_node

            # Move to the next node
            current_node = current_node.next

        return head
