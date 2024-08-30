from typing import List, Tuple
import heapq
import math

class Solution:
    def modifiedGraphEdges(
        self,
        n: int,
        edges: List[List[int]],
        source: int,
        destination: int,
        target: int,
    ) -> List[List[int]]:
        INF = int(2e9)
        graph = [[] for _ in range(n)]

        # Build the graph with known weights
        for u, v, w in edges:
            if w != -1:
                graph[u].append((v, w))
                graph[v].append((u, w))

        # Compute the initial shortest distance
        current_shortest_distance = self._dijkstra(graph, source, destination)
        if current_shortest_distance < target:
            return []

        if current_shortest_distance == target:
            # Update edges with -1 weight to an impossible value
            for edge in edges:
                if edge[2] == -1:
                    edge[2] = INF
            return edges

        # Adjust edges with unknown weights
        for i, (u, v, w) in enumerate(edges):
            if w != -1:
                continue

            # Set edge weight to 1 initially
            edges[i][2] = 1
            graph[u].append((v, 1))
            graph[v].append((u, 1))

            # Recompute shortest distance with updated edge weight
            new_distance = self._dijkstra(graph, source, destination)

            if new_distance <= target:
                # Adjust edge weight to exactly match the target
                edges[i][2] += target - new_distance

                # Update remaining edges with -1 weight to an impossible value
                for j in range(i + 1, len(edges)):
                    if edges[j][2] == -1:
                        edges[j][2] = INF
                return edges

        return []

    def _dijkstra(
        self, graph: List[List[Tuple[int, int]]], src: int, destination: int
    ) -> int:
        # Initialize the minimum distance to each node as infinity
        min_distance = [math.inf] * len(graph)
        min_distance[src] = 0

        # Min-heap to store (distance, node) tuples for exploration
        min_heap = [(0, src)]

        while min_heap:
            d, u = heapq.heappop(min_heap)

            # Skip processing if the current distance is greater than recorded
            if d > min_distance[u]:
                continue

            # Explore all adjacent nodes
            for v, w in graph[u]:
                if d + w < min_distance[v]:
                    min_distance[v] = d + w
                    heapq.heappush(min_heap, (min_distance[v], v))

        # Return the shortest distance to the destination
        return min_distance[destination]
