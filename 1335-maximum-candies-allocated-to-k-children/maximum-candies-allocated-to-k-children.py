from typing import List

class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        """Finds the maximum number of candies each child can get using binary search."""
        
        def can_distribute(min_candies: int) -> bool:
            """Checks if it's possible to distribute at least `min_candies` to each of the `k` children."""
            total_children_served = sum(candy // min_candies for candy in candies)
            return total_children_served >= k

        # Binary search to find the maximum possible candy per child
        left, right = 1, max(candies)
        max_possible_candies = 0

        while left <= right:
            mid = left + (right - left) // 2
            if can_distribute(mid):
                max_possible_candies = mid  # Update result
                left = mid + 1  # Try for a larger possible amount
            else:
                right = mid - 1  # Reduce the search space

        return max_possible_candies
