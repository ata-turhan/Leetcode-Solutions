class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 10**9 + 7  # Define the modulo constant
        
        # Use cache to memoize the results of the dp function
        @cache
        def dp(steps: int) -> int:
            # Base cases
            if steps == 0:
                return 1
            if steps == 1:
                return 1
            if steps == 2:
                return 2
            
            # Recurrence relation
            return (2 * dp(steps - 1) + dp(steps - 3)) % MOD
        
        return dp(n)  # Calculate the result for 'n' steps
