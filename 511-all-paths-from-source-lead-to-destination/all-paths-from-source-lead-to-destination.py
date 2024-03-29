class Solution:
    # Define constants for node states
    GRAY = 1  # Gray state indicates node is being visited
    BLACK = 2  # Black state indicates node has been visited and processed

    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # Initialize an adjacency list to represent the graph
        graph = [[] for _ in range(n)]
        # Populate the adjacency list with edges
        for u, v in edges:
            graph[u].append(v)
        
        # Initialize an array to track node states during traversal
        states = [None] * n
        
        # Nested function to perform depth-first search (DFS)
        def dfs(node):
            # If the node is already processed, return True
            if states[node] == self.BLACK:
                return True
            # If the node is being visited again (GRAY state), it indicates a cycle
            if states[node] == self.GRAY:
                return False
            # If the node is a leaf node, it should be the destination
            if not graph[node]:
                return node == destination
            
            # Mark the node as being visited (GRAY state)
            states[node] = self.GRAY
            
            # Traverse the neighbors of the current node
            for next_node in graph[node]:
                # If any neighbor leads to a cycle, return False
                if not dfs(next_node):
                    return False
            
            # Mark the node as visited and processed (BLACK state)
            states[node] = self.BLACK
            return True
        
        # Perform depth-first search (DFS) from the source node
        return dfs(source)
