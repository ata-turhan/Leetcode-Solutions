import heapq
from typing import List

class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        """
        Connects all sticks in the minimum possible cost.
        
        :param sticks: List[int] - List of stick lengths.
        :return: int - The minimum cost to connect all sticks.
        """
        cost = 0  # Initialize the total cost
        heapq.heapify(sticks)  # Convert the list of sticks into a min-heap

        while len(sticks) > 1:  # Continue until only one stick remains
            shortest = heapq.heappop(sticks)  # Pop the shortest stick
            second_shortest = heapq.heappop(sticks)  # Pop the second shortest stick
            new_stick = shortest + second_shortest  # Combine the two sticks
            heapq.heappush(sticks, new_stick)  # Push the combined stick back into the heap
            cost += new_stick  # Add the cost of this combination to the total cost

        return cost  # Return the total cost to connect all sticks

# Example usage:
# sol = Solution()
# print(sol.connectSticks([2, 4, 3]))  # Output: 14
# print(sol.connectSticks([1, 8, 3, 5]))  # Output: 30
