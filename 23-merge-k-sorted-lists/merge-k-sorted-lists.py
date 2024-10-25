from sortedcontainers import SortedList

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, linked_lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not linked_lists:
            return None
        
        # Remove any empty lists from the input
        for i in range(len(linked_lists) - 1, -1, -1):
            if not linked_lists[i]:
                linked_lists.pop(i)

        # Create a dummy node to act as the head of the merged list
        dummy_head = ListNode()
        sorted_nodes = SortedList(linked_lists, key=lambda node: node.val)
        current_node = dummy_head

        # While there are nodes in the sorted list, continue merging
        while sorted_nodes and sorted_nodes[0]:
            # Add the smallest node to the current list
            current_node.next = sorted_nodes[0]
            current_node = sorted_nodes[0]
            next_node = sorted_nodes[0].next
            sorted_nodes.pop(0)  # Remove the smallest node

            # If the next node exists, add it to the sorted list
            if next_node is not None:
                sorted_nodes.add(next_node)

        # Return the merged list starting from the first real node
        return dummy_head.next
