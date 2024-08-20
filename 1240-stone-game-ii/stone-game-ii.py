from functools import lru_cache
from typing import List

class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        
        # Compute the prefix sum to quickly calculate the sum of any subarray
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + piles[i]

        # Helper function to get the sum of piles[i:j]
        def range_sum(i: int, j: int) -> int:
            return prefix_sum[j] - prefix_sum[i]

        # Use lru_cache to memoize results of dp function for efficiency
        @lru_cache(None)
        def dp(i: int, m: int, is_alice: bool) -> int:
            # Base case: No more stones to take
            if i >= n:
                return 0

            if is_alice:
                max_stones = 0
                # Alice takes the maximum possible stones
                for x in range(1, 2 * m + 1):
                    if i + x <= n:         
                        max_stones = max(max_stones, range_sum(i, i + x) + dp(i + x, max(m, x), False))
                return max_stones
            else:
                min_stones = float("inf")
                # Bob minimizes Alice's score
                for x in range(1, 2 * m + 1):
                    if i + x <= n:
                        min_stones = min(min_stones, dp(i + x, max(m, x), True))
                return min_stones

        # Start the game with Alice's turn, index 0, and initial m value of 1
        return dp(0, 1, True)


