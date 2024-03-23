# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        lengthA = 0
        curA = headA
        while curA:
            curA = curA.next
            lengthA += 1

        lengthB = 0
        curB = headB
        while curB:
            curB = curB.next
            lengthB += 1

        curA = headA
        curB = headB
        while lengthA > lengthB:
            curA = curA.next
            lengthA -= 1
        while lengthB > lengthA:
            curB = curB.next
            lengthB -= 1
        while curA and curB:
            if curA == curB:
                return curA
            curA = curA.next
            curB = curB.next

        return None

        