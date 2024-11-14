from typing import List
import math

class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        # Helper function to check if a given max_size allows distribution to 'n' stores
        def can_distribute(max_size):
            required_stores = 0
            for quantity in quantities:
                # Calculate the number of stores needed if each store can have up to max_size items
                required_stores += math.ceil(quantity / max_size)
            return required_stores <= n

        # Initialize binary search bounds
        left, right = 1, max(quantities)
        minimized_maximum = right + 1

        # Binary search to find the minimum possible max size for each store
        while left <= right:
            mid = (left + right) // 2
            # If the current mid can be used as the max size for each store
            if can_distribute(mid):
                minimized_maximum = min(minimized_maximum, mid)
                right = mid - 1  # Try for a smaller maximum size
            else:
                left = mid + 1  # Increase mid to allow for larger store sizes

        return minimized_maximum
