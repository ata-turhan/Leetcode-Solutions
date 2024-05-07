class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Reverse the linked list
        prev, cur = None, head
        while cur:
            cur.next, prev, cur = prev, cur, cur.next
        cur = prev
        
        # Traverse the reversed list and double the digits while considering carry
        carry = 0
        while cur.next:
            new_val = cur.val * 2 + carry
            carry = new_val // 10
            cur.val = new_val % 10
            cur = cur.next
        
        # Process the last node separately to handle any remaining carry
        new_val = cur.val * 2 + carry
        cur.val = new_val % 10
        carry = new_val // 10
        if carry > 0:
            new_node = ListNode(val=carry)
            cur.next = new_node
            cur = cur.next
        
        # Re-reverse the list to restore the original order
        head = cur
        prev, cur = None, prev
        while cur:
            cur.next, prev, cur = prev, cur, cur.next
        
        return head
