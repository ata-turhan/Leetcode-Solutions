class Solution:
    def minimumTime(self, n: int, edges: List[List[int]], disappear: List[int]) -> List[int]:
        # Create adjacency list to represent the graph
        graph = [[] for _ in range(n)]
        for u, v, length in edges:
            graph[u].append((v, length))
            graph[v].append((u, length))
        
        # Initialize distance array with infinity
        distance = [float('inf')] * n
        distance[0] = 0  # Starting node has distance 0
        
        # Initialize priority queue (min-heap) with starting node and its distance
        pq = [(0, 0)]  # (distance, node)
        
        # Dijkstra's algorithm
        while pq:
            dist, node = heapq.heappop(pq)
            # Skip if the node is a disappearing node or its distance is already updated
            if disappear[node] <= dist or dist > distance[node]:
                continue
            # Update distance for each neighbor of the current node
            for neighbor, length in graph[node]:
                # If the neighbor is not disappearing and its distance can be reduced, update the distance
                if disappear[neighbor] > dist + length and dist + length < distance[neighbor]:
                    distance[neighbor] = dist + length
                    heapq.heappush(pq, (dist + length, neighbor))
        
        # If any node is unreachable from node 0, set its distance to -1
        for i in range(n):
            if distance[i] == float('inf'):
                distance[i] = -1
        
        return distance