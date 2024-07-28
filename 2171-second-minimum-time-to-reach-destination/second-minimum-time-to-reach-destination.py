from heapq import heappush, heappop
from collections import defaultdict
import math

class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        # Build the graph using adjacency list
        graph = defaultdict(list)
        for src, dest in edges:
            graph[src].append(dest)
            graph[dest].append(src)
        
        # Initialize distances and visit count arrays
        first_shortest = [math.inf] * (n + 1)  # First shortest path to each node
        second_shortest = [math.inf] * (n + 1)  # Second shortest path to each node
        visit_count = [0] * (n + 1)  # Frequency of reaching each node
        
        # Priority queue (min-heap) to store (time_taken, node)
        min_heap = []
        heappush(min_heap, (0, 1))  # Start from node 1 with time 0
        first_shortest[1] = 0
        
        while min_heap:
            current_time, node = heappop(min_heap)
            visit_count[node] += 1

            # If the destination node is reached for the second time, return the time taken
            if visit_count[node] == 2 and node == n:
                return current_time
            
            # Adjust the time taken considering the traffic light cycle
            if (current_time // change) % 2 == 1:
                # Wait for the green light
                current_time = change * (current_time // change + 1) + time
            else:
                # No wait needed
                current_time += time

            # Traverse all the neighbors of the current node
            for neighbor in graph[node]:
                if visit_count[neighbor] == 2:
                    continue  # Skip if the neighbor is already visited twice

                if first_shortest[neighbor] > current_time:
                    # Update first shortest path and push to heap
                    second_shortest[neighbor] = first_shortest[neighbor]
                    first_shortest[neighbor] = current_time
                    heappush(min_heap, (current_time, neighbor))
                elif second_shortest[neighbor] > current_time and first_shortest[neighbor] != current_time:
                    # Update second shortest path if a valid time is found
                    second_shortest[neighbor] = current_time
                    heappush(min_heap, (current_time, neighbor))
        
        return 0
