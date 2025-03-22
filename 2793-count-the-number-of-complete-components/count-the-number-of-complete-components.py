from typing import List, Set
from collections import defaultdict

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        # Build adjacency list for the undirected graph
        graph: dict[int, Set[int]] = defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        visited: Set[int] = set()
        complete_components: int = 0

        def dfs(node: int, component_nodes: Set[int]) -> None:
            """Performs DFS and collects all nodes in the current component."""
            visited.add(node)
            component_nodes.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor, component_nodes)

        for node in range(n):
            if node not in visited:
                component_nodes: Set[int] = set()
                dfs(node, component_nodes)

                # Count edges within the component
                edge_count: int = 0
                for u in component_nodes:
                    edge_count += len(graph[u])
                edge_count //= 2  # Each edge is counted twice

                node_count: int = len(component_nodes)
                max_edges: int = node_count * (node_count - 1) // 2

                # Check if component is complete
                if edge_count == max_edges:
                    complete_components += 1

        return complete_components
