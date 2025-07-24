from typing import List

class Solution:
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        """
        Return the minimum score obtainable by removing two distinct edges from a tree,
        where score = (largest component XOR) - (smallest component XOR).
        
        Approach:
        1. Root the tree at node 0.
        2. DFS to compute:
           - xor_subtree[u]: XOR of all node values in u's subtree.
           - tin[u], tout[u]: entry/exit times for ancestor checks.
        3. For each pair of removal edges (represented by their child endpoints u and v):
           - If one subtree is nested in the other, compute component XORs accordingly.
           - Otherwise, treat them as disjoint subtrees and compute three XORs.
        4. Track and return the minimum score across all pairs.
        
        Time Complexity: O(n²) for pairwise evaluation (n ≤ 1000).
        Space Complexity: O(n).
        """
        n = len(nums)
        # Build adjacency list
        adj: List[List[int]] = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # Arrays for parent, subtree XOR, and Euler tour times
        parent = [-1] * n
        xor_subtree = [0] * n
        tin = [0] * n
        tout = [0] * n

        timer = 0
        import sys
        sys.setrecursionlimit(10**7)

        def dfs(u: int, p: int) -> None:
            nonlocal timer
            parent[u] = p
            timer += 1
            tin[u] = timer

            # Start XOR accumulation with the node's own value
            current_xor = nums[u]
            for w in adj[u]:
                if w == p:
                    continue
                dfs(w, u)
                current_xor ^= xor_subtree[w]

            xor_subtree[u] = current_xor

            timer += 1
            tout[u] = timer

        # 1. Run DFS from root = 0
        dfs(0, -1)
        total_xor = xor_subtree[0]

        def is_ancestor(a: int, b: int) -> bool:
            """
            Return True if node a is an ancestor of node b
            in the rooted tree, based on entry/exit times.
            """
            return tin[a] <= tin[b] and tout[b] <= tout[a]

        # Prepare list of candidate cut points (every node except the root)
        cut_nodes = list(range(1, n))
        min_score = float('inf')

        # 2. Evaluate every pair of cuts (u, v)
        for i in range(len(cut_nodes)):
            u = cut_nodes[i]
            for j in range(i + 1, len(cut_nodes)):
                v = cut_nodes[j]

                # Determine the three component XORs based on nesting
                if is_ancestor(u, v):
                    # v-subtree inside u-subtree
                    xor1 = xor_subtree[v]
                    xor2 = xor_subtree[u] ^ xor_subtree[v]
                    xor3 = total_xor ^ xor_subtree[u]
                elif is_ancestor(v, u):
                    # u-subtree inside v-subtree
                    xor1 = xor_subtree[u]
                    xor2 = xor_subtree[v] ^ xor_subtree[u]
                    xor3 = total_xor ^ xor_subtree[v]
                else:
                    # Disjoint subtrees
                    xor1 = xor_subtree[u]
                    xor2 = xor_subtree[v]
                    xor3 = total_xor ^ xor_subtree[u] ^ xor_subtree[v]

                # Compute and update score
                current_score = max(xor1, xor2, xor3) - min(xor1, xor2, xor3)
                if current_score < min_score:
                    min_score = current_score

        return min_score
