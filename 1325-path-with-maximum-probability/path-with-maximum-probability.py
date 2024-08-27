class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = defaultdict(list)
        for edge, prob in zip(edges, succProb):
            u, v = edge
            graph[u].append((v, prob))
            graph[v].append((u, prob))

        distances = defaultdict(int)
        distances[start_node] = 1
        heap = [(-1, start_node)]

        while heap:
            node_prob, node = heapq.heappop(heap)
            node_prob *= -1
            for neg, edge_prob in graph[node]:
                if node_prob * edge_prob > distances[neg]:
                    distances[neg] = node_prob * edge_prob
                    heapq.heappush(heap, (-distances[neg], neg))
            
        return distances[end_node]
        