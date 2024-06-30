class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        # Cache to store the minimum cost for traveling starting from index i and valid until past_day
        @cache
        def dp(i, valid_until):
            if i == len(days):
                return 0  # No more days to travel

            if days[i] <= valid_until:
                return dp(i + 1, valid_until)  # Current day is covered by a previous pass

            min_cost = math.inf
            
            # 1-day pass
            next_valid_until = days[i]
            min_cost = min(min_cost, costs[0] + dp(i + 1, next_valid_until))
            
            # 7-day pass
            next_valid_until = days[i] + 6
            min_cost = min(min_cost, costs[1] + dp(i + 1, next_valid_until))
            
            # 30-day pass
            next_valid_until = days[i] + 29
            min_cost = min(min_cost, costs[2] + dp(i + 1, next_valid_until))

            return min_cost

        return dp(0, 0)  # Start from the first day with no valid pass initially
