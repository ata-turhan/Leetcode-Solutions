from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next

class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        # Step 1: Calculate the total length of the linked list
        length: int = 0
        cur: Optional[ListNode] = head

        while cur:
            cur = cur.next
            length += 1

        # Step 2: Determine the base size of each part and the extra nodes to distribute
        base_size: int = length // k
        extras: int = length % k

        # Step 3: Store the sizes for each part
        part_sizes: List[int] = [base_size] * k
        for i in range(extras):
            part_sizes[i] += 1  # Distribute extra nodes evenly across the first parts

        # Step 4: Split the linked list into parts
        result: List[Optional[ListNode]] = []
        cur = head
        for size in part_sizes:
            result.append(cur)  # Start of the current part
            prev: Optional[ListNode] = None
            for _ in range(size):
                prev = cur
                if cur:
                    cur = cur.next
            if prev:
                prev.next = None  # Terminate the current part
        
        return result
