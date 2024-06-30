from typing import List
from functools import cache
import math

class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        @cache
        def min_paint_cost(house_idx: int, prev_color: int) -> int:
            # Base case: If all houses are painted
            if house_idx == len(costs):
                return 0

            # Initialize the minimum cost to a large number
            min_cost = math.inf
            # Try painting the current house with each color
            for color in range(3):
                if color != prev_color:
                    # Calculate the cost of painting the current house and the rest
                    cost = costs[house_idx][color] + min_paint_cost(house_idx + 1, color)
                    # Update the minimum cost
                    min_cost = min(min_cost, cost)

            return min_cost

        # Start from the first house with no previous color
        return min_paint_cost(0, -1)
