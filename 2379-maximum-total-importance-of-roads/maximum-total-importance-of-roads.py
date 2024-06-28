class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        edge_counts = defaultdict(int)

        for road in roads:
            edge_counts[road[0]] += 1
            edge_counts[road[1]] += 1

        nodes = list(range(n))
        nodes.sort(key=lambda node: edge_counts[node])

        orders = list(range(1, n+1))

        total_importance = 0

        for order, node in zip(orders, nodes):
            total_importance += edge_counts[node] * order

        return total_importance        