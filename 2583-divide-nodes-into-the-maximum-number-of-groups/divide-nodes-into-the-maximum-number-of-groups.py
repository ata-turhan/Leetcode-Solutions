from collections import deque
from typing import List

class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        # 1) Build adjacency list
        graph = [[] for _ in range(n+1)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        # 2) Check bipartite using coloring (0/1). If not bipartite, return -1
        color = [-1] * (n+1)

        def bfs_check_bipartite(start: int) -> bool:
            queue = deque([start])
            color[start] = 0
            while queue:
                node = queue.popleft()
                for nxt in graph[node]:
                    if color[nxt] == -1:
                        color[nxt] = 1 - color[node]
                        queue.append(nxt)
                    elif color[nxt] == color[node]:
                        return False  # same color => not bipartite
            return True

        for node in range(1, n+1):
            if color[node] == -1:  # not visited
                if not bfs_check_bipartite(node):
                    return -1

        # 3) For each connected component, find maximum BFS layering that is valid
        visited = [False] * (n+1)

        def bfs_get_component(start: int) -> List[int]:
            """Collect all nodes in the connected component of 'start'."""
            comp_nodes = []
            queue = deque([start])
            visited[start] = True
            while queue:
                node = queue.popleft()
                comp_nodes.append(node)
                for nxt in graph[node]:
                    if not visited[nxt]:
                        visited[nxt] = True
                        queue.append(nxt)
            return comp_nodes

        # Check if BFS layering from 'root' is valid; if valid, return maximum depth
        def check_layering_and_get_depth(root: int, comp_nodes: List[int]) -> int:
            depth = [-1] * (n+1)
            depth[root] = 0
            queue = deque([root])
            while queue:
                node = queue.popleft()
                for nxt in graph[node]:
                    if depth[nxt] == -1:
                        depth[nxt] = depth[node] + 1
                        queue.append(nxt)
            # Now verify all edges in the component
            for node in comp_nodes:
                for nxt in graph[node]:
                    # only check edges within this component
                    # (both node and nxt in comp_nodes)
                    # a simple check: node in comp and nxt in comp is guaranteed by BFS
                    # but let's be safe:
                    if depth[nxt] != -1:
                        # If depths differ by anything other than 1, invalid layering
                        if abs(depth[node] - depth[nxt]) != 1:
                            return -1  # invalid layering
            # layering is valid, return the maximum depth used
            return max(depth[x] for x in comp_nodes if depth[x] != -1)

        answer = 0
        for node in range(1, n+1):
            if not visited[node]:
                # get connected component
                comp_nodes = bfs_get_component(node)
                # try BFS from every node in this component
                best_depth = -1
                for candidate_root in comp_nodes:
                    layer_depth = check_layering_and_get_depth(candidate_root, comp_nodes)
                    best_depth = max(best_depth, layer_depth)
                # If for all roots layering was invalid, best_depth would remain -1
                if best_depth < 0:
                    return -1  # Means no valid layering found
                # Add (best_depth + 1) to final answer
                answer += (best_depth + 1)

        return answer
