from collections import deque
from typing import List

class Solution:
    def maxTargetNodes(self, 
                       edges1: List[List[int]], 
                       edges2: List[List[int]], 
                       k: int
                      ) -> List[int]:
        """
        For each i in Tree1, returns the maximum number of nodes
        target to i after optimally connecting i to some node in Tree2.
        """
        # Build adjacency lists
        n = len(edges1) + 1
        m = len(edges2) + 1
        adj1 = [[] for _ in range(n)]
        adj2 = [[] for _ in range(m)]
        for u, v in edges1:
            adj1[u].append(v)
            adj1[v].append(u)
        for u, v in edges2:
            adj2[u].append(v)
            adj2[v].append(u)

        # Helper: BFS from `start` over `adj`, counting nodes within `limit` edges
        def bfs_count(adj: List[List[int]], start: int, limit: int) -> int:
            if limit < 0:
                return 0  # no nodes in Tree2 if k-1 < 0
            visited = [False] * len(adj)
            dq = deque([(start, 0)])
            visited[start] = True
            count = 0
            while dq:
                node, dist = dq.popleft()
                # only count if within allowed distance
                if dist <= limit:
                    count += 1
                    # expand further only if we can still stay within limit
                    if dist < limit:
                        for nei in adj[node]:
                            if not visited[nei]:
                                visited[nei] = True
                                dq.append((nei, dist + 1))
            return count

        # 1) Precompute for Tree2: number of nodes ≤ (k-1) from each j
        b2_sizes = [bfs_count(adj2, j, k-1) for j in range(m)]
        max_b2 = max(b2_sizes) if b2_sizes else 0

        # 2) For each i in Tree1: number of nodes ≤ k from i, then add max_b2
        answer = []
        for i in range(n):
            b1 = bfs_count(adj1, i, k)
            answer.append(b1 + max_b2)

        return answer
