from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next

class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Helper function to compute the greatest common divisor (GCD)
        def gcd(a: int, b: int) -> int:
            if a < b:
                return gcd(b, a)  # Ensure a >= b
            if b == 0:
                return a  # Base case for GCD
            return gcd(b, a % b)

        # If the list has only one node, return the head
        if not head or not head.next:
            return head

        cur: Optional[ListNode] = head

        # Traverse the list and insert GCD nodes between each pair of nodes
        while cur and cur.next:
            nxt: Optional[ListNode] = cur.next
            gcd_val: int = gcd(cur.val, nxt.val)  # Compute GCD between cur and nxt node values
            new_node: ListNode = ListNode(val=gcd_val, next=nxt)  # Create a new node with the GCD value
            cur.next = new_node  # Insert the new node after cur
            cur = nxt  # Move to the next pair of nodes

        return head
