from collections import Counter
from typing import List

class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        """
        Return the minimum cost to make basket1 and basket2 equal
        by swapping fruits at cost = min(value1, value2) per swap.
        If impossible, return -1.
        """
        # Frequency maps for each basket
        freq1 = Counter(basket1)
        freq2 = Counter(basket2)
        
        # Global minimum fruit cost across both baskets
        all_values = list(freq1.keys() | freq2.keys())
        gmin = min(all_values)
        
        # Check overall feasibility: each cost must appear an even total number of times
        for v in all_values:
            if (freq1[v] + freq2[v]) & 1:
                return -1
        
        # Collect surplus fruits to swap
        extra1, extra2 = [], []
        for v in all_values:
            diff = freq1[v] - freq2[v]
            if diff > 0:
                # Surplus in basket1: need to move diff//2 copies to basket2
                extra1.extend([v] * (diff // 2))
            elif diff < 0:
                # Surplus in basket2: need to move (-diff)//2 copies to basket1
                extra2.extend([v] * ((-diff) // 2))
        
        # No swaps needed
        if not extra1:
            return 0
        
        # Sort for optimal pairing: smallest extras from basket1 with largest extras from basket2
        extra1.sort()
        extra2.sort(reverse=True)
        
        # Compute total minimal cost
        total_cost = 0
        for a, b in zip(extra1, extra2):
            # Direct swap vs. two-step via global minimum
            cost_direct = min(a, b)
            cost_indirect = 2 * gmin
            total_cost += min(cost_direct, cost_indirect)
        
        return total_cost
