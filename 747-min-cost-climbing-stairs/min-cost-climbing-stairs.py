class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        
        # Handle edge cases
        if n == 0:
            return 0
        if n == 1:
            return cost[0]
        
        # Initialize the costs for the first two steps
        prev2, prev1 = cost[0], cost[1]
        
        # Iterate through the cost array starting from the third step
        for i in range(2, n):
            # Calculate the minimum cost to reach the current step
            current = min(prev1, prev2) + cost[i]
            # Update the previous two steps
            prev2, prev1 = prev1, current
        
        # Return the minimum cost to reach the top of the staircase
        return min(prev1, prev2)
