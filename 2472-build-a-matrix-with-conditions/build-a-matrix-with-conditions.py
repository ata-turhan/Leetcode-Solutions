from collections import defaultdict, deque
from typing import List

class Solution:
    def topological_sort(self, k: int, conditions: List[List[int]]) -> List[int]:
        # Initialize in-degree of each node to 0 and create an adjacency list
        in_degree = {i: 0 for i in range(1, k + 1)}
        graph = defaultdict(list)
        
        # Build the graph and update in-degrees based on conditions
        for u, v in conditions:
            graph[u].append(v)
            in_degree[v] += 1
        
        # Collect nodes with in-degree of 0 to start the topological sort
        queue = deque([node for node in in_degree if in_degree[node] == 0])
        order = []
        
        # Perform topological sorting using BFS
        while queue:
            node = queue.popleft()
            order.append(node)
            
            for neighbor in graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        # Return the order if it includes all nodes, otherwise return an empty list
        return order if len(order) == k else []

    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        # Get the topological order for rows and columns
        row_order = self.topological_sort(k, rowConditions)
        col_order = self.topological_sort(k, colConditions)
        
        # If topological sorting is not possible for either, return an empty matrix
        if not row_order or not col_order:
            return []
        
        # Create dictionaries to map each number to its position in the order
        row_pos = {num: i for i, num in enumerate(row_order)}
        col_pos = {num: i for i, num in enumerate(col_order)}
        
        # Initialize an empty matrix
        matrix = [[0] * k for _ in range(k)]
        
        # Place numbers in the matrix based on their row and column positions
        for num in range(1, k + 1):
            matrix[row_pos[num]][col_pos[num]] = num
        
        return matrix
