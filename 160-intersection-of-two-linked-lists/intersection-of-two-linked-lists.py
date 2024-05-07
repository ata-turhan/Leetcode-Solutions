class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # Calculate the length of linked list A
        lengthA = 0
        curA = headA
        while curA:
            curA = curA.next
            lengthA += 1
        
        # Calculate the length of linked list B
        lengthB = 0
        curB = headB
        while curB:
            curB = curB.next
            lengthB += 1
        
        # Reset pointers to the heads of both linked lists
        curA = headA
        curB = headB
        
        # Move the pointer of the longer list to make them equal in length
        while lengthA > lengthB:
            curA = curA.next
            lengthA -= 1
        while lengthB > lengthA:
            curB = curB.next
            lengthB -= 1
        
        # Traverse both lists until the intersection point is found
        while curA and curB:
            if curA == curB:
                return curA
            curA = curA.next
            curB = curB.next
        
        return None
