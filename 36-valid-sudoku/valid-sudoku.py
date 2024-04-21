from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        if not board:
            return True
        
        rows = [set() for _ in range(9)]  # Initialize sets to store values for each row
        cols = [set() for _ in range(9)]  # Initialize sets to store values for each column
        boxes = [set() for _ in range(9)]  # Initialize sets to store values for each 3x3 box
        
        for i in range(9):
            for j in range(9):
                el = board[i][j]
                if el == ".":
                    continue
                box_number = (i // 3) * 3 + j // 3  # Determine the box number for the current element
                
                # Check if the current element is already present in the same row, column, or box
                if el in rows[i] or el in cols[j] or el in boxes[box_number]:
                    return False
                
                # Add the current element to the respective row, column, and box sets
                rows[i].add(el)
                cols[j].add(el)
                boxes[box_number].add(el)
        
        return True  # If no conflicts are found, return True
