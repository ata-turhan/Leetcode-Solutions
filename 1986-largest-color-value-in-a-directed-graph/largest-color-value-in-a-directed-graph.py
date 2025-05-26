from collections import deque
from typing import List

class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        # Build graph and indegree array
        graph: List[List[int]] = [[] for _ in range(n)]
        indegree: List[int] = [0] * n
        for u, v in edges:
            graph[u].append(v)
            indegree[v] += 1

        # Initialize DP table: dp[u][c] = max count of color c along any path ending at u
        dp: List[List[int]] = [[0] * 26 for _ in range(n)]
        queue = deque([u for u in range(n) if indegree[u] == 0])

        processed = 0
        max_color_value = 0

        # Kahn's BFS for topological sort + DP propagation
        while queue:
            u = queue.popleft()
            processed += 1

            # Include this node's own color
            color_index = ord(colors[u]) - ord('a')
            dp[u][color_index] += 1
            # Update global maximum
            max_color_value = max(max_color_value, dp[u][color_index])

            # Propagate DP values to neighbors
            for v in graph[u]:
                for c in range(26):
                    # Carry forward the best counts
                    if dp[u][c] > dp[v][c]:
                        dp[v][c] = dp[u][c]
                # Decrease indegree and enqueue if ready
                indegree[v] -= 1
                if indegree[v] == 0:
                    queue.append(v)

        # If not all nodes were processed, a cycle exists
        if processed < n:
            return -1

        return max_color_value
