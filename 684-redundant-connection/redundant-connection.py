from collections import defaultdict

class Solution:
    def findRedundantConnection(self, edges):
        """
        Given a list of edges representing an undirected graph, find the edge that, 
        if removed, would result in a tree (i.e., no cycles).

        :param edges: List[List[int]] - List of edges where each edge is [u, v].
        :return: List[int] - The redundant edge that creates a cycle.
        """
        adjacency_list = defaultdict(set)

        def has_cycle(node, target):
            """
            Perform DFS to check if there exists a path from `node` to `target`.

            :param node: Current node being visited.
            :param target: Target node to reach.
            :return: bool - True if a path exists, otherwise False.
            """
            if node not in visited_nodes:
                visited_nodes.add(node)
                if node == target:
                    return True
                return any(has_cycle(neighbor, target) for neighbor in adjacency_list[node])
            return False

        # Process each edge in the graph
        for node1, node2 in edges:
            visited_nodes = set()
            # If both nodes already exist in the graph and there's a path between them, a cycle is detected
            if node1 in adjacency_list and node2 in adjacency_list and has_cycle(node1, node2):
                return [node1, node2]
            
            # Otherwise, add the edge to the graph
            adjacency_list[node1].add(node2)
            adjacency_list[node2].add(node1)
