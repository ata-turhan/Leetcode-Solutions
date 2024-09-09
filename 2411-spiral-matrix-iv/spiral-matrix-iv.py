from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next

class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        # Step 1: Initialize a matrix filled with -1 (default values)
        matrix: List[List[int]] = [[-1] * n for _ in range(m)]
        
        # Step 2: Initialize the boundary pointers for the spiral traversal
        top, bottom, left, right = 0, m - 1, 0, n - 1
        
        # Step 3: Pointer to traverse the linked list
        current_node: Optional[ListNode] = head
        
        # Step 4: Traverse the matrix in a spiral order
        while top <= bottom and left <= right:
            # Traverse from left to right along the top row
            for col in range(left, right + 1):
                if current_node:
                    matrix[top][col] = current_node.val
                    current_node = current_node.next
                else:
                    return matrix  # If the list ends, return the matrix
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
