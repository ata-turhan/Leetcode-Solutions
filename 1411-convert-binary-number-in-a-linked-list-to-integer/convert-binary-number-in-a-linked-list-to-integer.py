# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        num_str = []

        cur = head

        while cur:
            num_str.append(str(cur.val))
            cur = cur.next

        return int("".join(num_str), 2)
        