from collections import defaultdict
from typing import List

class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        """
        Calculate the maximum number of components in the tree where the sum of node values 
        in each component is divisible by k.

        :param n: Number of nodes in the tree.
        :param edges: List of edges in the tree.
        :param values: List of node values.
        :param k: The divisor for checking divisibility.
        :return: Maximum number of divisible components.
        """
        # Build the adjacency list representation of the tree
        adjacency_list = defaultdict(list)
        for node_a, node_b in edges:
            adjacency_list[node_a].append(node_b)
            adjacency_list[node_b].append(node_a)

        def dfs(current_node: int, parent_node: int) -> int:
            """
            Perform DFS to calculate the sum of values in the subtree rooted at `current_node`.
            Split components where the subtree sum is divisible by `k`.
            
            :param current_node: Current node being visited.
            :param parent_node: Parent of the current node in the tree.
            :return: The remaining sum of the subtree if not divisible by `k`.
            """
            subtree_sum = values[current_node]
            for neighbor in adjacency_list[current_node]:
                if neighbor != parent_node:
                    # Recursively calculate the subtree sum for child nodes
                    subtree_sum += dfs(neighbor, current_node)

            # Check if the subtree sum is divisible by `k`
            if subtree_sum % k == 0:
                nonlocal divisible_components
                divisible_components += 1  # Count this as a divisible component
                return 0  # Reset sum for this component
            else:
                return subtree_sum  # Return remaining sum for further calculations

        divisible_components = 0
        dfs(0, -1)  # Start DFS from node 0 as the root, with no parent
        return divisible_components
