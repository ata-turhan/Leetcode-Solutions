from collections import defaultdict, deque
from typing import List
from sortedcontainers import SortedSet

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        # Initialize ancestor sets for each node
        ancestors = [SortedSet() for _ in range(n)]
        queue = deque()
        adj_list = defaultdict(list)
        incoming_edges = [0] * n

        # Build adjacency list and count incoming edges for each node
        for u, v in edges:
            incoming_edges[v] += 1       
            adj_list[u].append(v) 

        # Enqueue nodes with no incoming edges
        for i in range(n):
            if incoming_edges[i] == 0:
                queue.append(i)

        # Process nodes in topological order
        while queue:
            node = queue.popleft()
            for neighbor in adj_list[node]:
                # Add current node as an ancestor of its neighbors
                ancestors[neighbor].add(node)
                # Add all ancestors of current node to its neighbors
                ancestors[neighbor].update(ancestors[node])

                # Decrease the incoming edge count and enqueue if it reaches zero
                incoming_edges[neighbor] -= 1
                if incoming_edges[neighbor] == 0:
                    queue.append(neighbor)

        return [ancestor_set for ancestor_set in ancestors]
