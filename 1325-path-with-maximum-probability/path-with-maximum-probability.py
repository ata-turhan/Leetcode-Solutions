from collections import defaultdict
import heapq
from typing import List

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        # Build the graph as an adjacency list where each node points to a list of tuples (neighbor, success_probability)
        adjacency_list = defaultdict(list)
        for (src, dest), probability in zip(edges, succProb):
            adjacency_list[src].append((dest, probability))
            adjacency_list[dest].append((src, probability))

        # Dictionary to store the maximum probability to reach each node
        max_probabilities = defaultdict(int)
        max_probabilities[start_node] = 1  # Start node has a probability of 1 to reach itself

        # Max heap to prioritize the nodes with the highest probability
        max_heap = [(-1, start_node)]  # Use negative probability to simulate a max heap using heapq

        while max_heap:
            # Pop the node with the highest probability
            current_prob, current_node = heapq.heappop(max_heap)
            current_prob *= -1  # Convert back to positive probability

            # Explore neighbors
            for neighbor, edge_prob in adjacency_list[current_node]:
                # Calculate the probability of reaching the neighbor through the current node
                new_prob = current_prob * edge_prob
                if new_prob > max_probabilities[neighbor]:
                    max_probabilities[neighbor] = new_prob
                    heapq.heappush(max_heap, (-new_prob, neighbor))

        # Return the probability to reach the end_node, or 0 if it's unreachable
        return max_probabilities[end_node]
