from typing import List

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        if not prices:
            return 0
        
        n = len(prices)
        hold = -prices[0] - fee  # Maximum profit when holding a stock
        cash = 0  # Maximum profit when not holding a stock
        
        for i in range(1, n):
            hold = max(hold, cash - prices[i] - fee)  # Update the profit for holding a stock
            cash = max(cash, hold + prices[i])  # Update the profit for not holding a stock
        
        return cash

