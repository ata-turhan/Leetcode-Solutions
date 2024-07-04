# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current_fill_node = head  # Node to accumulate sum values
        current_traverse_node = head.next  # Node to traverse the list
        
        while current_traverse_node:
            # Sum the values until we encounter a zero
            while current_traverse_node.val != 0:
                current_fill_node.val += current_traverse_node.val
                current_traverse_node = current_traverse_node.next 
            
            # Move to the next segment after zero
            current_traverse_node = current_traverse_node.next
            
            # If end of the list is reached, break the loop
            if not current_traverse_node:
                break
            
            # Move the fill node to the next position and reset its value to zero
            current_fill_node = current_fill_node.next 
            current_fill_node.val = 0
        
        # Remove all nodes after the last filled node
        current_fill_node.next = None
        
        return head
