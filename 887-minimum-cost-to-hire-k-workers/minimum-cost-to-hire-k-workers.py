import heapq
from typing import List

class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        total_cost = float("inf")  # Initialize the total cost to infinity
        qualities = []  # Initialize a heap to store qualities in descending order
        # Calculate the ratio of wage to quality for each worker and sort them
        wages_to_qualities = sorted((w / q, q) for w, q in zip(wage, quality))
        cur_total_quantity = 0  # Initialize the current total quantity of workers

        # Iterate through the sorted list of wage-to-quality ratios
        for wage_to_quality, q in wages_to_qualities:
            heapq.heappush(qualities, -q)  # Push the negative quality onto the heap
            cur_total_quantity += q  # Update the current total quantity

            # If the number of qualities exceeds the maximum allowed, pop the maximum quality
            if len(qualities) > k:
                cur_total_quantity -= -heapq.heappop(qualities)  # Update the current total quantity

            # If the number of qualities equals the maximum allowed, calculate the total cost
            if len(qualities) == k:
                # Calculate the total cost using the current total quantity and wage-to-quality ratio
                total_cost = min(total_cost, cur_total_quantity * wage_to_quality)

        return total_cost  # Return the minimum total cost
