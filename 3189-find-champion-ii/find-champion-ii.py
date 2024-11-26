class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        incoming_edges = [0] * n
        visited_nodes = set()
        queue = deque()
        topo_sort = []

        for u, v in edges:
            graph[u].append(v)
            incoming_edges[v] += 1

        origins = [ i for i in range(n) if incoming_edges[i] == 0 ]

        if len(origins) != 1:
            return -1

        queue.append(origins[0])

        while queue:
            for _ in range(len(queue)):
                visiting_node = queue.popleft()
                if visiting_node in visited_nodes:
                    return -1
                visited_nodes.add(visiting_node)
                topo_sort.append(visiting_node)

                for neighbour in graph[visiting_node]:
                    incoming_edges[neighbour] -= 1
                    if incoming_edges[neighbour] == 0:
                        queue.append(neighbour)

        return topo_sort[0]

        