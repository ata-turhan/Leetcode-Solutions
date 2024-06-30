from typing import List
from functools import cache

class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        @cache
        def dp(house_idx: int, prev_color: int, neighborhoods: int) -> int:
            # Base case: if all houses are processed
            if house_idx == len(houses):
                # If exactly target neighborhoods are formed
                return 0 if neighborhoods == target else float("inf")

            # If the house is already painted
            if houses[house_idx] != 0:
                # If the current house color is the same as the previous house color
                if houses[house_idx] == prev_color:
                    return dp(house_idx + 1, houses[house_idx], neighborhoods)
                else:
                    return dp(house_idx + 1, houses[house_idx], neighborhoods + 1)

            # Initialize minimum cost to infinity
            min_cost = float("inf")
            # Try painting the current house with each color
            for color in range(len(cost[0])):
                if (color + 1) != prev_color:
                    # Calculate cost for painting with a different color
                    current_cost = cost[house_idx][color] + dp(house_idx + 1, color + 1, neighborhoods + 1)
                else:
                    # Calculate cost for painting with the same color
                    current_cost = cost[house_idx][color] + dp(house_idx + 1, color + 1, neighborhoods)

                # Update minimum cost
                min_cost = min(min_cost, current_cost)

            return min_cost

        # Calculate minimum cost and handle the case where it's impossible to form the required neighborhoods
        result = dp(0, -1, 0)
        return result if result != float("inf") else -1
