class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        @cache
        def dp(i, past_day):
            if i == len(days):
                return 0
            if days[i] <= past_day:
                return dp(i+1, past_day)
            else:
                min_cost = math.inf

                past_day1 = days[i] + 1 - 1
                cost = costs[0]
                min_cost = min(min_cost, cost + dp(i+1, past_day1))

                past_day7 = days[i] + 7 - 1
                cost = costs[1]
                min_cost = min(min_cost, cost + dp(i+1, past_day7))

                past_day30 = days[i] + 30 - 1
                cost = costs[2]
                min_cost = min(min_cost, cost + dp(i+1, past_day30))
            

            return min_cost

        return dp(0, 0)    