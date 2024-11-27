from collections import defaultdict, deque
from typing import List

class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        # Build the initial graph with direct edges between nodes
        graph = defaultdict(list)
        for i in range(n - 1):
            graph[i].append(i + 1)

        # Function to perform BFS and calculate the shortest distance
        def bfs(source: int, destination: int) -> int:
            queue = deque([(source, 0)])  # (current_node, steps)
            visited = set()

            while queue:
                current_node, steps = queue.popleft()
                if current_node in visited:
                    continue
                visited.add(current_node)

                if current_node == destination:
                    return steps

                for neighbor in graph[current_node]:
                    if neighbor not in visited:
                        queue.append((neighbor, steps + 1))

            return -1  # Return -1 if destination is unreachable

        # Process each query and compute the result
        results = []
        for source, destination in queries:
            graph[source].append(destination)  # Add the new edge
            distance = bfs(0, n - 1)  # Perform BFS from node 0 to node n-1
            results.append(distance)

        return results
