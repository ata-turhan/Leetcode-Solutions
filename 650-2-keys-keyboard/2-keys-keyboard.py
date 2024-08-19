from functools import lru_cache

class Solution:
    def minSteps(self, n: int) -> int:
        # Use lru_cache to memoize the results of the dp function for optimization
        @lru_cache(None)
        def dp(current_chars: int, copied_chars: int) -> int:
            # Base case: If we've reached exactly 'n' characters
            if current_chars == n:
                return 0
            # If we've exceeded 'n' characters, return an infinitely large value
            if current_chars > n:
                return float("inf")

            # If no characters have been copied yet (-1 indicates this), perform the first copy and paste operation
            if copied_chars == -1:
                return 2 + dp(current_chars * 2, current_chars)
            else:
                # Two options: paste the copied characters or copy all and paste
                paste_operation = 1 + dp(current_chars + copied_chars, copied_chars)
                copy_paste_operation = 2 + dp(current_chars * 2, current_chars)
                # Return the minimum number of steps between the two options
                return min(paste_operation, copy_paste_operation)

        # Start with 1 character on the notepad and no copied characters
        return dp(1, -1)
