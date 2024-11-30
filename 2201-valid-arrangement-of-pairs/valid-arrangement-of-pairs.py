from collections import defaultdict
from typing import List

class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        in_degree = defaultdict(int)
        out_degree = defaultdict(int)
        
        # Step 1: Build the graph and calculate in-degree and out-degree
        for u, v in pairs:
            graph[u].append((v, [u, v]))
            out_degree[u] += 1
            in_degree[v] += 1
        
        # Step 2: Identify the starting node for the Eulerian path
        start_node = None
        for node in graph:
            if out_degree[node] - in_degree[node] == 1:
                start_node = node
                break
        if start_node is None:
            start_node = pairs[0][0]  # If Eulerian circuit, start from any node
        
        # Step 3: Perform Hierholzer's algorithm to find the Eulerian path
        eulerian_path = []
        
        def dfs(node):
            while graph[node]:
                next_node, edge = graph[node].pop()
                dfs(next_node)
                eulerian_path.append(edge)
        
        dfs(start_node)
        
        # Step 4: Reverse the path to get the correct order and return
        return eulerian_path[::-1]
