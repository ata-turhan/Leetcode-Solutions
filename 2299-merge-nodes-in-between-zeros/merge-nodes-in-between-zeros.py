# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fill_node = head
        traverse_node = head.next 
        while True:
            while traverse_node.val != 0:
                fill_node.val += traverse_node.val
                traverse_node = traverse_node.next 
            traverse_node = traverse_node.next
            if not traverse_node:
                break
            else:
                fill_node = fill_node.next 
                fill_node.val = 0
        fill_node.next = None
        return head