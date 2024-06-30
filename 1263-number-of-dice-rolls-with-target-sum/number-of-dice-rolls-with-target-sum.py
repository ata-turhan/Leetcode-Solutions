class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        MODULO = 10**9 + 7

        @cache
        def dfs(remaining_dice, remaining_sides, current_sum, target_sum):
            if current_sum == target_sum and remaining_dice == 0:
                return 1
            if current_sum > target_sum or remaining_dice == 0:
                return 0

            total_ways = 0
            for side in range(1, remaining_sides + 1):
                total_ways = (total_ways + dfs(remaining_dice - 1, remaining_sides, current_sum + side, target_sum)) % MODULO
            return total_ways

        return dfs(n, k, 0, target)

 
