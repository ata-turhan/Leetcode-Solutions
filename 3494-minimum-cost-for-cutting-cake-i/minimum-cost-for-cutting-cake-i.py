class Solution:
    def minimumCost(self, m: int, n: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        # Sort the cuts in descending order
        horizontalCuts.sort(reverse=True)
        verticalCuts.sort(reverse=True)

        # Initialize the number of horizontal and vertical pieces
        horizontal_pieces = 1
        vertical_pieces = 1

        total_cost = 0
        i, j = 0, 0

        # Use a greedy approach to pick the most expensive cut at each step
        while i < len(horizontalCuts) and j < len(verticalCuts):
            if horizontalCuts[i] >= verticalCuts[j]:
                total_cost += horizontalCuts[i] * horizontal_pieces
                vertical_pieces += 1
                i += 1
            else:
                total_cost += verticalCuts[j] * vertical_pieces
                horizontal_pieces += 1
                j += 1

        # If there are remaining horizontal cuts
        while i < len(horizontalCuts):
            total_cost += horizontalCuts[i] * horizontal_pieces
            i += 1

        # If there are remaining vertical cuts
        while j < len(verticalCuts):
            total_cost += verticalCuts[j] * vertical_pieces
            j += 1

        return total_cost
