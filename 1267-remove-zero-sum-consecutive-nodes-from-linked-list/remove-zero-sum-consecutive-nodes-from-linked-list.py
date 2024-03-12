# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummyNode = ListNode(0, next=head)
        prefix_sum = {0:dummyNode}
        cur_sum = 0
        cur = head
        while cur:
            cur_sum += cur.val
            if cur_sum in prefix_sum:
                start_node = prefix_sum[cur_sum]
                node = start_node.next
                del_sum = cur_sum 
                while node != cur:
                    del_sum += node.val
                    del prefix_sum[del_sum]
                    node = node.next
                start_node.next = cur.next
            else:
                prefix_sum[cur_sum] = cur
            cur = cur.next
        return dummyNode.next