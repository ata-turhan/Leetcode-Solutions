class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        @cache
        def dp(i, prev, negs):
            if i == len(houses):
                if negs == target:
                    return 0
                else:
                    return float("inf")

            if houses[i] != 0:
                if houses[i] == prev:
                    return dp(i+1, houses[i], negs)
                else:
                    return dp(i+1, houses[i], negs+1)

            min_cost = float("inf")
            for color in range(len(cost[0])):
                if (color + 1) != prev:
                    cur_cost = cost[i][color] + dp(i+1, color+1, negs+1)
                    min_cost = min(min_cost, cur_cost)
                else:
                    cur_cost = cost[i][color] + dp(i+1, color+1, negs)
                    min_cost = min(min_cost, cur_cost)
            return min_cost

        return dp(0, -1, 0) if dp(0, -1, 0) != float("inf") else -1