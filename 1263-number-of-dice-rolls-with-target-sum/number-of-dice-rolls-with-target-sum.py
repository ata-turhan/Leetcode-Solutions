class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        MODULO = 10**9 + 7

        @cache
        def dfs(remaining_dice, num_sides, current_sum):
            # Base case: if the current sum equals the target and no dice are left
            if current_sum == target and remaining_dice == 0:
                return 1
            # Base case: if the current sum exceeds the target or no dice are left but target not met
            if current_sum > target or remaining_dice == 0:
                return 0

            total_ways = 0
            # Recursive case: explore each possible outcome of rolling a die
            for side in range(1, num_sides + 1):
                total_ways = (total_ways + dfs(remaining_dice - 1, num_sides, current_sum + side)) % MODULO
            return total_ways

        # Start the recursive search with all dice, the number of sides, and a current sum of 0
        return dfs(n, k, 0)
