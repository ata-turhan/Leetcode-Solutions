from functools import cache

class Solution:
    def waysToReachStair(self, k: int) -> int:
        @cache
        def dp(stair: int, jump: int, came_down: bool) -> int:
            # If the current stair exceeds the allowed range, return 0 ways
            if stair > k + 1:
                return 0

            # Initialize ways to 0, unless we've reached exactly the k-th stair
            ways = 1 if stair == k else 0

            # If we haven't come down on the previous move, consider moving down
            if stair >= 1 and not came_down:
                ways += dp(stair - 1, jump, True)
            
            # Always consider moving up with the current jump value
            ways += dp(stair + (1 << jump), jump + 1, False)
            
            return ways

        # Start from stair 1 with an initial jump value of 0, and not having come down
        return dp(1, 0, False)
