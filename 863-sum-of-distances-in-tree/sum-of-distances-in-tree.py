from collections import defaultdict
from typing import List

class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        # Create an adjacency list to represent the tree
        tree = defaultdict(list)
        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)

        # Initialize result list and counts list
        res = [0] * n
        counts = [1] * n

        # Perform post-order depth-first search (DFS)
        def post_order_dfs(node, parent):
            for child in tree[node]:
                if child != parent:
                    # Recursively visit child nodes
                    post_order_dfs(child, node)
                    # Update counts and result for the current node
                    counts[node] += counts[child]
                    res[node] += res[child] + counts[child]

        # Perform pre-order depth-first search (DFS)
        def pre_order_dfs(node, parent):
            for child in tree[node]:
                if child != parent:
                    # Update result for the child nodes
                    res[child] = res[node] + n - 2 * counts[child]
                    # Recursively visit child nodes
                    pre_order_dfs(child, node)

        # Start DFS from the root node (0)
        post_order_dfs(0, None)
        pre_order_dfs(0, None)

        return res
