from collections import defaultdict
from typing import List

class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        # Count the number of edges connected to each node
        edge_counts = defaultdict(int)
        for road in roads:
            edge_counts[road[0]] += 1
            edge_counts[road[1]] += 1

        # List of nodes sorted by their edge counts
        nodes = list(range(n))
        nodes.sort(key=lambda node: edge_counts[node])

        # Assign increasing importance values to nodes
        importance_values = list(range(1, n + 1))

        # Calculate the total importance based on the edge counts
        total_importance = 0
        for importance, node in zip(importance_values, nodes):
            total_importance += edge_counts[node] * importance

        return total_importance
