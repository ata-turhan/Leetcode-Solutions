from typing import List
from collections import deque

class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        def bfs(start_node: int) -> List[int]:
            distance = [-1] * len(edges)
            queue = deque([(start_node, 0)])

            while queue:
                current, dist = queue.popleft()
                if distance[current] != -1:
                    continue
                distance[current] = dist
                neighbor = edges[current]
                if neighbor != -1:
                    queue.append((neighbor, dist + 1))
            return distance

        distance_from_node1 = bfs(node1)
        distance_from_node2 = bfs(node2)

        min_max_distance = float('inf')
        result_node = -1

        for node in range(len(edges)):
            d1, d2 = distance_from_node1[node], distance_from_node2[node]
            if d1 != -1 and d2 != -1:
                max_distance = max(d1, d2)
                if max_distance < min_max_distance:
                    min_max_distance = max_distance
                    result_node = node

        return result_node
