from typing import List
import math

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        """Finds the minimum time required to repair all cars using binary search."""

        def can_repair_all_cars(time_limit: int) -> bool:
            """Checks if it's possible to repair `cars` within `time_limit`."""
            total_repaired = sum(int(math.sqrt(time_limit // rank)) for rank in ranks)
            return total_repaired >= cars

        # Binary search range: Min time is 1, max is worst-case scenario (slowest worker repairing all)
        left, right = 1, min(ranks) * cars**2
        min_repair_time = right

        while left <= right:
            mid = left + (right - left) // 2
            if can_repair_all_cars(mid):
                min_repair_time = mid  # Update best known minimum time
                right = mid - 1  # Try for a smaller possible time
            else:
                left = mid + 1  # Increase time since current is insufficient

        return min_repair_time
