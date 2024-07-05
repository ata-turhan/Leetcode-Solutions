# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        critical_points = []

        prev_prev_val = None
        prev_val = None
        cur = head
        i = -1
        while cur:
            if i < 1:
                pass
            elif prev_prev_val < prev_val and prev_val > cur.val:
                critical_points.append(i)
            elif prev_prev_val > prev_val and prev_val < cur.val:
                critical_points.append(i)
    
            prev_prev_val = prev_val 
            prev_val = cur.val
            cur = cur.next
            i += 1

        if len(critical_points) < 2:
            return [-1, -1]
        else:
            min_diff = float("inf")
            for i in range(1, len(critical_points)):
                if critical_points[i] - critical_points[i-1] < min_diff:
                    min_diff =    critical_points[i] - critical_points[i-1]

            max_diff = critical_points[-1] - critical_points[0]

            return [min_diff, max_diff] 
