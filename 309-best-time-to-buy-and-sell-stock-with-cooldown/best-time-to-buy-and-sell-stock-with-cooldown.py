from typing import List
from functools import cache

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Dictionary to store the results of subproblems
        dp = {}  # key=(i, buying) val=max_profit

        def dfs(i: int, buying: bool) -> int:
            # Base case: If we've gone through all the prices
            if i >= len(prices):
                return 0
            
            # If the result for this subproblem is already computed, return it
            if (i, buying) in dp:
                return dp[(i, buying)]
            
            # Calculate the profit for the do_nothing state
            do_nothing = dfs(i + 1, buying)
            
            if buying:
                # If buying, calculate the profit if we buy at the current price
                buy = dfs(i + 1, not buying) - prices[i]
                dp[(i, buying)] = max(buy, do_nothing)
            else:
                # If selling, calculate the profit if we sell at the current price
                sell = dfs(i + 2, not buying) + prices[i]
                dp[(i, buying)] = max(sell, do_nothing)
            
            return dp[(i, buying)]
        
        # Start the DFS from the first day with the intention to buy
        return dfs(0, True)
