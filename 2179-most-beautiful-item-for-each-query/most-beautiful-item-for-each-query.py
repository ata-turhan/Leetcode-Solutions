class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort()
        price_beauty = {}
        
        for price, beauty in items:
            price_beauty[price] = beauty

        best_beauty_so_far = 0
        for price, beauty in sorted(price_beauty.items()):
            best_beauty_so_far = max(best_beauty_so_far, beauty)
            price_beauty[price] = best_beauty_so_far

        prices = sorted(price for price in price_beauty)
        res = []
        for query in queries:
            q_idx = bisect.bisect_right(prices, query)
            if q_idx == 0:
                res.append(0)
            else:
                res.append(price_beauty[prices[q_idx-1]])

        return res


        
        