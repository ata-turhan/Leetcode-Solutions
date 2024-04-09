class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1, len(prices)):
            profit += max(0, prices[i]-prices[i-1])
        return profit 
        
        l = 0
        r = 1
        brought = prices[0]
        profit = 0
        while r < len(prices):
            if prices[r] <= brought:
                brought = prices[r]
            else:
                profit += prices[r] - brought
                brought = prices[r]
            r += 1
        return profit
            
        