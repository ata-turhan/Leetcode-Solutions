# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize a dummy head node to construct the result list
        dummy_head = ListNode(0)
        tail = dummy_head  # Initialize the tail node to track the end of the result list
        carry = 0  # Initialize the carry variable to handle sum overflow

        # Iterate until both input lists are exhausted and there is no carry
        while l1 or l2 or carry:
            # Extract digits from both input lists or set to 0 if the list has been exhausted
            digit1 = l1.val if l1 else 0
            digit2 = l2.val if l2 else 0

            # Calculate the sum of digits and carry
            sum_val = digit1 + digit2 + carry
            digit = sum_val % 10  # Extract the digit from the sum
            carry = sum_val // 10  # Calculate the carry for the next iteration

            # Create a new node with the calculated digit and append it to the result list
            new_node = ListNode(digit)
            tail.next = new_node
            tail = tail.next  # Move the tail pointer to the newly added node

            # Move to the next node in both input lists if they exist
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        result = dummy_head.next  # Extract the result list from the dummy head
        del dummy_head  # Delete the dummy head node to free up memory
        return result