from collections import defaultdict
from typing import List

class Solution:
    def countGoodNodes(self, edges: List[List[int]]) -> int:
        # Create the graph as an adjacency list
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)  # Since it's an undirected graph, add both directions

        res = [0]  # This will store the count of good nodes
        
        def dfs(node: int, parent: int) -> int:
            """
            Perform DFS to count the good nodes.
            
            :param node: The current node being visited.
            :param parent: The parent node from which we came to this node.
            :return: The size of the subtree rooted at this node.
            """
            if len(graph[node]) == 1 and node != 0:  # Check if the node is a leaf (not the root)
                res[0] += 1
                return 1
            
            subtree_sizes = []
            
            # Visit all neighbors except the parent node to avoid cycles
            for neighbor in graph[node]:
                if neighbor != parent:
                    subtree_sizes.append(dfs(neighbor, node))
            
            # If all subtree sizes are the same, the node is considered "good"
            if len(set(subtree_sizes)) <= 1:
                res[0] += 1
                
            # Return the size of the subtree rooted at the current node
            return sum(subtree_sizes) + 1

        # Start DFS from the root node, which is considered to be node 0
        dfs(0, -1)

        # Return the total count of good nodes
        return res[0]
