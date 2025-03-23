from typing import List
import heapq

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        MOD: int = 10**9 + 7

        # Step 1: Build graph
        graph: List[List[tuple[int, int]]] = [[] for _ in range(n)]
        for u, v, time in roads:
            graph[u].append((v, time))
            graph[v].append((u, time))

        # Step 2: Dijkstra’s initialization
        dist: List[int] = [float('inf')] * n
        count: List[int] = [0] * n
        dist[0], count[0] = 0, 1
        heap: List[tuple[int, int]] = [(0, 0)]  # (time, node)

        # Step 3: Dijkstra + path counting
        while heap:
            time_u, u = heapq.heappop(heap)

            if time_u > dist[u]:
                continue  # Skip if not optimal

            for v, time_uv in graph[u]:
                new_time = time_u + time_uv

                if new_time < dist[v]:
                    dist[v] = new_time
                    count[v] = count[u]
                    heapq.heappush(heap, (new_time, v))
                elif new_time == dist[v]:
                    count[v] = (count[v] + count[u]) % MOD

        return count[n - 1]
