from heapq import heappop, heappush
from collections import defaultdict

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        # Build the graph
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))

        # Dijkstra's algorithm to find the number of cities reachable within the distance threshold
        def dijkstra(start):
            heap = [(0, start)]
            distances = {i: float('inf') for i in range(n)}
            distances[start] = 0
            
            while heap:
                dist, node = heappop(heap)
                if dist > distances[node]:
                    continue
                for neighbor, weight in graph[node]:
                    new_dist = dist + weight
                    if new_dist < distances[neighbor]:
                        distances[neighbor] = new_dist
                        heappush(heap, (new_dist, neighbor))
            
            # Count the number of cities reachable within the distance threshold
            return sum(1 for d in distances.values() if d <= distanceThreshold)

        # Find the city with the smallest number of reachable cities
        num_reachable_cities = []
        for i in range(n):
            num_reachable_cities.append((dijkstra(i), i))

        # Find the city with the smallest number of reachable cities, preferring the largest index
        num_reachable_cities.sort(key=lambda x: (x[0], -x[1]))

        return num_reachable_cities[0][1]

