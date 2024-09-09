# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        # Step 1: Initialize matrix filled with -1
        matrix = [[-1 for _ in range(n)] for _ in range(m)]
        
        # Step 2: Initialize boundaries
        top, bottom, left, right = 0, m - 1, 0, n - 1
        
        # Step 3: Traverse the linked list and fill the matrix
        current_node = head
        
        while top <= bottom and left <= right:
            # Traverse from left to right along the top row
            for col in range(left, right + 1):
                if current_node:
                    matrix[top][col] = current_node.val
                    current_node = current_node.next
                else:
                    return matrix
            top += 1  # Shrink the top boundary
            
            # Traverse from top to bottom along the right column
            for row in range(top, bottom + 1):
                if current_node:
                    matrix[row][right] = current_node.val
                    current_node = current_node.next
                else:
                    return matrix
            right -= 1  # Shrink the right boundary
            
            if top <= bottom:
                # Traverse from right to left along the bottom row
                for col in range(right, left - 1, -1):
                    if current_node:
                        matrix[bottom][col] = current_node.val
                        current_node = current_node.next
                    else:
                        return matrix
                bottom -= 1  # Shrink the bottom boundary
            
            if left <= right:
                # Traverse from bottom to top along the left column
                for row in range(bottom, top - 1, -1):
                    if current_node:
                        matrix[row][left] = current_node.val
                        current_node = current_node.next
                    else:
                        return matrix
                left += 1  # Shrink the left boundary
        
        return matrix