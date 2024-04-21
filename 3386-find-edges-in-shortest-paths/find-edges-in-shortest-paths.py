from typing import List
from heapq import heappop, heappush

class Solution:
    def findAnswer(self, n: int, edges: List[List[int]]) -> List[bool]:
        """
        Function to find the answers for each edge in the graph.

        Args:
            n: The number of nodes in the graph.
            edges: List of edges represented as tuples (u, v, w), where (u, v) is an edge and w is its weight.

        Returns:
            List of boolean values indicating whether each edge is part of the shortest path from node 0 to node n-1.
        """
        # Initialize the graph as an adjacency list.
        graph = [[] for _ in range(n)]
        # Build the graph using the given edges.
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))
        
        def dijkstra(source):
            """
            Dijkstra's algorithm to find the shortest distances from the source node to all other nodes.

            Args:
                source: The source node from which the shortest distances are calculated.

            Returns:
                List of shortest distances from the source node to all other nodes.
            """
            # Initialize the distances array with infinity for all nodes.
            dist = [float('inf')] * n
            # Distance from the source node to itself is 0.
            dist[source] = 0
            # Priority queue to store nodes based on their distance from the source node.
            pq = [(0, source)]
            # Main loop of Dijkstra's algorithm.
            while pq:
                # Pop the node with the smallest distance from the priority queue.
                x, u = heappop(pq)
                # If the distance recorded for this node is still valid, process its neighbors.
                if dist[u] == x:
                    # Iterate through the neighbors of the current node.
                    for v, w in graph[u]:
                        # Update the distance to the neighbor if a shorter path is found.
                        if x + w < dist[v]:
                            dist[v] = x + w
                            # Add the neighbor to the priority queue with its updated distance.
                            heappush(pq, (x + w, v))
            # Return the shortest distances from the source node to all other nodes.
            return dist 
        
        # Find the shortest distances from the source node (0) and the destination node (n-1).
        dist0 = dijkstra(0)
        dist1 = dijkstra(n - 1)
        # If there is no path from node 0 to node n-1, return a list of False values for all edges.
        if dist0[n - 1] == float('inf'):
            return [False] * len(edges)
        ans = []
        # Iterate through each edge and check if it is part of the shortest path.
        for u, v, w in edges:
            # Check if the sum of distances from source to u, v to destination, and u to v (or vice versa) equals the distance from source to destination.
            ans.append(dist0[u] + w + dist1[v] == dist0[n - 1] or dist0[v] + w + dist1[u] == dist0[n - 1])
        # Return the list of answers for each edge.
        return ans
