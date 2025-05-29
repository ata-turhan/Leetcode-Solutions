from typing import List
from collections import deque

class Solution:
    def maxTargetNodes(
        self,
        edges1: List[List[int]],
        edges2: List[List[int]]
    ) -> List[int]:
        """
        For each node i in the first tree, compute the maximum number of
        nodes at even distance (target nodes) across both trees when i
        is optimally connected to one node in the second tree.
        """

        def build_adj(edges: List[List[int]], size: int) -> List[List[int]]:
            adj = [[] for _ in range(size)]
            for u, v in edges:
                adj[u].append(v)
                adj[v].append(u)
            return adj

        def bfs_parity(adj: List[List[int]]) -> (List[int], List[int]):
            """
            Performs a BFS from node 0, computing each node's depth parity
            (0 or 1) and returning the depth list and a two‐element count
            of how many nodes have parity 0 and 1 respectively.
            """
            n = len(adj)
            depth = [-1] * n
            depth[0] = 0
            counts = [1, 0]  # we start with node 0 at parity 0
            queue = deque([0])

            while queue:
                u = queue.popleft()
                for w in adj[u]:
                    if depth[w] == -1:
                        depth[w] = depth[u] ^ 1
                        counts[depth[w]] += 1
                        queue.append(w)
            return depth, counts

        # Number of nodes in each tree
        n = len(edges1) + 1
        m = len(edges2) + 1

        # Build adjacency lists
        tree1 = build_adj(edges1, n)
        tree2 = build_adj(edges2, m)

        # Compute parity depths and counts for both trees
        depth1, count1 = bfs_parity(tree1)
        depth2, count2 = bfs_parity(tree2)

        # The best we can do in tree2 is attach to whichever parity yields more odd‐distance nodes
        max_odd_in_tree2 = max(count2)

        # For each node i in tree1, its even‐distance count is count1[depth1[i]]
        # Total = even‐distance in tree1 + best odd‐distance in tree2
        return [count1[depth1[i]] + max_odd_in_tree2 for i in range(n)]
