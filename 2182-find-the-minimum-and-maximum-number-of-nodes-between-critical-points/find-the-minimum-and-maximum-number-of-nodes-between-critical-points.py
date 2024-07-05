# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        critical_points = []
        
        # Initial values for previous and current nodes
        prev_prev_val = None
        prev_val = None
        current_node = head
        index = -1

        # Traverse the linked list to find critical points
        while current_node:
            if index >= 1:
                if prev_prev_val < prev_val and prev_val > current_node.val:
                    critical_points.append(index)
                elif prev_prev_val > prev_val and prev_val < current_node.val:
                    critical_points.append(index)

            # Update previous values and move to the next node
            prev_prev_val = prev_val
            prev_val = current_node.val
            current_node = current_node.next
            index += 1

        # If less than two critical points, return [-1, -1]
        if len(critical_points) < 2:
            return [-1, -1]

        # Calculate minimum and maximum distances between critical points
        min_diff = float("inf")
        for i in range(1, len(critical_points)):
            min_diff = min(min_diff, critical_points[i] - critical_points[i - 1])

        max_diff = critical_points[-1] - critical_points[0]

        return [min_diff, max_diff]
