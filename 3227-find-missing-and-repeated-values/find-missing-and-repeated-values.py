from typing import List

class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        """Finds the repeated and missing numbers in the grid."""
        n = len(grid)
        num_count = {}
        repeated, missing = -1, -1

        # Count occurrences of each number
        for row in grid:
            for num in row:
                num_count[num] = num_count.get(num, 0) + 1
                if num_count[num] == 2:
                    repeated = num

        # Find the missing number
        for num in range(1, n**2 + 1):
            if num not in num_count:
                missing = num
                break

        return [repeated, missing]
