from typing import List
import bisect

class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        # Sort items by price for efficient processing
        items.sort()
        
        # Dictionary to store maximum beauty at each price point
        max_beauty_by_price = {}
        
        # Populate max_beauty_by_price dictionary with highest beauty seen so far at each price
        for price, beauty in items:
            max_beauty_by_price[price] = beauty

        # Update max_beauty_by_price so each price has the maximum beauty up to that price
        highest_beauty = 0
        for price in max_beauty_by_price:
            highest_beauty = max(highest_beauty, max_beauty_by_price[price])
            max_beauty_by_price[price] = highest_beauty

        # Extract sorted list of prices for binary search
        sorted_prices = sorted(max_beauty_by_price)
        results = []
        
        # For each query, find the maximum beauty within the budget
        for budget in queries:
            # Locate the highest price within the budget
            index = bisect.bisect_right(sorted_prices, budget)
            if index == 0:
                results.append(0)  # No items affordable within budget
            else:
                results.append(max_beauty_by_price[sorted_prices[index - 1]])

        return results
