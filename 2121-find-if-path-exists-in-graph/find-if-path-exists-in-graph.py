from collections import defaultdict, deque

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # Create an adjacency list to represent the graph
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # Perform BFS to find if there is a valid path from source to destination
        queue = deque([source])
        visited = set()
        
        while queue:
            node = queue.popleft()
            if node == destination:
                return True
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
        
        return False
