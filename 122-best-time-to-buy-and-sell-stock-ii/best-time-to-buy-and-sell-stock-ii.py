class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0  # Initialize profit to 0
        # Iterate through the prices
        for i in range(1, len(prices)):
            # Add the positive difference between consecutive prices to profit
            profit += max(0, prices[i] - prices[i-1])
        return profit  # Return the total profit

            
        