class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}

        def count_ways(coin_index, current_amount):
            # Base case: If the current amount is equal to the target amount, one valid way is found
            if current_amount == amount:
                return 1
            # If the current amount exceeds the target amount, no valid way is found
            if current_amount > amount:
                return 0
            # If all coins are used up without reaching the target amount, no valid way is found
            if coin_index == len(coins):
                return 0
            # Check if the result is already cached
            if (coin_index, current_amount) in memo:
                return memo[(coin_index, current_amount)]

            # Calculate the number of ways by including the current coin and excluding it
            memo[(coin_index, current_amount)] = count_ways(coin_index, current_amount + coins[coin_index]) + count_ways(coin_index + 1, current_amount)
            return memo[(coin_index, current_amount)]

        return count_ways(0, 0)
