# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        prev_node = ListNode()
        prev_node.next = list1
        head = prev_node
        current_node = list1
        for _ in range(a):
            prev_node = prev_node.next
            current_node = current_node.next
        for _ in range(b - a):
            current_node = current_node.next
        prev_node.next = list2
        tail = list2
        while tail.next:
            tail = tail.next
        tail.next = current_node.next
        return head.next
