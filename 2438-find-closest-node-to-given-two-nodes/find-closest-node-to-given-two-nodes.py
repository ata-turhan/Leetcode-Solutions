class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        n = len(edges)

        graph = defaultdict(list)
        for u, v in enumerate(edges):
            if v == -1:
                continue
            graph[u].append(v)

        dist_to_node1 = [-1] * n
        queue = deque( [(node1, 0)])

        while queue:
            node, dist = queue.popleft()
            if dist_to_node1[node] == -1:
                dist_to_node1[node] = dist
                for nei in graph[node]:
                    queue.append((nei, dist + 1))

        dist_to_node2 = [-1] * n
        queue = deque([(node2, 0)])

        while queue:
            node, dist = queue.popleft()
            if dist_to_node2[node] == -1:
                dist_to_node2[node] = dist
                for nei in graph[node]:
                    queue.append((nei, dist + 1))

        min_dist = n
        min_node = -1

        for node in range(n):
            if dist_to_node1[node] == -1 or dist_to_node2[node] == -1:
                continue
            if min_dist > max(dist_to_node1[node], dist_to_node2[node]):
                min_dist = max(dist_to_node1[node], dist_to_node2[node])
                min_node = node

        return min_node
        