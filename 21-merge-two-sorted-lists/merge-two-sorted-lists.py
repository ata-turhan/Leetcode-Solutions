class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Check if either list is empty
        if not (list1 and list2):
            return list1 or list2
        
        # Determine the head of the merged list
        if list1.val > list2.val:
            head = list2
            list2 = list2.next
        else:
            head = list1
            list1 = list1.next
        
        # Initialize pointer for traversing the merged list
        cur = head
        
        # Merge the lists while comparing node values
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next
        
        # Append remaining nodes if any
        if list1 or list2:
            cur.next = list1 or list2
        
        # Return the head of the merged list
        return head
