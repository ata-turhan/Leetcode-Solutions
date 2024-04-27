from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Calculate the maximum profit that can be achieved from buying and selling stocks.

        Args:
            prices (List[int]): A list of stock prices.

        Returns:
            int: The maximum profit.
        """
        # Initialize variables
        left = 0         # Pointer to the leftmost position
        right = 1        # Pointer to the position one step to the right
        max_profit = 0   # Maximum profit
        
        # Loop through the prices array
        while right < len(prices):
            # If the price at the right position is greater than the price at the left position,
            # calculate the profit and update the max_profit if necessary
            if prices[right] > prices[left]:
                max_profit = max(max_profit, prices[right] - prices[left])
            else:
                # If the price at the right position is not greater, move the left pointer to the right position
                left = right
            # Move the right pointer to the next position
            right += 1
        
        # Return the maximum profit
        return max_profit
