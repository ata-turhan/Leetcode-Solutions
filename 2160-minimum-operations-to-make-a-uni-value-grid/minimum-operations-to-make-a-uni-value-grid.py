from typing import List

class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        """Returns the minimum number of operations to make all elements equal, or -1 if impossible."""
        
        flattened = [cell for row in grid for cell in row]
        flattened.sort()
        median_value = flattened[len(flattened) // 2]
        total_operations = 0

        for value in flattened:
            diff = abs(value - median_value)
            if diff % x != 0:
                return -1
            total_operations += diff // x

        return total_operations
