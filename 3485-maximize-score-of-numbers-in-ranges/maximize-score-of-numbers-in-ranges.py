from typing import List

class Solution:
    def maxPossibleScore(self, start: List[int], d: int) -> int:
        # Sort the start array
        start.sort()

        # Initialize binary search boundaries
        left: int = 0
        right: int = start[-1] + d - start[0]  # max possible distance between two numbers
        max_score: int = 0

        # Perform binary search to find the maximum possible score
        while left <= right:
            mid: int = (left + right) // 2  # midpoint of current search range
            last_selected: int = start[0]   # Initialize with the first number in the sorted list
            is_valid: bool = True  # Flag to check if mid can be a valid score
            
            # Greedily check if we can select integers with at least 'mid' score
            for i in range(1, len(start)):
                # Check if the current number can be selected with at least 'mid' score
                if last_selected + mid <= start[i] + d:
                    last_selected = max(last_selected + mid, start[i])  # update the last selected number
                else:
                    is_valid = False
                    break  # If not possible, stop checking this value of 'mid'

            # If valid, we try to find a larger possible score
            if is_valid:
                max_score = mid  # Update max_score
                left = mid + 1  # Try for a larger score
            else:
                right = mid - 1  # Try for a smaller score

        return max_score
