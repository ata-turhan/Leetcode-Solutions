class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))

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
            return sum(1 for d in distances.values() if d <= distanceThreshold)

        num_negs = [0] * n
        for i in range(n):
            num_negs[i] = dijkstra(i)

        min_neg = min(num_negs)
        for i in range(n-1, -1, -1):
            if num_negs[i] == min_neg:
                return i

        num_negs = [0] * n
        for i in range(n):
            num_negs[i] = dijkstra(i)

        min_neg = min(num_negs)
        print(num_negs)

        for i in range(n-1, -1, -1):
            if num_negs[i] == min_neg:
                return i
