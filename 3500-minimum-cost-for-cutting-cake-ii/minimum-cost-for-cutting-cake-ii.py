class Solution:
    def minimumCost(self, m: int, n: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        # Sort the cuts in descending order to maximize the cost savings
        horizontalCuts.sort(reverse=True)
        verticalCuts.sort(reverse=True)

        # Initialize the number of horizontal and vertical segments
        horizontal_segments = 1
        vertical_segments = 1

        total_cost = 0
        h_index, v_index = 0, 0

        # Use a greedy approach to pick the most expensive cut at each step
        while h_index < len(horizontalCuts) and v_index < len(verticalCuts):
            if horizontalCuts[h_index] >= verticalCuts[v_index]:
                # Add cost of the horizontal cut multiplied by the number of horizontal segments
                total_cost += horizontalCuts[h_index] * horizontal_segments
                # Increment the number of vertical segments
                vertical_segments += 1
                h_index += 1
            else:
                # Add cost of the vertical cut multiplied by the number of vertical segments
                total_cost += verticalCuts[v_index] * vertical_segments
                # Increment the number of horizontal segments
                horizontal_segments += 1
                v_index += 1

        # Add remaining horizontal cuts
        while h_index < len(horizontalCuts):
            total_cost += horizontalCuts[h_index] * horizontal_segments
            h_index += 1

        # Add remaining vertical cuts
        while v_index < len(verticalCuts):
            total_cost += verticalCuts[v_index] * vertical_segments
            v_index += 1

        return total_cost
