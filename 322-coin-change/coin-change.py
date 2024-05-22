from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        # Initialize dp array with amount + 1, which is an impossibly high value
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0  # Base case: 0 coins are needed to make amount 0

        coins.sort()  # Sort the coins to enable early termination in the inner loop

        # Iterate over each amount from 1 to the target amount
        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
                else:
                    break  # No need to check larger coins

        # If dp[amount] is still amount + 1, it means it's not possible to form the amount with the given coins
        return dp[amount] if dp[amount] != amount + 1 else -1

# Example usage:
# sol = Solution()
# print(sol.coinChange([1, 2, 5], 11))  # Output: 3
