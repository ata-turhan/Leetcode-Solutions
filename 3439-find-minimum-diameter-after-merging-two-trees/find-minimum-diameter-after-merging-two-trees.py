from collections import deque, defaultdict

class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        def bfs_diameter(tree, start):
            # Perform BFS to find the farthest node and distance
            def bfs(node):
                q = deque([node])
                distances = {node: 0}
                farthest_node = node
                max_distance = 0
                
                while q:
                    current = q.popleft()
                    current_distance = distances[current]
                    
                    for neighbor in tree[current]:
                        if neighbor not in distances:
                            distances[neighbor] = current_distance + 1
                            q.append(neighbor)
                            if distances[neighbor] > max_distance:
                                max_distance = distances[neighbor]
                                farthest_node = neighbor
                
                return farthest_node, max_distance
            
            # First BFS to find the farthest node from the start
            farthest_node, _ = bfs(start)
            # Second BFS from the farthest node to find the diameter
            other_end, diameter = bfs(farthest_node)
            
            # Perform BFS again to find the distance from farthest_node to all other nodes
            q = deque([farthest_node])
            distances = {farthest_node: 0}
            while q:
                current = q.popleft()
                current_distance = distances[current]
                
                for neighbor in tree[current]:
                    if neighbor not in distances:
                        distances[neighbor] = current_distance + 1
                        q.append(neighbor)
            
            # Find the center of the diameter
            path = []
            node = other_end
            while distances[node] > diameter // 2:
                for neighbor in tree[node]:
                    if distances[neighbor] == distances[node] - 1:
                        path.append(node)
                        node = neighbor
                        break
            
            center = node
            return diameter, center

        tree1 = defaultdict(list)
        tree2 = defaultdict(list)
        
        for u, v in edges1:
            tree1[u].append(v)
            tree1[v].append(u)
        
        for u, v in edges2:
            tree2[u].append(v)
            tree2[v].append(u)
        
        # Find diameters and centers of both trees
        diameter1, center1 = bfs_diameter(tree1, 0)
        diameter2, center2 = bfs_diameter(tree2, 0)
        
        # Calculate the minimum possible diameter after merging
        min_diameter = max(diameter1, diameter2, (diameter1 + 1) // 2 + (diameter2 + 1) // 2 + 1)
        
        return min_diameter


        