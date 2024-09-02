from typing import List

class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        total_chalk = sum(chalk)  # Calculate the total amount of chalk needed for one full cycle
        k %= total_chalk  # Reduce k to the remainder when divided by total_chalk
        
        accumulated_chalk = 0  # Tracks the cumulative chalk used
        for index, chalk_needed in enumerate(chalk):
            accumulated_chalk += chalk_needed
            if k < accumulated_chalk:
                return index  # Return the index of the student who will use the last piece of chalk
