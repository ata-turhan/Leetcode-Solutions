from collections import defaultdict

class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:        
        graph = defaultdict(list)
        in_degree = defaultdict(int)
        out_degree = defaultdict(int)
        
        # Build graph and degree counts
        for pair in pairs:
            u, v = pair
            graph[u].append((v, pair))
            out_degree[u] += 1
            in_degree[v] += 1
        
        # Find the starting node for Eulerian path
        start = None
        for node in graph:
            if out_degree[node] - in_degree[node] == 1:
                start = node
                break
        if start is None:
            start = pairs[0][0]  # Start at any node if Eulerian circuit
        
        path = []
        def dfs(u):
            while graph[u]:
                v, pair = graph[u].pop()
                dfs(v)
                path.append(pair)
        
        dfs(start)
        return path[::-1]
