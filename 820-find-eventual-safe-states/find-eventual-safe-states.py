class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        
        # Step 1: Build reverse graph and calculate outdegrees
        reverse_graph = [[] for _ in range(n)]
        outdegree = [0] * n
        
        for u in range(n):
            for v in graph[u]:
                reverse_graph[v].append(u)
                outdegree[u] += 1
                
        # Step 2: Initialize queue with all nodes having outdegree == 0 (terminal nodes)
        queue = deque([i for i in range(n) if outdegree[i] == 0])
        
        # We'll maintain a list or boolean array to mark safe nodes
        safe = [False] * n
        for node in queue:
            safe[node] = True  # Terminal nodes are immediately safe
        
        # Step 3: Process the queue
        while queue:
            curr = queue.popleft()
            # For each predecessor of curr in reverse graph
            for prev in reverse_graph[curr]:
                outdegree[prev] -= 1
                if outdegree[prev] == 0:
                    safe[prev] = True
                    queue.append(prev)
        
        # Step 4: Gather all safe nodes in sorted order
        result = [i for i in range(n) if safe[i]]
        result.sort()
        return result